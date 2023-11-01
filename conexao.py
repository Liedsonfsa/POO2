import mysql.connector

class Conexao:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='127.0.0.1',
            database='mydb',
            user='root',
            password='root'
        )
    
    def getConexao(self):
        return self.conexao
    