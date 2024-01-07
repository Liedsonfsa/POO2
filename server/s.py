import socket
import threading
import mydb


host = 'localhost'
porta = 5555
addr = (host, porta)

db = mydb.Mydb()

def menu(con, cliente):

    conectado = True

    while conectado:
        envio = con.recv(4096).decode()
        
        if envio[0] == '0':
            print(f"Mensagem 0 Servidor: {envio}")
            conectado = False
        elif envio[0] == '1':
            print(f"Mensagem 1 Servidor: {envio}")
            lista = envio.split(',')
            print(f'lista: {lista}')
            resposta = db.cadastrar(lista[1], lista[2], lista[3], lista[4])
            print(resposta)
            con.send(str(resposta).encode())
        elif envio[0] == '2':
            print(f"Mensagem 2 Servidor: {envio}")
            lista = envio.split(',')
            print(f'lista: {lista}')
            resposta = db.efetuarLogin(lista[1], lista[2])
            con.send(str(resposta).encode())
        elif envio[0] == '4':
            lista = envio.split(',')
            resposta = db.realizarPostagem(lista[1], lista[2])
            con.send(str(resposta).encode())
        elif envio[0] == '5':
            text = db.addText()
            # con.send(text.encode())
        elif envio[0] == '6':
            text = db.addTextUser(envio[1])
            # con.send(text.encode())
        


def main():
    print("[INICIADO] Aguardando conexão...")
    serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_socket.bind(addr)
    serv_socket.listen()

    while True:
        con, cliente = serv_socket.accept()
        thread = threading.Thread(target=menu, args=(con, cliente))
        thread.start()
        


if __name__ == "__main__":
    try:
        main()
    finally:
        print('não deu...')