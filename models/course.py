from database import get_db_connection
from typing import List


class Course:

    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


def get_courses() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,name FROM courses ORDER BY name')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    courses = []
    for result in results:
        course = {
            'id': result[0],
            'name': result[1]
        }

        courses.append(course)

    return courses

def save_courses(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_courses = '''
         INSERT INTO courses (name) VALUES (%s)
    '''
    cursor.execute(insert_courses, (
        data["name"],
    ))

    conn.commit()

    cursor.close()
    conn.close()

def delete_courses(curso_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete_courses= '''
             DELETE FROM classroom WHERE id = %s
        '''

    cursor.execute(delete_courses, (curso_id,))
    conn.commit()
    cursor.close()
    conn.close()

def edit_courses(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_courses = '''
         UPDATE classroom SET name = %s WHERE id = %s
    '''
    cursor.execute(insert_courses, (
        data["name"],
        data['id']
    ))

    conn.commit()

    cursor.close()
    conn.close()