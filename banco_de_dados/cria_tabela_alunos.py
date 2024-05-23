import sqlite3

conn = sqlite3.connect('banco_de_dados.db')
cursor = conn.cursor()

SQL = """
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        sobre_nome TEXT,
        nome_do_pai TEXT,
        nome_da_mae TEXT,
        data_de_nascimento TEXT,
        telefone TEXT,
        cpf TEXT,
        logradouro TEXT,
        rua TEXT,
        bairro TEXT,
        cidade TEXT,
        estado TEXT,
        cep TEXT        
    );
"""

cursor.execute(SQL)
conn.commit()
conn.close()
