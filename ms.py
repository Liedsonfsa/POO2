import mysql.connector

def inserir():
    novo_elemento = (user, email, nome, senha)
    inserir_dados = "INSERT INTO usuario (user, email, nome, senha) VALUES (%s, %s, %s, %s)"

conexao = mysql.connector.connect(
    host='localhost',
    database='mydb',
    user='root',
    password='root'
    
)

user = "usuario1"
email = "email1"
nome = "nome1"
senha = "senha1"

cursor = conexao.cursor()

novo_elemento = (user, email, nome, senha)
inserir_dados = "INSERT INTO usuario (user, email, nome, senha) VALUES (?, ?, ?, ?)", (nome, user, email, senha)
cursor.execute('INSERT INTO usuario (user, email, nome, senha) VALUES (?, ?, ?, ?)', (user, email, nome, senha))
conexao.commit()
    
cursor.close()
conexao.close()