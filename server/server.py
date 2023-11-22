import socket
import threading

from PyQt5 import QtCore

# HEADER = 64
# PORT = 5555

# SERVER = 'localhost'
# print(SERVER)
# print(socket.gethostname())
# ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'

# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)

# def handle_client(conn, addr):
#     handle = conn.recv(1024).decode(FORMAT)
#     print(f"{handle} caiu de paraquedas...")
#     connected = True
#     while connected:

#         msg_length = conn.recv(1024).decode(FORMAT)
#         msg = msg_length

#         if msg == 'bye':
#             connected = False
#         else:
#             print(f"{handle}: {msg}")
        
    
#     print(f'{handle} pulou fora...')
#     conn.close()

# def start():
#     server.listen()
#     print(f"[LISTENING] Server is listening on {SERVER}")
#     while True:
#         conn, addr = server.accept()
#         thread = threading.Thread(target=handle_client, args=(conn, addr))
#         thread.start()
#         print(f"[Online] {threading.activeCount() - 1}")

# print("[STARTING] server is starting...")
# start()

# from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

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
    

class Server:
    def __init__(self, host, port):
        self.conecction = (host, port)
        # self.thread = threading.Thread(target=handle_client, args=(conn, addr))
    
    def start_server(self):
        print('iniciou...')
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(self.conecction)
        server.listen()
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
        
        print('fechou...')
        
    
    def handle_client(conn, addr):
        # handle = conn.recv(1024).decode(FORMAT)
        # print(f"{handle} caiu de paraquedas...")
        connected = True
        while connected:

            msg_length = conn.recv(1024).decode(FORMAT)
            msg = msg_length

            if msg == 'bye':
                connected = False
            else:
                print(f"msg: {msg}")
            
        
        print(f'pulou fora...')
        conn.close()


if __name__ == '__main__':
    server = Server('localhost', 5555)
    server.start_server()
    