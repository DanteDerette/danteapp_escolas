from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/salvar_aluno", methods=['POST'])
def salvar_aluno():
    dict = request.get_json()
            
    conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    cursor = conn.cursor()
    
    ## Quando é Alterar tem ID
    ## Quando é Inserir não ID
    if dict['id'] == '':        
        SQL = """ INSERT INTO
            alunos (
                nome,
                sobre_nome,
                nome_do_pai,
                nome_da_mae,
                data_de_nascimento,
                telefone,
                cpf,
                logradouro,
                rua,
                bairro,
                cidade,
                estado,
                cep            
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);"""
        
        cursor.execute(SQL,
            (
                dict['nome'],
                dict['sobre_nome'],
                dict['nome_do_pai'],
                dict['nome_da_mae'],
                dict['data_de_nascimento'],
                dict['telefone'],
                dict['cpf'],
                dict['logradouro'],
                dict['rua'],
                dict['bairro'],
                dict['cidade'],
                dict['estado'],
                dict['cep'],
            )
        )
    else:
        SQL = """ UPDATE alunos 
                SET
                    nome = ?,
                    sobre_nome = ?,
                    nome_do_pai = ?,
                    nome_da_mae = ?,
                    data_de_nascimento = ?,
                    telefone = ?,
                    cpf = ?,
                    logradouro = ?,
                    rua = ?,
                    bairro = ?,
                    cidade = ?,
                    estado = ?,
                    cep = ?         
                WHERE id = ?;"""
        cursor.execute(SQL,
            (
                dict['nome'],
                dict['sobre_nome'],
                dict['nome_do_pai'],
                dict['nome_da_mae'],
                dict['data_de_nascimento'],
                dict['telefone'],
                dict['cpf'],
                dict['logradouro'],
                dict['rua'],
                dict['bairro'],
                dict['cidade'],
                dict['estado'],
                dict['cep'],
                dict['id'],
            )
        )
        
    
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
    print(dados)
    
    conn.close()
    return jsonify(dados=dados)

@app.route("/exclui_aluno", methods=['POST'])
def exclui_aluno():
    dict = request.get_json()
    conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    cursor = conn.cursor()
    SQL = """ DELETE FROM alunos WHERE id=""" + str(dict['id']) + """;"""
    cursor.execute(SQL)
    conn.commit()
    
    conn.close()
    return jsonify(x=0)

@app.route("/ler_aluno_especifico", methods=['POST'])
def ler_aluno_especifico():
    dict = request.get_json()
    conn = sqlite3.connect('banco_de_dados/banco_de_dados.db')
    cursor = conn.cursor()
    SQL = """ SELECT * FROM alunos WHERE id=""" + str(dict['id']) + """;"""
    cursor.execute(SQL)
    dados = cursor.fetchall()
    
    SQL = """ PRAGMA table_info(alunos);"""
    cursor.execute(SQL)
    cabecalho = cursor.fetchall()
    
        
    conn.close()
    return jsonify(
        dados=dados,
        cabecalho=cabecalho
    )



app.run(debug=True, host='0.0.0.0')