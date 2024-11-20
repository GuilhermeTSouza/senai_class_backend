from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

truncate_table = '''
    TRUNCATE TABLE teacher CASCADE
'''
cursor.execute(truncate_table)
conn.commit()


teacher = [
    ('Laís' ,),
    ('Ana Paula',)
]

insert_teacher = '''
         INSERT INTO teacher (name) VALUES (%s)
    '''
cursor.executemany(insert_teacher, teacher)
conn.commit()