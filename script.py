from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

# create_table_course = '''
# CREATE TABLE courses(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR (150) NOT NULL
# )
# '''
#
# cursor.execute(create_table_course)
# conn.commit()
courses =[
    ("Técnico em Desenvolvimento",),
    ("Técnico em ADM",)
]


insert_course = '''
    INSERT INTO courses (name) VALUES (%s)
'''
cursor.executemany(insert_course, courses)

conn.commit()

cursor.close()
conn.close()

