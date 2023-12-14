import socket
import threading
import mydb

host = 'localhost'
porta = 5555
addr = (host, porta)

db = mydb.Mydb()

class Servidor:
    """
    Servidor onde o cliente deverá se conectar.

    Attributes
    ----------
    con : socket
        server socket
    cliente : _RetAddress
        endereço do cliente
    
    Methods
    -------
    menu(con, cliente)
        recebe as requisições do cliente.
    main(None)
        mantém o servidor ativo.
    """

    def __init__(self, con, cliente):
        """
        Parameters
        ----------
        con : socket
        cliente : _RetAddress
            endereço 
        """
        self.con = con
        self.cliente = cliente
        pass
    

    def menu(self):
        """
        Onde o servidor funciona.

        Recebe as requisições do cliente e pode ou inserir informações no banco de dados ou retornar informações para o cliente.

        Parameters
        ----------
                con : socket do servidor
                cliente : endereço do cliente
        
        Returns
        -------
                None
        """

        conectado = True

        while conectado:
            envio = self.con.recv(4096).decode()
            
            if envio[0] == '0':
                print(f"Mensagem 0 Servidor: {envio}")
                conectado = False
            elif envio[0] == '1':
                print(f"Mensagem 1 Servidor: {envio}")
                lista = envio.split(',')
                print(f'lista: {lista}')
                resposta = db.cadastrar(lista[1], lista[2], lista[3], lista[4])
                print(resposta)
                self.con.send(str(resposta).encode())
            elif envio[0] == '2':
                print(f"Mensagem 2 Servidor: {envio}")
                lista = envio.split(',')
                print(f'lista: {lista}')
                resposta = db.efetuarLogin(lista[1], lista[2])
                self.con.send(str(resposta).encode())
            elif envio[0] == '4':
                lista = envio.split(',')
                print(lista)
                db.realizarPostagem(lista[1], lista[2])
            elif envio[0] == '5':
                text = db.addText()
                
                self.con.send(text.encode())
            elif envio[0] == '6':
                text = db.addTextUser(envio[1])
                
                self.con.send(text.encode())
            


    def main(self):
        """
        Onde o servidor fica ativo.
        """
        print("[INICIADO] Aguardando conexão...")
        serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv_socket.bind(addr)
        serv_socket.listen()

        while True:
            con, cliente = serv_socket.accept()
            server = Servidor(con,  cliente)
            thread = threading.Thread(target=self.menu, args=(server.con, server.cliente))
            thread.start()
        


if __name__ == "__main__":
    
    try:
        Servidor.main()
    finally:
        print('não deu...')
