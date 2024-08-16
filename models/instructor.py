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
