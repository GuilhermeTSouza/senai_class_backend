from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

truncate_table = '''
    TRUNCATE TABLE instructor CASCADE
'''
cursor.execute(truncate_table)
conn.commit()


instructor = [
    ('Moises' , 1),
    ('Rodolfo' , 1),
    ('Alberto' , 1)
]

insert_instructor = '''
         INSERT INTO instructor (name, area_id) VALUES (%s,%s)
    '''
cursor.executemany(insert_instructor, instructor)
conn.commit()