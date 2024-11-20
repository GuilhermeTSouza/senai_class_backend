from scripts.database import get_db_connection
from typing import List


class Teacher:

    def __init__(self, instructor_id, name, area_id):
        self.instructor_id = instructor_id
        self.name = name
        self.area_id = area_id



def get_teacher() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id ,name FROM teacher;')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    teacher = []
    for result in results:
        teachers = {
            'id': result[0],
            'name': result[1],
        }

        teacher.append(teachers)

    return teacher

def save_teacher(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_teacher = '''
         INSERT INTO teacher (name, area_id) VALUES (%s,%s)
    '''
    cursor.execute(insert_teacher, (
        data["name"],
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
         UPDATE teacher SET name=%s WHERE id = %s
    '''
    cursor.execute(insert_teacher, (
        data["name"],
        data['id']
    ))

    conn.commit()

    cursor.close()
    conn.close()
