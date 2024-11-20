from scripts.database import get_db_connection
from typing import List


class Area:
    def __init__(self, area_id, name):
        self.area_id = area_id
        self.name = name

def get_area() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,name FROM area ORDER BY name')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    area = []
    for result in results:
        areas = {
            'id': result[0],
            'name': result[1]
        }

        area.append(areas)

    return area
