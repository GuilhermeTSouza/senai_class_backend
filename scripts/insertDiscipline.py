from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

truncate_table = '''
    TRUNCATE TABLE discipline
'''
cursor.execute(truncate_table)
conn.commit()


discipline = [
    ('BD' , 1, None , 75 ),
    ('Web' , 1, None , 105 ),
    ('Backend' , 1, None , 75 ),
    ('Frontend' , 1, None , 105 ),
    ('COE' , 1, 1 , 105 ),
    ('Disciplina 1' , 2, None , 75 ),
    ('Disciplina 2' , 2, None , 105 ),
    ('Disciplina 3' , 2, None , 75 ),
    ('Disciplina 4' , 2, None , 105 ),
    ('Mat' , 2, 2 , 105 ),

]

insert_discipline = '''
         INSERT INTO discipline (name, course_id, teacher_id, workload ) VALUES (%s,%s,%s,%s)
    '''
cursor.executemany(insert_discipline, discipline)
conn.commit()