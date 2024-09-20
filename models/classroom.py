from database import get_db_connection
from typing import List


class Classroom:

    def __init__(self, classroom_id, number_classroom, capacity, computer):
        self.classroom_id = classroom_id
        self.number_classroom = number_classroom
        self.capacity = capacity
        self.computer = computer


def get_classroom() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,number_classroom, capacity, computer FROM classroom ORDER BY number_classroom')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    classroom = []
    for result in results:
        classrooms = {
            'id': result[0],
            'number_classroom': result[1],
            'capacity': result[2],
            'computer': result[3]
        }

        classroom.append(classrooms)

    return classroom


def save_classroom(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    insert_classroom = '''
         INSERT INTO classroom (number_classroom, capacity, computer) VALUES (%s,%s,%s)
    '''
    cursor.execute(insert_classroom, (
        data["number_classroom"],
        data["capacity"],
        data["computer"]
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
         UPDATE classroom SET number_classroom=%s, capacity=%s ,computer=%s WHERE id = %s
    '''
    cursor.execute(insert_classroom, (
        data["number_classroom"],
        data["capacity"],
        data["computer"],
        data['id']
    ))

    conn.commit()

    cursor.close()
    conn.close()


