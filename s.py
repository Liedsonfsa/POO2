import threading
import socket


class ClienteThread(threading.Thread):
    def _init_(self, clientAddress, clientesocket):
        threading.Thread._init_(self)
        self.csocket = clientesocket
        self.name = ''
        self.addr = clientAddress
        print('Nova conexão: ', clientAddress)

    def run(self):
        self.name = self.csocket.recv(1024).decode()
        print(self.name, "se conectou!")
        msg = ''
        while True:
            data = self.csocket.recv(1024)
            msg = data.decode()
            if msg == 'bye':
                break
            print('from', self.name+": ", msg)
            self.csocket.send(msg.encode())
        print('Cliente se ', self.addr, 'Desconectou...')


if __name__ == '__main__':
    localhost = '127.0.0.1'
    port = 8007
    addr = (localhost, port)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    print('Servidor iniciado!')
    print('Aguardando nova conexão...')
    while True:
        server.listen(20)
        clientsock, clientAddress = server.accept()
        newthread = ClienteThread(clientAddress, clientsock)
        newthread.start()
