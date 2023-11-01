import sys
from datetime import datetime

from conexao import Conexao

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

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

    def botaoCadastra(self):
        nome = self.tela_cadastro.caixa_nome.text()
        email = self.tela_cadastro.caixa_email.text()
        senha = self.tela_cadastro.caixa_senha.text()
        user = self.tela_cadastro.caixa_usuario.text()
        if not(nome == '' or email == '' or senha == '' or user == ''):
            e = self.cad.checkEmail(email)
            u = self.cad.cadastrado(user)
            if u != False or e == True:
                if u != False and  e == True:
                    QMessageBox.information(None,'Error', 'Email e Usuário já cadastrados!')
                    self.tela_cadastro.caixa_email.setText('')
                    self.tela_cadastro.caixa_usuario.setText('')
                elif e == True:
                    QMessageBox.information(None,'Email', 'Email já cadastrado!')
                    self.tela_cadastro.caixa_email.setText('')
                else:
                    QMessageBox.information(None,'Usuário', 'Nome de usuário já cadastrado!')
                    self.tela_cadastro.caixa_usuario.setText('')
            else:
                usuario = Usuario(nome, user, senha, email)
                self.cad.cadastrar(usuario)
                QMessageBox.information(None,'Cadastro', 'Cadastro realizado com sucesso!')
                self.tela_cadastro.caixa_email.setText('')
                self.tela_cadastro.caixa_nome.setText('')
                self.tela_cadastro.caixa_senha.setText('')
                self.tela_cadastro.caixa_usuario.setText('')
                self.QtStack.setCurrentIndex(0)
        else:
            QMessageBox.information(None,'POOII', 'Todos os valores devem ser preenchidos!')
    
    
    
    def logar(self):
        user = self.tela_inicial.caixa_usuario.text()
        senha = self.tela_inicial.caixa_senha.text()
        usuario = self.cad.checkPassword(user, senha)
        if usuario != False:
            self.QtStack.setCurrentIndex(3)
            self.tela_perfil.Nome.setText(usuario.user)
            self.tela_perfil.Email.setText(usuario.email)
            self.tela_perfil.horario.setText('Seus últimos posts')
        else:
            QMessageBox.information(None,'POOII', 'Login ou senha errados!')
            self.tela_inicial.caixa_senha.setText('')
            self.tela_inicial.caixa_usuario.setText('')
        
        self.tela_inicial.caixa_senha.setText('')
    
    def teste(self):
        usuario = self.tela_perfil.Nome.text()
        u = self.cad.cadastrado(usuario)
        posts = u.posts()
        for pos, post in enumerate(posts):
            self.tela_principal.textBrowser.setText(post)
            print(post)
    
    def navegarEntrePosts(self):
        usuario = self.tela_perfil.Nome.text()
        u = self.cad.cadastrado(usuario)
        m = u.avancar()
        
        self.tela_perfil.postArea.setText(m)

    def postar(self):
        post = self.tela_principal.texto_postar.toPlainText()
        
        usuario = self.tela_perfil.Nome.text()
        m = Mensagens(post, usuario)
        u = self.cad.cadastrado(usuario)
        u.getPosts(m)
        
        self.timeline.getPost(m)
        posts = self.timeline.posts()

        self.tela_principal.horarioPost.setText(str(m._data))
        self.tela_principal.textBrowser.setText(posts)
        self.tela_principal.texto_postar.setText('')
    
    
    def postarConversa(self):
        post = self.tela_conversas.sendtext.text()
        # self.tela_conversas.sendandrec.setText(post)
        self.tela_conversas.sendtext.setText('')
    
    
    def abrirPerfil(self):
        self.QtStack.setCurrentIndex(4)
        self.tela_inicial.caixa_senha.setText('')
    
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
    

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())
