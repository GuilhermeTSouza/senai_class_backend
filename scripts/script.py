from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

# create_table_area = '''
# CREATE TABLE area (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL
# )
# '''
# cursor.execute(create_table_area)
# conn.commit()
#
# create_table_instructor = '''
# CREATE TABLE instructor (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     area_id INT REFERENCES area(id) ON DELETE CASCADE
# )
# '''
# cursor.execute(create_table_instructor)
# conn.commit()
#
create_table_teacher = '''
CREATE TABLE teacher (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL
)
'''
cursor.execute(create_table_teacher)
conn.commit()
#
# create_table_course = '''
# CREATE TABLE course (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     area_id INT REFERENCES area(id) ON DELETE CASCADE,
#     monday BOOLEAN NOT NULL DEFAULT false,
#     tuesday BOOLEAN NOT NULL DEFAULT false,
#     wednesday BOOLEAN NOT NULL DEFAULT false,
#     thursday BOOLEAN NOT NULL DEFAULT false,
#     friday BOOLEAN NOT NULL DEFAULT false
# )
# '''
# cursor.execute(create_table_course)
# conn.commit()
#
# create_table_classroom = '''
# CREATE TABLE classroom (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     area_id INT REFERENCES area(id) ON DELETE CASCADE,
#     nb_places INT NOT NULL
# )
# '''
# cursor.execute(create_table_classroom)
# conn.commit()
#
# create_table_discipline = '''
# CREATE TABLE discipline (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     course_id INT REFERENCES course(id) ON DELETE CASCADE,
#     teacher_id INT REFERENCES teacher(id) ON DELETE CASCADE,
#     workload INT NOT NULL
# )
# '''
# cursor.execute(create_table_discipline)
# conn.commit()




# delete_table = '''
#  DROP TABLE teacher CASCADE;
# '''
# cursor.execute(delete_table)
# conn.commit()
# cursor.close()
# conn.close()

cursor.close()
conn.close()

