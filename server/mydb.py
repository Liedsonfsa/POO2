import mysql.connector

from datetime import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

class Mydb:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='mydb'
        )

    
    def getConexao(self):
        return self.conexao
    
    def cadastrar(self, user, email, nome, senha):
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
    
    def checkUser(self, user):
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
    def checkEmail(self, email):
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

    def efetuarLogin(self, user, hash_senha):
        con = self.getConexao()
        con.reconnect()
        cursor = con.cursor()
        comando = "SELECT * FROM usuario WHERE user = %s"
        print(f'user: {user}, hash: {hash_senha}')
        cursor.execute(comando, (user, ))
        usuario = cursor.fetchone()
        print(usuario)
        resposta = int()
        if usuario != None and usuario[3] == hash_senha:
            resposta = 0
        else:
            resposta = 2
        
       
        con.close()
        cursor.close()
        return str(resposta)

    def realizarPostagem(self, post, usuario):
        con = self.getConexao()
        con.reconnect()
        cursor = con.cursor()
        comando = 'INSERT INTO postagem (mensagem, data, likes, usuario_user) VALUES ( %s, %s, %s, %s)'
        data = datetime.now()
        info = (post, str(data), 0, usuario)

        cursor.execute(comando, info)

        con.commit()
        con.close()
        
    
    def addTextUser(self, user):
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

    def addText(self):
        con = self.getConexao()
        con.reconnect()
        cursor = con.cursor()

        text = ''
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
        
        tela.textBrowser.setText(text)
        
        return text

