import socket

tcp_cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = ('localhost', 5555)
# connection = ('26.212.178.226', 5555)

tcp_cliente.connect(connection)

while True:
    mens = input('mensagem: ')
    tcp_cliente.send(mens.encode())
