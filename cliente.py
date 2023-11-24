<<<<<<< HEAD
from PyQt5 import QtCore, QtWidgets

from tela_principal import Tela_Principal
from tela_inicial import Tela_Inicial

import sys
import socket
import random


class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()

    def receive_message(self):
        message = self.client_socket.recv(1024)
        message = message.decode()

        print(message)
        self.signal.emit(message)


class Client(object):
    def __init__(self):
        self.messages = []
        self.mainWindow = QtWidgets.QMainWindow()

        # add widgets to the application window
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)

        self.chatWidget.setHidden(True)
        self.chat_ui = Tela_Principal()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.botao_postar.clicked.connect(self.send_message)

        self.connect_ui = Tela_Inicial()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.botao_logar.clicked.connect(self.btn_connect_clicked)

        self.mainWindow.setGeometry(QtCore.QRect(1080, 20,350, 500))
        self.mainWindow.show()

        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        
    def btn_connect_clicked(self):
        host = '171.0.0.1'
        port = 8007
        nickname = self.connect_ui.caixa_usuario.text()

        if len(host) == 0:
            host = "localhost"
        
        if len(port) == 0:
            port = 5555
        else:
            try:
                port = int(port)
            except Exception as e:
                error = "Invalid port number \n'{}'".format(str(e))
                print("[INFO]", error)
                self.show_error("Port Number Error", error)
        
        if len(nickname) < 1:
            nickname = socket.gethostname()

        nickname = nickname + "_" + str(random.randint(1, port))

        if self.connect(host, port, nickname):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)

            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()
            print("[INFO] recv thread started")


    def show_message(self, message):
        self.chat_ui.textBrowser.append(message)
        
    
    def connect(self, host, port, nickname):

        try:
            self.tcp_client.connect((host, port))
            self.tcp_client.send(nickname.encode())

            print("[INFO] Connected to server")

            return True
        except Exception as e:
            error = "Unable to connect to server \n'{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Connection Error", error)
            # self.connect_ui.hostTextEdit.clear()
            # self.connect_ui.portTextEdit.clear()
            
            return False
        

    def send_message(self):
        message = self.chat_ui.texto_postar.toPlainText()
        self.chat_ui.textBrowser.append("Me: " + message)

        print("sent: " + message)

        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_ui.texto_postar.clear()


    def show_error(self, error_type, message):
        errorDialog = QtWidgets.QMessageBox()
        errorDialog.setText(message)
        errorDialog.setWindowTitle(error_type)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        errorDialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())
=======
import socket
# import tela_principal

class Client:
    def __init__(self, user):
        self.user = user
        self.tcp_user = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rede = ('localhost', 5555)
        
    
    
    def enviarMensagem(self, mensagem):
        
        pass

    def conversa(self):
        self.tcp_user.connect(cliente.rede)
        # texto = self.tela
        pass



if __name__ == '__main__':
    handle = input('handle: ')
    cliente = Client(handle)
    cliente.tcp_user.connect(cliente.rede)
    cliente.tcp_user.send(handle.encode())
    while True:
            try:
                enviar = input('mensagem: ')
                if enviar == 'bye':
                    cliente.tcp_user.send(enviar.encode())
                    print("saindo...")
                    if enviar == 'bye':
                        cliente.tcp_user.close()
                cliente.tcp_user.send(enviar.encode())
            except:
                cliente.tcp_user.close()
                break
>>>>>>> main
