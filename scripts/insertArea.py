from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

truncate_table = '''
    TRUNCATE TABLE area CASCADE
'''
cursor.execute(truncate_table)
conn.commit()


areas = [
    ('Tecnologia da Informação' ,),
    ('Elétrica',),
    ('Modelação',),
    ('Montagem de Veículos',),
    ('Solda',),
    ('Marcenaria',),
    ('Mecânica de Veículos',),
    ('Móveis',),
    ('Adiministração',),
    ('Calderaria',)
]

insert_area = '''
    INSERT INTO area (name) VALUES (%s)
'''


cursor.executemany(insert_area, areas)
conn.commit()