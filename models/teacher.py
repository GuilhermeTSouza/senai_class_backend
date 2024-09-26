from database import get_db_connection
from typing import List


class Teacher:

    def __init__(self, instructor_id, name, email, area):
        self.instructor_id = instructor_id
        self.name = name
        self.email = email
        self.area = area


def get_teacher() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,name, email, area FROM teacher;')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    teacher = []
    for result in results:
        teachers = {
            'id': result[0],
            'name': result[1],
            'email': result[2],
            'area': result[3]
        }

        teacher.append(teachers)

    return teacher

def save_teacher(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_teacher = '''
         INSERT INTO teacher (name, email, area) VALUES (%s,%s,%s)
    '''
    cursor.execute(insert_teacher, (
        data["name"],
        data["email"],
        data["area"]
    ))

    conn.commit()

    cursor.close()
    conn.close()

def delete_teacher(teacher_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    delete_teacher= '''
             DELETE FROM teacher WHERE id = %s
        '''

    cursor.execute(delete_teacher, (teacher_id,))
    conn.commit()
    cursor.close()
    conn.close()

def edit_teacher(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_teacher = '''
         UPDATE teacher SET name=%s, email=%s ,area=%s WHERE id = %s
    '''
    cursor.execute(insert_teacher, (
        data["name"],
        data["email"],
        data["area"],
        data['id']
    ))

    conn.commit()

    cursor.close()
    conn.close()
