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

    cursor.execute('SELECT id,number_classroom, capacity, computer FROM classroom;')

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
