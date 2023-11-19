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
