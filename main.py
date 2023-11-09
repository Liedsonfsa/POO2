import sys
from datetime import datetime

from hashlib import sha256

from conexao import Conexao

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from collections import deque

from tela_cadastro import Tela_Cadastro
from tela_inicial import Tela_Inicial
from sistema import Sistema
from usuario import Usuario
from mensagens import Mensagens
from tela_principal import Tela_Principal
from tela_perfil import Tela_Perfil
from tela_conversas import Tela_Conversas
from timeline import Timeline

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_principal = Tela_Principal()
        self.tela_principal.setupUi(self.stack3)

        self.tela_perfil = Tela_Perfil()
        self.tela_perfil.setupUi(self.stack4)

        self.tela_conversas = Tela_Conversas()
        self.tela_conversas.setupUi(self.stack5)

        self.conexao = Conexao()

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)


        self.cad = Sistema()
        self.tela_inicial.botao_ir_cadastro.clicked.connect(self.abrirTelaCadastro) # funções dos botões da tela principal
        self.timeline = Timeline()

        self.tela_inicial.botao_logar.clicked.connect(self.logar)

        self.tela_cadastro.botao_ir_cadastro.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.botao_sair.clicked.connect(self.voltarCadastro)

        self.tela_principal.botao_perfil.clicked.connect(self.abrirPerfil)
        self.tela_cadastro.botao_sair.clicked.connect(self.voltarCadastro)

        self.tela_principal.botao_postar.clicked.connect(self.postar)

        self.tela_perfil.botao_inicio.clicked.connect(self.abrirTelaPrincipal)
        self.tela_perfil.botao_sair.clicked.connect(self.abrirTelaInicial)

        self.tela_principal.botao_inicio.clicked.connect(self.sairSistema)

        self.tela_inicial.botao_sair.clicked.connect(QtWidgets.qApp.quit)

        self.tela_principal.botao_conversas.clicked.connect(self.abrirTelaConversas)
        self.tela_conversas.botao_enviar.clicked.connect(self.postarConversa)

        self.tela_principal.botao_perfil.clicked.connect(self.navegarEntrePosts)
        self.tela_conversas.botao_enviar.clicked.connect(self.conversa)

    def botaoCadastra(self):
        nome = self.tela_cadastro.caixa_nome.text()
        email = self.tela_cadastro.caixa_email.text()
        senha = self.tela_cadastro.caixa_senha.text()
        user = self.tela_cadastro.caixa_usuario.text()
        
        con = self.conexao.getConexao()
        con.reconnect()

        hash_senha = sha256(senha.encode())

        
        new = (user, email, nome, hash_senha.hexdigest())
        cursor = con.cursor()
        search_user = 'SELECT * FROM usuario WHERE user = %s'
        search_email = 'SELECT * FROM usuario WHERE email = %s'
        new_user = "INSERT INTO usuario (user, email, nome, senha) VALUES (%s, %s, %s, %s)"

        if not(nome == '' or email == '' or senha == '' or user == ''):
            cursor.execute(search_email, (email, ))
            e = cursor.fetchone()
            cursor.execute(search_user, (user, ))
            u = cursor.fetchone()
            if u != None or e != None:
                if u != None and e != None:
                    QMessageBox.information(None,'Error', 'Email e Usuário já cadastrados!')
                    self.tela_cadastro.caixa_email.setText('')
                    self.tela_cadastro.caixa_usuario.setText('')
                elif e != None:
                    QMessageBox.information(None,'Email', 'Email já cadastrado!')
                    self.tela_cadastro.caixa_email.setText('')
                else:
                    QMessageBox.information(None,'Usuário', 'Nome de usuário já cadastrado!')
                    self.tela_cadastro.caixa_usuario.setText('')
            else:
                QMessageBox.information(None,'Cadastro', 'Cadastro realizado com sucesso!')
                self.tela_cadastro.caixa_email.setText('')
                self.tela_cadastro.caixa_nome.setText('')
                self.tela_cadastro.caixa_senha.setText('')
                self.tela_cadastro.caixa_usuario.setText('')
                cursor.execute(new_user, new)
                con.commit()
                self.QtStack.setCurrentIndex(0)
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')

        cursor.close()
        con.close()



    def logar(self):
        user = self.tela_inicial.caixa_usuario.text()
        senha = self.tela_inicial.caixa_senha.text()
        con = self.conexao.getConexao()
        con.reconnect()
        cursor = con.cursor()
        comando = "SELECT * FROM usuario WHERE user = %s"

        cursor.execute(comando, (user, ))
        usuario = cursor.fetchone()
        hash_senha = sha256(senha.encode())

        print(usuario)
        if usuario != None and usuario[3] == hash_senha.hexdigest():
            self.QtStack.setCurrentIndex(3)
            self.tela_perfil.Nome.setText(usuario[0])
            self.tela_perfil.Email.setText(usuario[1])
            self.addText()
        else:
            QMessageBox.information(None,'POOII', 'Login ou senha errados!')
            self.tela_inicial.caixa_senha.setText('')
            self.tela_inicial.caixa_usuario.setText('')

        self.tela_inicial.caixa_senha.setText('')
        con.close()
        cursor.close()

    def navegarEntrePosts(self):
        usuario = self.tela_perfil.Nome.text()

        self.addTextUser(usuario)

    def postar(self):
        post = self.tela_principal.texto_postar.toPlainText()

        usuario = self.tela_perfil.Nome.text()
        con = self.conexao.getConexao()
        con.reconnect()
        cursor = con.cursor()
        comando = 'INSERT INTO postagem (mensagem, data, likes, usuario_user) VALUES ( %s, %s, %s, %s)'
        data = datetime.now()
        info = (post, str(data), 0, usuario)

        cursor.execute(comando, info)

        con.commit()
        con.close()

        self.addText()
        self.addTextUser(usuario)
        

    def postarConversa(self):
        post = self.tela_conversas.sendtext.text()
        # self.tela_conversas.sendandrec.setText(post)
        self.tela_conversas.sendtext.setText('')


    def abrirPerfil(self): # piadbsdoj
        self.QtStack.setCurrentIndex(4)
        self.tela_inicial.caixa_senha.setText('')

        user = self.tela_perfil.Nome.text()
        self.addTextUser(user)
    
    
    def abrirTelaConversas(self):
        self.QtStack.setCurrentIndex(5)

    def abrirTelaInicial(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)


    def abrirTelaLogin(self):
        self.QtStack.setCurrentIndex(2)

    def sairSistema(self):
        self.QtStack.setCurrentIndex(0)

    def abrirTelaPrincipal(self):
        self.QtStack.setCurrentIndex(3)
        self.tela_inicial.caixa_senha.setText('')
        
    
    def voltarCadastro(self):
        self.QtStack.setCurrentIndex(0)
        self.tela_cadastro.caixa_usuario.setText('')
        self.tela_cadastro.caixa_nome.setText('')
        self.tela_cadastro.caixa_senha.setText('')
        self.tela_cadastro.caixa_email.setText('')

    def voltarLogin(self):
        self.QtStack.setCurrentIndex(0)
        self.tela_inicial.caixa_senha.setText('')
        self.tela_inicial.caixa_usuario.setText('')

    def addText(self):
        con = self.conexao.getConexao()
        con.reconnect()
        cursor = con.cursor()

        text = ''
        comando = 'SELECT * FROM postagem'
        cursor.execute(comando)
        posts = cursor.fetchall()
        # print(posts)

        text = ''
        if(posts == list):
            print()
        else:
            for post in posts:
                text = f'\n{post[2]}             {post[1]}\n{post[3]}\n' + text
        
        con.commit()
        con.close()
        
        self.tela_principal.textBrowser.setText(text)
        self.tela_principal.texto_postar.setText('')
    
    def addTextUser(self, user):
        con = self.conexao.getConexao()
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
        
        self.tela_perfil.postArea.setText(text)
    
    def conversa(self):
        mensagem = self.tela_conversas.caixa_mensagem.toPlainText()
        con = self.conexao.getConexao()
        con.reconnect()
        cursor = con.cursor()

        comando = 'INSERT INTO conversa (user1, user2, mensagens1, mensagens2) VALUES ( %s, %s, %s, %s)'
        user1 = self.tela_perfil.Nome.text()
        user2 = 'teste'
        self.tela_conversas.area_mensagens.setText(mensagem)

        cursor.execute(comando, (user1, user2, mensagem, 'nada'))

        con.commit()
        con.close()

        # self.tela_conversas.area_mensagens.setText(mensagem)
        

    
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
