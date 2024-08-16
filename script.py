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
teacher =[

    ('Lais', 'lais@sp.senai.br', 'COE',)

]


insert_teacher = '''
    INSERT INTO teacher (name , email , area) VALUES (%s,%s,%s)
'''
cursor.executemany(insert_teacher, teacher)
conn.commit()

# delete_table = '''
#  DROP TABLE intructor;
# '''
# cursor.execute(delete_table)
# conn.commit()

cursor.close()
conn.close()

