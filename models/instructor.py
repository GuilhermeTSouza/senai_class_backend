from database import get_db_connection
from typing import List


class Instructor:

    def __init__(self, instructor_id, name, email, area):
        self.instructor_id = instructor_id
        self.name = name
        self.email = email
        self.area = area


def get_instructor() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,name, email, area FROM instructor;')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    instructor = []
    for result in results:
        instructors = {
            'id': result[0],
            'name': result[1],
            'email': result[2],
            'area': result[3]
        }

        instructor.append(instructors)

    return instructor

def save_instructor(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_instructor = '''
         INSERT INTO instructor (name, email, area) VALUES (%s,%s,%s)
    '''
    cursor.execute(insert_instructor, (
        data["name"],
        data["email"],
        data["area"]
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
         UPDATE instructor SET name=%s, email=%s ,area=%s WHERE id = %s
    '''
    cursor.execute(insert_instructor, (
        data["name"],
        data["email"],
        data["area"],
        data['id']
    ))

    conn.commit()

    cursor.close()
    conn.close()