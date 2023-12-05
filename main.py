import sys
from datetime import datetime
import socket
import random

from hashlib import sha256

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from tela_cadastro import Tela_Cadastro
from tela_inicial import Tela_Inicial
from tela_principal import Tela_Principal
from tela_perfil import Tela_Perfil
from tela_conversas import Tela_Conversas
from tela_contatos import Tela_Contatos

from server.mydb import Mydb

ip = 'localhost'
porta = 5555
nome = 'liedson'
addr = ((ip, porta))
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client_socket.connect(addr)
    client_socket.send(nome.encode())
except Exception as e:
    print(f'Ocorreu uma exceção: {e}')
    exit()


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
        self.stack6 = QtWidgets.QMainWindow()

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

        self.tela_contatos = Tela_Contatos()
        self.tela_contatos.setupUi(self.stack6)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)


class Main(QMainWindow, Ui_Main):
    def __init__(self):
        super(Main, self).__init__(None)
        self.setupUi(self)


        self.tela_inicial.botao_ir_cadastro.clicked.connect(self.abrirTelaCadastro) # funções dos botões da tela principal

        self.tela_inicial.botao_logar.clicked.connect(self.logar)

        self.tela_cadastro.botao_ir_cadastro.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.botao_sair.clicked.connect(self.voltarCadastro)

        self.tela_principal.botao_perfil.clicked.connect(self.abrirPerfil)
        self.tela_cadastro.botao_sair.clicked.connect(self.voltarCadastro)

        self.tela_perfil.botao_inicio.clicked.connect(self.abrirTelaPrincipal)
        self.tela_perfil.botao_sair.clicked.connect(self.abrirTelaInicial)

        self.tela_principal.botao_inicio.clicked.connect(self.sairSistema)

        self.tela_inicial.botao_sair.clicked.connect(QtWidgets.qApp.quit)

        self.tela_principal.botao_conversas.clicked.connect(self.abrirTelaConversas)
        
        self.mydb = Mydb()
        
    
    def botaoCadastra(self):
        """
        Este módulo captura as informações preenchidas pelo usuário e se todos os campos estiverem preenchidos, as envia para o servidor.
        Caso as informações sejam válidas, o usuário é cadastrado.
        """
        nome = self.tela_cadastro.caixa_nome.text()
        email = self.tela_cadastro.caixa_email.text()
        senha = self.tela_cadastro.caixa_senha.text()
        user = self.tela_cadastro.caixa_usuario.text()
        
        hash_senha = sha256(senha.encode())
        
        lista = list()
        lista.append('1')
        lista.append(user)
        lista.append(email)
        lista.append(nome)
        lista.append(hash_senha.hexdigest())
        dados = ','.join(lista)
        
        if not(nome == '' or email == '' or senha == '' or user == ''):
            client_socket.send(dados.encode())
            try:
                resposta = client_socket.recv(4096).decode()
            except:
                print("\nNão foi possível permanecer conectado!\n")
                client_socket.close()

            if resposta != '0':
                if resposta == '3':
                    QMessageBox.information(None,'Error', 'Email e Usuário já cadastrados!')
                    self.tela_cadastro.caixa_email.setText('')
                    self.tela_cadastro.caixa_usuario.setText('')
                elif resposta == '1':
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
                self.QtStack.setCurrentIndex(0)
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')
    
    
    def logar(self):
        """
        Este módulo captura as informações fornecidas pelo usuário e caso sejam válidas, as envia para o servidor.
        Caso as informações estejam corretas, a conexão é permitida.
        """
        user = self.tela_inicial.caixa_usuario.text()
        senha = self.tela_inicial.caixa_senha.text()
        hash_senha = sha256(senha.encode())
        lista = list()
        print(f'user: {user}, senha: {hash_senha}')
        lista.append('2')
        lista.append(user)
        lista.append(hash_senha.hexdigest())
        print(f'1: {lista[1]}, 2: {lista[2]}')  
        dados = ','.join(lista)
        client_socket.send(dados.encode())
        print(f'dados: {dados}')
        try:
            resposta = client_socket.recv(4096).decode()
        except:
            print("\nNão foi possível permanecer conectado!\n")
            client_socket.close()
        
        if resposta == '0':
            self.QtStack.setCurrentIndex(3)
            self.tela_perfil.Nome.setText(user)
            self.tela_perfil.Email.setText('teste')
            client_socket.send('5'.encode())
        else:
            QMessageBox.information(None,'POOII', 'Login ou senha errados!')
            self.tela_inicial.caixa_senha.setText('')
            self.tela_inicial.caixa_usuario.setText('')

        self.tela_inicial.caixa_senha.setText('')


    # def postar(self):
    #     post = self.tela_principal.texto_postar.toPlainText()

    #     usuario = self.tela_perfil.Nome.text()
    #     con = self.conexao.getConexao()
    #     con.reconnect()
    #     cursor = con.cursor()
    #     comando = 'INSERT INTO postagem (mensagem, data, likes, usuario_user) VALUES ( %s, %s, %s, %s)'
    #     data = datetime.now()
    #     info = (post, str(data), 0, usuario)

    #     cursor.execute(comando, info)

    #     con.commit()
    #     con.close()

    #     self.send_message()
    #     # self.tcp_cliente.send(post.encode())

    #     self.addText()
    #     self.addTextUser(usuario)

    def postar(self):
        """
        Este módulo captura o conteúdo da postagem e o nome do usuário, e as envia para o servidor.
        """
        post = self.tela_principal.texto_postar.toPlainText()
        usuario = self.tela_perfil.Nome.text()

        client_socket.send(post.encode())
        lista = list()
        lista.append('4')
        lista.append(usuario)
        lista.append(post)
        dados = ','.join(lista)

        client_socket.send(dados.encode())
    

    
    def abrirPerfil(self):
        """
        ESte módulo abre a tela de perfil do usuário.
        """
        self.QtStack.setCurrentIndex(4)
        self.tela_inicial.caixa_senha.setText('')

        user = self.tela_perfil.Nome.text()
        # self.addTextUser(user)
    
    
    def abrirTelaConversas(self):
        """
        ESte módulo abre a tela de perfil do usuário.
        """
        self.QtStack.setCurrentIndex(6)

    def abrirTelaInicial(self):
        """
        Este módulo abre a tela inicial.
        """
        self.QtStack.setCurrentIndex(0)

    def abrirTelaCadastro(self):
        """
        Este módulo abre a tela de cadastro.
        """
        self.QtStack.setCurrentIndex(1)


    def abrirTelaLogin(self):
        """
        Este módulo abre a tela de login.
        """
        self.QtStack.setCurrentIndex(2)

    def sairSistema(self):
        """
        Este módulo abre a tela inicial.
        """
        self.QtStack.setCurrentIndex(0)

    def abrirTelaPrincipal(self):
        """
        Este módulo abre a tela principal.
        """
        self.QtStack.setCurrentIndex(3)
        self.tela_inicial.caixa_senha.setText('')
        
    
    def voltarCadastro(self):
        """
        Este módulo volta para a tela incial e reseta as informações dos line edits.
        """
        self.QtStack.setCurrentIndex(0)
        self.tela_cadastro.caixa_usuario.setText('')
        self.tela_cadastro.caixa_nome.setText('')
        self.tela_cadastro.caixa_senha.setText('')
        self.tela_cadastro.caixa_email.setText('')

    def voltarLogin(self):
        """
        Este módulo volta para a tela incial e reseta as informações dos line edits.
        """
        self.QtStack.setCurrentIndex(0)
        self.tela_inicial.caixa_senha.setText('')
        self.tela_inicial.caixa_usuario.setText('')

    def addText(self):
        """
        Este módulo envia um código para o servidor para que ele devolva todas as mensagens referentes a timeline que estão no banco de dados.
        """
        client_socket.send('5'.encode())
        text = client_socket.recv(4096).decode()
        self.tela_principal.textBrowser.setText(text)
        self.tela_principal.texto_postar.setText('')
        # self.tcp_cliente.send(post.encode())


    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
