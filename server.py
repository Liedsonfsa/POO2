import socket

def get(host, port):
    addr = (host, port)

    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    serv_socket.bind(addr)
    serv_socket.listen(10)
    con, cliente = serv_socket.accept()

    return con, cliente


# host = '26.212.178.226'
# host = '127.0.0.1'
host = '0.0.0.0'

port = 8007

addr = (host, port)

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_socket.bind(addr)
serv_socket.listen(10)
print('aguardando...')

con, cliente = serv_socket.accept()
print('Conectando...')
print('aguardando mensagem...')

while True:
    try:
        recebe = con.recv(1024)
        if recebe.decode() !=  '':
            print('mensagem recebida: ' + recebe.decode())
            if recebe.decode() != 'sair' or recebe.decode() != '':
                if recebe.decode() == 'sair':
                    enviar = 'sair'
                else:
                    enviar = input('escreva algo: ')
                # enviar = ''
                con.send(enviar.encode())
            if enviar == 'sair':
                print('cliente saiu...')
            
    except:     
        addr = (host, port)

        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        serv_socket.bind(addr)
        serv_socket.listen(10)
        print('aguardando uma nova conexão...')

        con, cliente = serv_socket.accept()
    
        

