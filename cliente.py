import socket

ip = '127.0.0.1'

port = 8007
addr = ((ip, port))

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect(addr)


while True:
    try:
        enviar = input('mensagem: ')
        cliente_socket.send(enviar.encode())
        print('mensagem enviada: ' + enviar)
        print('mensagem recebida: ' + cliente_socket.recv(1024).decode())
        if cliente_socket.recv(1024).decode() == 'sair':
            cliente_socket.close()
            print('Caiu fora...')
    except:
        cliente_socket.close()
        break

