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
create_table_courses = '''
CREATE TABLE courses(
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    segunda BOOLEAN NOT NULL DEFAULT false,
    terca BOOLEAN NOT NULL DEFAULT false,
    quarta BOOLEAN NOT NULL DEFAULT false,
    quinta BOOLEAN NOT NULL DEFAULT false,
    sexta BOOLEAN NOT NULL DEFAULT false,
    quant_semestre INTEGER NOT NULL
)
'''

cursor.execute(create_table_courses)
conn.commit()
#
# create_table_classroom = '''
# CREATE TABLE classroom(
#     id SERIAL PRIMARY KEY,
#     classroom_name VARCHAR(150) NOT NULL,
#     capacity INTEGER NOT NULL,
#     function VARCHAR(150) NOT NULL
# )
# '''
#
# cursor.execute(create_table_classroom)
# conn.commit()

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
# cursor.execute(create_table_usuario)
# conn.commit()


create_table_disciplina = '''
CREATE TABLE discipline(
        id SERIAL PRIMARY KEY,
        name VARCHAR(145) NOT NULL,
        worload INT NOT NULL,
        classroom_id INT REFERENCES classroom(id) ON DELETE CASCADE
)
'''
cursor.execute(create_table_disciplina)
conn.commit()
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

classroom=[
    ('Sala de Aula 3', 34 , 'TI'),
    ('Sala de Aula 2', 34 , 'Aulas'),
    ('Sala de Aula 1', 34 , 'Aulas')


]
#
teacher =[
    ('Ana Paula Valério Côa', 'ana.coa@sp.senai.br', 'Matemática'),
    ('Lais Baptista Marim','lais.marin@sp.senai.br','COE')
]
#
instructor = [
    ('Clayton Stênico','clayton.stenico@sp.senai.br','Elétrica'),
    ('Diego Poly Romano','diego.romano@sp.senai.br','Elétrica'),
    ('Esdras Abrimael de Oliveira', 'esdras.oliveira@sp.senai.br', 'Marcenaria e Modelação'),
    ('Fabiano Antonio Braga','fabiano.braga@sp.senai.br','Mecanica'),
    ('José Francisco Bis','jose.bis@sp.senai.br','Marcenaria e Modelação'),
    ('Jorge Luiz dos Santos','jorge.santos@sp.senai.br','Elétrica'),
    ('Marcilio Gonçalves Vieira','marcilio.vieira@sp.senai.br','Mineração'),
    ('Márcio Fabrício','marcio.fabricio@sp.senai.br','Mecânica'),
    ('Matheus Lourenço Dias','matheus.dias@sp.senai.br','Solda e Calderaria'),
    ('Matheus da silva Pereira','matheus.pereira@sp.senai.br','Solda e Calderaria'),
    ('Michael Cesar Ferraz','michael.ferraz@sp.senai.br','Solda e calderaria'),
    ('Paulo Sérgio Peres','paulo.peres@sp.senai.br','Solda e calderaria'),
    ('Sidnei Vechi Telles','sidnei.telles@sp.senai.br','Mecânica'),
    ('Andre Luis Thomazini','andre.thomazini@sp.senai.br','Elétrica'),
    ('Carlos Gil Cardoso do Nascimento','carlos.nascimento@sp.senai.br','ADM'),
    ('Janderson Demori','janderson.demori@sp.senai.br','Elétrica'),
    ('Rafael Lopes Vieira','rafael.viera@sp.senai.br','Elétrica'),
    ('Maristela de Morais','maristela.morais@sp.senai.br','ADM'),
    ('Mike Bavaroti de Lima','mike.lima@sp.senai.br','ADM'),
    ('Moises Francisco Olimpio Filho','moises.filho@sp.senai.br','TI')
]

course = [
    ('Modelador',),
    ('Montador de Veículos Automotores',),
    ('Soldador',),
    ('Montador de Veículos Automotores 2',),
    ('Marceneiro',),
    ('Caldereiro',),
    ('Eletricista de Manutenção',),
    ('Modelador 2',),
    ('Eletricista de Manutenção 2',),
    ('Mecânica Automóveis Leves',),
    ('Soldador 2',),
    ('Prod. Ind. de Móveis',),
    ('Soldador 3',),
    ('Op. Proc. Siderurgícos',),
    ('Montador de Veículos Automotores 3',),
    ('Caldereiro 2',),
    ('Técnico em Administração',),
    ('Técnico em Administração 2',),
    ('Técnico em Administração 3',),
    ('Técnico em Administração 4',),
    ('Técnico Eletroeletrônica',),
    ('Técnico Eletroeletrônica Sesi',),
    ('Técnico Eletroeletrônica Sesi 2',),
    ('Técnico Desenvolvimento de Sistemas Sesi',),
    ('Técnico Desenvolvimento de Sistemas Sesi 2',)
]
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
# insert_users = '''
#     INSERT INTO users (username , email ,password , theme , user_color) VALUES (%s,%s,%s,%s,%s)
# '''
# cursor.executemany(insert_users , users)
# conn.commit()
#





# delete_table = '''
#  DROP TABLE courses, discipline CASCADE;
# '''
# cursor.execute(delete_table)
# conn.commit()
#
# cursor.close()
# conn.close()

