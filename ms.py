import mysql.connector

def inserir():
    novo_elemento = (user, email, nome, senha)
    inserir_dados = "INSERT INTO usuario (user, email, nome, senha) VALUES (%s, %s, %s, %s)"

conexao = mysql.connector.connect(
    host='26.30.212.204',
    database='mydb',
    user='root',
    password='root'
    
)

user = "usuario1"
email = "email1"
nome = "nome1"
senha = "senha1"

cursor = conexao.cursor()

cursor.execute('SELECT * FROM usuarios')
teste = cursor.fetchall()
print(teste)
conexao.commit()
    
cursor.close()
conexao.close()