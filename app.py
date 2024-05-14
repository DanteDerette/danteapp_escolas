from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/salvar_aluno", methods=['POST'])
def salvar_aluno():
    dict = request.get_json()
    nome = dict['nome']
    
    conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    cursor = conn.cursor()
    SQL = """ INSERT INTO alunos(nome) VALUES(?);"""
    
    cursor.execute(SQL, (nome,))
    conn.commit()
    conn.close()
    return jsonify(retorno="Sucesso")
  
@app.route("/ler_todos_alunos", methods=['POST'])
def ler_todos_alunos():
    conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    cursor = conn.cursor()
    SQL = """ SELECT * FROM alunos;"""
    
    cursor.execute(SQL)
    dados = cursor.fetchall()
    
    conn.close()
    return jsonify(dados=dados)

app.run(debug=True)