from scripts.database import get_db_connection
from typing import List


class Instructor:

    def __init__(self, instructor_id, name, area_id):
        self.instructor_id = instructor_id
        self.name = name
        self.area_id = area_id



def get_instructor() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

# 'SELECT c.id , c.name, c.area_id, a.name, c.nb_places '
#                    'FROM classroom AS c '
#                    'INNER JOIN area AS a ON c.area_id = a.id '
#                    'ORDER BY c.name'

    cursor.execute('SELECT i.id, i.name, i.area_id , a.name '
                   'FROM instructor AS i '
                   'INNER JOIN area AS a ON i.area_id = a.id '
                   'ORDER BY i.name')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    instructor = []
    for result in results:
        instructors = {
            'id': result[0],
            'name': result[1],
            'area_id': result[2],
            'area_name': result[3],
        }

        instructor.append(instructors)

    return instructor

def save_instructor(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_instructor = '''
         INSERT INTO instructor (name, area_id) VALUES (%s,%s)
    '''
    cursor.execute(insert_instructor, (
        data["name"],
        data["area_id"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

def delete_instructor(instrutor_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete_instructor= '''
             DELETE FROM instructor WHERE id = %s
        '''

    cursor.execute(delete_instructor, (instrutor_id,))
    conn.commit()
    cursor.close()
    conn.close()

def edit_instructor(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_instructor = '''
         UPDATE instructor SET name=%s, area_id=%s WHERE id = %s
    '''
    cursor.execute(insert_instructor, (
        data["name"],
        data["area_id"],
        data['id']
    ))

    conn.commit()

    cursor.close()
    conn.close()