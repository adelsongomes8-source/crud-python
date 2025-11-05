from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Criação da aplicação Flask
app = Flask(__name__)

# Configuração da conexão com o banco de dados MySQL
db = mysql.connector.connect(
    host="",
    user="",
    password="",
    database=""
)

# Criar cursor para executar queries
cursor = db.cursor()

# 1) ROTA INICIAL
@app.route('/')
def index():
    return render_template('index.html')

# 2) ROTA PARA O FORMULÁRIO
# DE CRIAÇÃO DO LIVRO
@app.route('/criar')
def pagina_criar():
    return render_template('criar.html')

# 3) ROTA PARA CRIAÇÃO DO
# LIVRO NO BANCO DE DADOS
@app.route('/criar/novo', methods=['POST'])
def criar_livro():
    titulo = request.form['titulo']
    ano_publicacao = request.form['ano_publicacao']
    editora = request.form['editora']
    isbn = request.form['isbn']
    
    query = "INSERT INTO livro (titulo, ano_publicacao, editora, isbn) VALUES (%s, %s, %s, %s)"
    values = (titulo, ano_publicacao, editora, isbn)
    
    cursor.execute("DELETE FROM livro WHERE id = %s , (id))
    db.commit()
    
    return redirect('/listar')

# INICIALIZAÇÃO DO SERVIDOR
if __name__ == '__main__':
    app.run(debug=True)
