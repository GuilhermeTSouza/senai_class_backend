from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

truncate_table = '''
    TRUNCATE TABLE classroom CASCADE
'''
cursor.execute(truncate_table)
conn.commit()


classroom = [
    ('Sala 03' , 3, 34 ),
    ('Laboratório CLP', 4 , 16),
    ('Laboratório Eletrônica Digital', 4 , 16),

]

insert_classroom = '''
    INSERT INTO classroom (name , area_id , nb_places) VALUES (%s, %s, %s)
'''


cursor.executemany(insert_classroom, classroom)
conn.commit()