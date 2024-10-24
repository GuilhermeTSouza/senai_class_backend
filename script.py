from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

# create_table_teacher = '''
# CREATE TABLE teacher(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     email VARCHAR(150) NOT NULL,
#     area VARCHAR(150) NOT NULL
# )
# '''
#
# cursor.execute(create_table_teacher)
# conn.commit()
#
# create_table_instructor = '''
# CREATE TABLE instructor(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL,
#     email VARCHAR(150) NOT NULL,
#     area VARCHAR(150) NOT NULL
# )
# '''
#
# cursor.execute(create_table_instructor)
# conn.commit()
#
# create_table_courses = '''
# CREATE TABLE courses(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL
# )
# '''
#
# cursor.execute(create_table_courses)
# conn.commit()
#
# create_table_classroom = '''
# CREATE TABLE classroom(
#     id SERIAL PRIMARY KEY,
#     number_classroom INTEGER NOT NULL,
#     capacity INTEGER NOT NULL,
#     computer BOOLEAN NOT NULL
# )
# '''
#
# cursor.execute(create_table_classroom)
# conn.commit()
#
#
# create_table_usuario = '''
# CREATE TABLE users(
#     id SERIAL PRIMARY KEY,
#     username VARCHAR(150) NOT NULL,
#     email VARCHAR(150) NOT NULL,
#     password VARCHAR(150) NOT NULL,
#     theme VARCHAR(150) NOT NULL,
#     user_color VARCHAR(150) NOT NULL
# )
# '''
#
# create_table_disciplina = '''
# CREATE TABLE discipline(
#         id SERIAL PRIMARY KEY,
#         name VARCHAR(145) NOT NULL,
#         worload INT NOT NULL
# )
# '''
# cursor.execute(create_table_disciplina)
# conn.commit()
#
# create_table_curso_disciplina = '''
# CREATE TABLE course_discipline(
#         id SERIAL PRIMARY KEY,
#         course_id INT REFERENCES courses(id) ON DELETE CASCADE,
#         discipline_id INT REFERENCES discipline(id) ON DELETE CASCADE
# )
# '''
# cursor.execute(create_table_curso_disciplina)
# conn.commit()
#
#
# cursor.execute(create_table_usuario)
# conn.commit()





# classroom=[
#
# ]
#
#
# teacher =[
#     ('José Mendes', 'jose.mendes@example.com', 'Engenharia'),
#     ('Mariana Teixeira', 'mariana.teixeira@example.com', 'Direito'),
#     ('Paulo Gonçalves', 'paulo.goncalves@example.com', 'Medicina'),
#     ('Renata Carvalho', 'renata.carvalho@example.com', 'Economia'),
#     ('Lucas Fernandes', 'lucas.fernandes@example.com', 'Informática'),
#     ('Sofia Ribeiro', 'sofia.ribeiro@example.com', 'Educação Física'),
#     ('Tiago Moreira', 'tiago.moreira@example.com', 'Psicologia'),
#     ('Vanessa Oliveira', 'vanessa.oliveira@example.com', 'Arquitetura'),
#     ('Wagner Santos', 'wagner.santos@example.com', 'Administração')
#
# ]
#
#
#
# instructor = [
#     ('Alice Silva', 'alice.silva@example.com', 'Matemática'),
#     ('Bruno Costa', 'bruno.costa@example.com', 'Física'),
#     ('Carla Souza', 'carla.souza@example.com', 'Química'),
#     ('Daniel Lima', 'daniel.lima@example.com', 'Biologia'),
#     ('Elena Rocha', 'elena.rocha@example.com', 'História'),
#     ('Fernando Alves', 'fernando.alves@example.com', 'Geografia'),
#     ('Giselle Martins', 'giselle.martins@example.com', 'Literatura'),
#     ('Henrique Pinto', 'henrique.pinto@example.com', 'Inglês'),
#     ('Isabel Duarte', 'isabel.duarte@example.com', 'Artes')
# ]
#
#
#
# course = [
#     ('Ciência da Computação',),
#     ('Engenharia Civil',),
#     ('Medicina',),
#     ('Direito',),
#     ('Administração de Empresas',),
#     ('Psicologia',),
#     ('Arquitetura e Urbanismo',),
#     ('Biologia',)
# ]
#
# users = [
#     ('Admin' , 'Admin@gmail.com' , '1234' , 'dark' , '#28c241')
# ]




# insert_teacher = '''
#     INSERT INTO teacher (name, email, area) VALUES (%s,%s,%s)
# '''
# cursor.executemany(insert_teacher, teacher)
# conn.commit()

# insert_instructor = '''
#     INSERT INTO instructor (name, email, area) VALUES (%s,%s,%s)
# '''
# cursor.executemany(insert_instructor, instructor)
# conn.commit()
# #
# insert_course = '''
#     INSERT INTO courses (name) VALUES (%s)
# '''
# cursor.executemany(insert_course, course)
# conn.commit()
#
#
#
#
#
# insert_users = '''
#     INSERT INTO users (username , email ,password , theme , user_color) VALUES (%s,%s,%s,%s,%s)
# '''
# cursor.executemany(insert_users , users)
# conn.commit()

# delete_table = '''
#  DROP TABLE user;
# '''
# cursor.execute(delete_table)
# conn.commit()

cursor.close()
conn.close()

