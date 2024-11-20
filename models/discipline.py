from scripts.database import get_db_connection
from typing import List


class Discipline:

    def __init__(self, discipline_id, name, course_id, teacher_id,workload):
        self.discipline_id = discipline_id
        self.name = name
        self.course_id = course_id
        self.teacher_id = teacher_id
        self.workload = workload

def get_discipline() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,name, course_id, teacher_id, workload FROM discipline;')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    discipline = []
    for result in results:
        disciplines = {
            'id': result[0],
            'name': result[1],
            'course_id': result[2],
            'teacher_id': result[3],
            'workload': result[4]
        }

        discipline.append(disciplines)

    return discipline

def save_discipline(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_discipline = '''
         INSERT INTO discipline (name, course_id, teacher_id, workload ) VALUES (%s,%s,%s,%s)
    '''
    cursor.execute(insert_discipline, (
        data["name"],
        data["course_id"],
        data["teacher_id"],
        data["workload"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

def delete_discipline(discipline_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete_discipline= '''
             DELETE FROM discipline WHERE id = %s
        '''

    cursor.execute(delete_discipline, (discipline_id,))
    conn.commit()
    cursor.close()
    conn.close()

def edit_discipline(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_discipline = '''
         UPDATE discipline SET name = %s, course_id = %s, teacher_id = %s, worload = %s WHERE id = %s
    '''
    cursor.execute(insert_discipline, (
        data["name"],
        data["course_id"],
        data["teacher_id"],
        data["worload"]
    ))

    conn.commit()

    cursor.close()
    conn.close()