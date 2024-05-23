import sqlite3

conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()


SQL = """ SELECT * FROM alunos;"""
cursor.execute(SQL)
print(cursor.fetchall())
conn.close()