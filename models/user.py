from database import get_db_connection
from typing import List


class Classroom:

    def __init__(self, user_id, username, email, password , theme , user_color):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.theme = theme
        self.user_color = user_color


def get_users() -> List:
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT id,username, email, password, theme ,user_color FROM users;')

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    user = []
    for result in results:
        users = {
            'id': result[0],
            'username': result[1],
            'email': result[2],
            'password': result[3],
            'theme': result[4],
            'user_color': result[5]
        }

        user.append(users)

    return user
