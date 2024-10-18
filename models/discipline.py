from database import get_db_connection
from typing import List


class Discipline:

    def __init__(self, discipline_id, name, workload):
        self.discipline_id = discipline_id
        self.name = name
        self.workload = workload

def get_discipline() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,name, workload, area FROM discipline;')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    discipline = []
    for result in results:
        disciplines = {
            'id': result[0],
            'name': result[1],
            'workload': result[2],
        }

        discipline.append(disciplines)

    return discipline

def save_discipline(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_discipline = '''
         INSERT INTO discipline (name, workload) VALUES (%s,%s)
    '''
    cursor.execute(insert_discipline, (
        data["name"],
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
         UPDATE discipline SET name=%s, workload=%s WHERE id = %s
    '''
    cursor.execute(insert_discipline, (
        data["name"],
        data["workload"]
    ))

    conn.commit()

    cursor.close()
    conn.close()