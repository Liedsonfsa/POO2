import mysql.connector

from datetime import datetime

class Mydb:
    """
    A classe representa o banco de dados onde vão ser ralizadas as consultas.

    Attributes:
            self.conexao : a conexão do banco de dados
    Methods:
            getConexao() : retorna a conexão do banco de dados.
            cadastrar(user, email, nome, senha) : recebe as informações para efetuar o cadastro de um usuário.
            checkUser(user) : checa se o user name informado já está cadastrado.
            checkEmail(email) : checa se o email informado já está cadastrado.

    """
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='mydb'
        )

    
    def getConexao(self):
        """
        Retorna a conexão do banco de dados.
                Parameters:
                        None
                Returns:
                        
                        PooledMySQLConnection | MySQLConnection: conexão do banco de dados.
        """
        return self.conexao
    
    def cadastrar(self, user: str, email: str, nome: str, senha: str):
        """
        Este módulo recebe as informações necessárias para o cadastro, e faz uma pesquisa no banco de dados pelo user e o email
        informados, caso já sejam cadastrados o novo usuário não sera inserido.
                Parameters: 
                        user (str): user do usuário
                        email (str): email do usuário
                        nome (str): nome do usuário
                        senha (str): hash da senha do usuário
                Return:
                        str: 0 se as informações ainda não estão registradas, 1 se o email já está cadastrato,
                        2 se o user já está cadastrado e 3 se as duas informações já estão cadastradas na base de dados.

        """
        con = self.getConexao()
        con.reconnect()
        
        new = (user, email, nome, senha)
        cursor = con.cursor()
        search_user = 'SELECT * FROM usuario WHERE user = %s'
        search_email = 'SELECT * FROM usuario WHERE email = %s'
        new_user = "INSERT INTO usuario (user, email, nome, senha) VALUES (%s, %s, %s, %s)"

        
        cursor.execute(search_email, (email, ))
        e = cursor.fetchone()
        cursor.execute(search_user, (user, ))
        u = cursor.fetchone()
        print(f'u: {u}, e: {e}')
        resposta = 0
        if u != None or e != None:
            if u != None and e != None:
                resposta = 3
            elif e != None:
                resposta = 1
            else:
                resposta = 2
        else:
            cursor.execute(new_user, new)
            con.commit()
        cursor.close()
        con.close()
        return str(resposta)
    
    def checkUser(self, user: str):
        """
        Este módulo faz uma pesquisa pelo user do usuário no banco de dados.
                Parameters: 
                        user (str): nome do usuário.
                Return: 
                        str: 0 se o user não existir, e 1 se ele já estiver cadastrado.
        """
        con = self.getConexao()
        con.reconnect()

        cursor = con.cursor()

        comando = 'SELECT * FROM usuario WHERE user = %s'
        cursor.execute(comando, (user, ))
        usuario = cursor.fetchone()
        resposta = 1
        if usuario == None:
            resposta = 0
        
        return str(resposta)
    
    def checkEmail(self, email: str) -> str:
        """
        Este módulo faz uma pesquisa pelo email do usuário no banco de dados
                Parameters: 
                        email (str): email do usuário
                Return: 
                        str: 0 se o email não existir, e 1 se ele já estiver cadastrado
        """
        con = self.getConexao()
        con.reconnect()

        cursor = con.cursor()

        comando = 'SELECT * FROM usuario WHERE email = %s'
        cursor.execute(comando, (email, ))
        usuario = cursor.fetchone()
        resposta = 1
        if usuario == None:
            resposta = 0
        
        return str(resposta)

    def efetuarLogin(self, user: str, hash_senha: str):
        """
        Este módulo recebe o user e o hash da senha do usuário, e efetua uma busca pelo usuário no banco de dsdos,
        caso o user e o hash sejam os mesmos dos encontrados no banco de dados, o acesso é permitido.
                Parameters:
                        user (str): nome do usuário
                        hash_senha (str): hash da senha do usuário
                Return:
                        str: 2 se o login ou senha estiverem errados, e 0 se estiverem corretos.

        """
        con = self.getConexao()
        con.reconnect()
        cursor = con.cursor()
        comando = "SELECT * FROM usuario WHERE user = %s"
        print(f'user: {user}, hash: {hash_senha}')
        cursor.execute(comando, (user, ))
        usuario = cursor.fetchone()
        print(usuario)
        resposta = 2
        if usuario != None and usuario[3] == hash_senha:
            resposta = 0
        
        con.close()
        cursor.close()
        return str(resposta)

    def realizarPostagem(self, post: str, usuario: str):
        """
        Este módulo recebe o conteúdo da postagem e o nome do usuário e os insere no banco de dados
                Parameters:
                        post (str): conteúdo da postagem
                        usuario (str): nome fo usuário
                Return:
                        None
        """
        con = self.getConexao()
        con.reconnect()
        cursor = con.cursor()
        comando = 'INSERT INTO postagem (mensagem, data, likes, usuario_user) VALUES ( %s, %s, %s, %s)'
        data = datetime.now()
        info = (post, str(data), 0, usuario)

        cursor.execute(comando, info)
        
        con.commit()
        con.close()
        
    
    def addTextUser(self, user: str) -> str:
        """
        Este módulo recebe o nome do usuário e seleciona todas as mensagens desse usuário no banco de dados,
        e as adiciona na tela de perfil do usuário.
                Parameters:
                        user (str): nome do usuário
                Return:
                        text (str): todas as mensagens do usuário
        """
        print('addTextUser')
        con = self.getConexao()
        con.reconnect()
        cursor = con.cursor()

        comando = 'SELECT * FROM postagem WHERE usuario_user = %s'
        cursor.execute(comando, (user, ))
        posts = cursor.fetchall()
        
        text = ''
        if(posts == list):
            print()
        else:
            for post in posts:
                text = f'\n{post[2]}             {post[1]}\n{post[3]}\n' + text
        
        con.commit()
        con.close()

        return text

    def addText(self) -> str:
        """
        Este módulo adiciona todas as mensagens do banco de dados na timeline dos usuários.
                Parameters:
                        None
                Returns:
                        str : as mensagens
        """
        print('addText')
        con = self.getConexao()
        con.reconnect()
        cursor = con.cursor()
        
        comando = 'SELECT * FROM postagem'
        cursor.execute(comando)
        posts = cursor.fetchall()
        
        text = ''
        if(posts == list):
            print()
        else:
            for post in posts:
                text = f'\n{post[2]}             {post[1]}\n{post[3]}\n' + text
        
        con.commit()
        con.close()
        print(text)
        
        return text
