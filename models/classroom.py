from scripts.database import get_db_connection
from typing import List


class Classroom:

    def __init__(self, classroom_id, name, area_id, nb_places):
        self.classroom_id = classroom_id
        self.name = name
        self.area_id = area_id
        self.nb_places = nb_places


def get_classroom() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT c.id , c.name, c.area_id, a.name, c.nb_places '
                   'FROM classroom AS c '
                   'INNER JOIN area AS a ON c.area_id = a.id '
                   'ORDER BY c.name')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    classroom = []
    for result in results:
        classrooms = {
            'id': result[0],
            'name': result[1],
            'area_id': result[2],
            'area_name': result[3],
            'nb_places': result[4]
        }

        classroom.append(classrooms)

    return classroom


def save_classroom(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_classroom = '''
         INSERT INTO classroom (name, area_id, nb_places) VALUES (%s,%s,%s)
    '''
    cursor.execute(insert_classroom, (
        data["name"],
        data["area_id"],
        data["nb_places"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

def delete_classroom(sala_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete_classroom = '''
             DELETE FROM classroom WHERE id = %s
        '''

    cursor.execute(delete_classroom, (sala_id,))
    conn.commit()
    cursor.close()
    conn.close()

def edit_classroom(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_classroom = '''
         UPDATE classroom SET name=%s, area_id=%s ,nb_places=%s WHERE id = %s
    '''
    cursor.execute(insert_classroom, (
        data["name"],
        data["area_id"],
        data["nb_places"],
        data['id']
    ))

    conn.commit()

    cursor.close()
    conn.close()


