import sqlite3

conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()

SQL = """
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY, 
        nome text NOT NULL        
    );
"""
cursor.execute(SQL)
conn.commit()
conn.close()
