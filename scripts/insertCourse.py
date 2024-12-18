from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

truncate_table = '''
    TRUNCATE TABLE course CASCADE
'''
cursor.execute(truncate_table)
conn.commit()


classroom = [
    ('Técnico Desenvolvimento de Sistemas 1' , 1, False, False,False,True,True ),
    ('Técnico Desenvolvimento de Sistemas 2', 1, False, True, True, False, False),
    ('Técnico Eletroeltrônica 1' , 2, False, False,False,True,True ),
    ('Técnico Eletroeltrônica 2', 2, False, True, True, False, False),
]

insert_courses = '''
         INSERT INTO course (name, area_id ,monday, tuesday, wednesday, thursday, friday) VALUES (%s,%s,%s,%s,%s,%s,%s)
    '''
cursor.executemany(insert_courses, classroom)
conn.commit()