from database import get_db_connection
from typing import List


class Course:

    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


def get_courses() -> List[Course]:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,name FROM course;')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    courses = []
    for result in results:
        course = Course(
            course_id=result[0],
            name=result[1]
        )
        courses.append(course)

    return courses
