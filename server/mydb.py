import mysql.connector

from datetime import datetime

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class Mydb:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='26.212.178.226',
            user='root',
            password="",
            database='mydb'
        )
    
    def cadastrar(self, user, email, nome, senha):
        con = self.conexao
        con.reconnect()
        
        new = (user, email, nome, senha.hexdigest())
        cursor = con.cursor()
        search_user = 'SELECT * FROM usuario WHERE user = %s'
        search_email = 'SELECT * FROM usuario WHERE email = %s'
        new_user = "INSERT INTO usuario (user, email, nome, senha) VALUES (%s, %s, %s, %s)"

        
        cursor.execute(search_email, (email, ))
        e = cursor.fetchone()
        cursor.execute(search_user, (user, ))
        u = cursor.fetchone()
        if u != None or e != None:
            if u != None and e != None:
                return 3
            elif e != None:
                return 1
            else:
                return 2
        else:
            cursor.execute(new_user, new)
            con.commit()
        cursor.close()
        con.close()
        return 0
    
    def checkUser(self, user):
        con = self.conexao
        con.reconnect()

        cursor = con.cursor()

        comando = 'SELECT * FROM usuario WHERE user = %s'
        cursor.execute(comando, (user, ))
        usuario = cursor.fetchone()
        resposta = 1
        if usuario == None:
            resposta = 0
        
        return resposta
    def checkEmail(self, email):
        con = self.conexao
        con.reconnect()

        cursor = con.cursor()

        comando = 'SELECT * FROM usuario WHERE email = %s'
        cursor.execute(comando, (email, ))
        usuario = cursor.fetchone()
        resposta = 1
        if usuario == None:
            resposta = 0
        
        return resposta

    def efetuarLogin(self, user, hash_senha):
        con = self.conexao
        con.reconnect()
        cursor = con.cursor()
        comando = "SELECT * FROM usuario WHERE user = %s"

        cursor.execute(comando, (user, ))
        usuario = cursor.fetchone()
        resposta = int()
        if usuario != None and usuario[3] == hash_senha.hexdigest():
            resposta = 0
        else:
            resposta = 2
        
        con.send(str(resposta).encode())
        con.close()
        cursor.close()

    def realizarPostagem(self, post, usuario):
        con = self.conexao
        con.reconnect()
        cursor = con.cursor()
        comando = 'INSERT INTO postagem (mensagem, data, likes, usuario_user) VALUES ( %s, %s, %s, %s)'
        data = datetime.now()
        info = (post, str(data), 0, usuario)

        cursor.execute(comando, info)

        con.commit()
        con.close()
    
    def addTextUser(self, user):
        con = self.conexao
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
        con = self.conexao
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
        
        return text

