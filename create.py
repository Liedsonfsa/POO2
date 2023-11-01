import mysql.connector

def novo_user(user, email, nome, senha):
    conexao = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="root",
      database="mydb"
    )
    cursor = conexao.cursor()
    novo_elemento = (user, email, nome, senha)
    inserir_dados = "INSERT INTO usuario (user, email, nome, senha) VALUES (%s, %s, %s, %s)"
    cursor.execute(inserir_dados, novo_elemento)
    conexao.commit()


    cursor.close()
    conexao.close()

def buscar_usuario(user):
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="mydb"
    )
    cursor = conexao.cursor()

    comando = "SELECT * FROM usuario WHERE user = %s"
    comando2 = "SELECT * FROM usuario"
    # cursor.execute(comando, (user,))
    cursor.execute(comando2)
    resultados = cursor.fetchall()
    if resultados == []:
      print('Não encontrado...')
    else:
      #print(resultados)
      for i in resultados:
        print(i[0])
        print(i[1])

    cursor.close()
    conexao.close()

# novo_user('lucas', 'lucas@gmail.com', 'lucas', '1234')
buscar_usuario('lucas')