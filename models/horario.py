from scripts.database import get_db_connection
from typing import List
from datetime import datetime, timedelta
import pandas as pd
from io import BytesIO
import base64
from flask import jsonify

class Horario:

    def __init__(self, course_id):
        self.course_id = course_id


def gerar_horario(curso_id, data_inicio) -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    select_areaUnique = '''SELECT area_id, name FROM course WHERE id = %s'''
    cursor.execute(select_areaUnique, (curso_id,))
    results = cursor.fetchall()
    area_id = results[0][0]
    course_name = results[0][1]

    select_discipline = '''SELECT d.id as id_discipline, d.name as name_discipline, d.course_id, 
    d.teacher_id, d.workload, t.id as id_teacher, t.name as name_teacher FROM discipline AS d
    LEFT JOIN teacher AS t ON d.teacher_id = t.id WHERE course_id = %s;'''
    cursor.execute(select_discipline, (curso_id,))
    results = cursor.fetchall()

    discipline = []
    for result in results:
        disciplines = {
            'id_discipline': result[0],
            'name_discipline': result[1],
            'course_id': result[2],
            'teacher_id': result[3],
            'workload': result[4],
            'id_teacher': result[5],
            'name_teacher': result[6]
        }

        discipline.append(disciplines)

    select_instructor = '''SELECT id,name, area_id FROM instructor WHERE area_id = %s;'''
    cursor.execute(select_instructor, (area_id,))
    results = cursor.fetchall()

    instructor = []
    for result in results:
        instructors = {
            'id': result[0],
            'name': result[1],
            'area_id': result[2],
        }

        instructor.append(instructors)

    select_classroom = '''SELECT id,name, nb_places, area_id FROM classroom WHERE area_id = %s;'''
    cursor.execute(select_classroom, (area_id,))
    results = cursor.fetchall()

    classroom = []
    for result in results:
        classrooms = {
            'id': result[0],
            'name': result[1],
            'nb_places': result[2],
            'area_id': result[3],
        }

        classroom.append(classrooms)

    cursor.close()
    conn.close()

    data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d')  # Exemplo de data de início
    horario = []

    # Converte a carga horária total para a quantidade de aulas
    for disciplina in discipline:
        total_aulas = int(disciplina["workload"] / 0.75)

        # Encontra todas as salas compatíveis com a área do curso e as separa por "|"
        salas_disponiveis = [s["name"] for s in classroom if s["area_id"] == area_id]
        salas_str = " | ".join(salas_disponiveis)

        # Encontra todos os instrutores compatíveis com a área do curso e os separa por "|"
        instrutores_disponiveis = [i["name"] for i in instructor if i["area_id"] == area_id]
        instrutores_str = " | ".join(instrutores_disponiveis)

        # Defina o número de aulas semanais e inicialize a contagem de semanas
        aulas_por_semana = 5
        semanas = 0

        while total_aulas > 0:
            # Calcula a data da semana atual
            data_semana = data_inicio + timedelta(weeks=semanas)

            # Calcula o número de aulas para esta semana
            aulas_na_semana = min(aulas_por_semana, total_aulas)

            # Define o instrutor com base na condição
            if disciplina["id_teacher"] is not None:
                instrutor = disciplina["name_teacher"]
            else:
                instrutor = instrutores_str

            # Adiciona a entrada no horário
            horario.append({
                "curso": course_name,
                "disciplina": disciplina["name_discipline"],
                "instrutor": instrutor,
                "sala": salas_str,
                "data": data_semana.strftime("%Y-%m-%d"),
                "aulas_na_semana": aulas_na_semana,
                "aulas_restantes": total_aulas
            })

            total_aulas -= aulas_na_semana

            # Incrementa o contador de semanas
            semanas += 1

    # df = pd.DataFrame(horario)
    # # Cria um buffer em memória para armazenar o arquivo Excel
    # output = BytesIO()
    # # Salva o DataFrame no buffer como um arquivo Excel
    # with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
    #     df.to_excel(writer, index=False)
    # # Move o ponteiro para o início do buffer
    # output.seek(0)
    # return output

    df = pd.DataFrame(horario)

    # Cria um buffer em memória para armazenar o arquivo Excel
    output = BytesIO()

    # Salva o DataFrame no buffer como um arquivo Excel
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False)

    # Move o ponteiro para o início do buffer
    output.seek(0)

    # Codifica o conteúdo do arquivo Excel em base64
    excel_base64 = base64.b64encode(output.read()).decode('utf-8')

    print(f"Excel Base64: {excel_base64[:100]}...")

    # Retorna a string base64 como resposta JSON
    data = {
        'excel_base64': excel_base64,
        'file_name': f"horario_curso_{curso_id}.xlsx"
    }

    return data