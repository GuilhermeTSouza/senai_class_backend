from scripts.database import get_db_connection
from typing import List


class Course:

    def __init__(self, course_id, name, area_id ,monday, tuesday, wednesday, thursday, friday):
        self.course_id = course_id
        self.name = name
        self.area_id = area_id
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday


def get_courses() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,name, area_id FROM course ORDER BY name')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    courses = []
    for result in results:
        course = {
            'id': result[0],
            'name': result[1],
            'area_id': result[2]
        }

        courses.append(course)

    return courses

def save_courses(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_courses = '''
         INSERT INTO course (name, area_id ) VALUES (%s,%s)
    '''
    cursor.execute(insert_courses, (
        data["name"],
        data["area_id"],
    ))

    conn.commit()

    cursor.close()
    conn.close()

def delete_courses(curso_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete_courses= '''
             DELETE FROM course WHERE id = %s
        '''

    cursor.execute(delete_courses, (curso_id,))
    conn.commit()
    cursor.close()
    conn.close()

def edit_courses(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_courses = '''
         UPDATE course SET name = %s, area_id = %s WHERE id = %s
    '''
    cursor.execute(insert_courses, (
        data["name"],
        data["area_id"],
        data['id']
    ))

    conn.commit()

    cursor.close()
    conn.close()