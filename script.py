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

# create_table_courses = '''
# CREATE TABLE courses(
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(150) NOT NULL
# )
# '''
#
# cursor.execute(create_table_courses)
# conn.commit()

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


classroom=[

]


teacher =[
    ('José Mendes', 'jose.mendes@example.com', 'Engenharia'),
    ('Mariana Teixeira', 'mariana.teixeira@example.com', 'Direito'),
    ('Paulo Gonçalves', 'paulo.goncalves@example.com', 'Medicina'),
    ('Renata Carvalho', 'renata.carvalho@example.com', 'Economia'),
    ('Lucas Fernandes', 'lucas.fernandes@example.com', 'Informática'),
    ('Sofia Ribeiro', 'sofia.ribeiro@example.com', 'Educação Física'),
    ('Tiago Moreira', 'tiago.moreira@example.com', 'Psicologia'),
    ('Vanessa Oliveira', 'vanessa.oliveira@example.com', 'Arquitetura'),
    ('Wagner Santos', 'wagner.santos@example.com', 'Administração')

]

instructor = [
    ('Alice Silva', 'alice.silva@example.com', 'Matemática'),
    ('Bruno Costa', 'bruno.costa@example.com', 'Física'),
    ('Carla Souza', 'carla.souza@example.com', 'Química'),
    ('Daniel Lima', 'daniel.lima@example.com', 'Biologia'),
    ('Elena Rocha', 'elena.rocha@example.com', 'História'),
    ('Fernando Alves', 'fernando.alves@example.com', 'Geografia'),
    ('Giselle Martins', 'giselle.martins@example.com', 'Literatura'),
    ('Henrique Pinto', 'henrique.pinto@example.com', 'Inglês'),
    ('Isabel Duarte', 'isabel.duarte@example.com', 'Artes')
]


course = [
    ('Ciência da Computação',),
    ('Engenharia Civil',),
    ('Medicina',),
    ('Direito',),
    ('Administração de Empresas',),
    ('Psicologia',),
    ('Arquitetura e Urbanismo',),
    ('Biologia',)
]


insert_teacher = '''
    INSERT INTO teacher (name, email, area) VALUES (%s,%s,%s)
'''

insert_instructor = '''
    INSERT INTO instructor (name, email, area) VALUES (%s,%s,%s)
'''

insert_course = '''
    INSERT INTO courses (name) VALUES (%s)
'''
cursor.executemany(insert_teacher, teacher)
cursor.executemany(insert_instructor, instructor)
cursor.executemany(insert_course, course)
conn.commit()

# delete_table = '''
#  DROP TABLE intructor;
# '''
# cursor.execute(delete_table)
# conn.commit()

cursor.close()
conn.close()

