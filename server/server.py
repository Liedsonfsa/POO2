import socket
import threading

HEADER = 64
PORT = 5555

SERVER = 'localhost'
print(SERVER)
print(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'UTF-8'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    handle = conn.recv(1024).decode(FORMAT)
    print(f"{handle} caiu de paraquedas...")
    connected = True
    while connected:

        msg_length = conn.recv(1024).decode(FORMAT)
        msg = msg_length

        if msg == 'bye':
            connected = False
        else:
            print(f"{handle}: {msg}")
        
    
    print(f'{handle} pulou fora...')
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Online] {threading.activeCount() - 1}")
        


print("[STARTING] server is starting...")
start()