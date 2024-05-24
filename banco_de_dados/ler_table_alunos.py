import sqlite3

conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()


SQL = """ SELECT * FROM alunos;"""
cursor.execute(SQL)
print(cursor.fetchall())
conn.close()

[
    (1, 'Dante', 'Derette', '', '', '', '', '', '', '', '', '', '', ''),
    (2, 'Dante', 'Derette', '', '', '', '', '', '', '', '', '', '', ''),
    (3, 'Dante', 'Derette', '', '', '', '', '', '', '', '', '', '', ''),
    (4, 'Dante', 'Derette', '', '', '', '', '', '', '', '', '', '', ''),
    (5, 'Dante', 'Derette', '', '', '', '', '', '', '', '', '', '', ''),
    (6, 'Alexandre', 'da Silva', '', '', '', '', '', '', '', '', '', '', '')
    ]

