import mysql.connector

class Conexao:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='root',
            database='mydb'
        )
    
    def getConexao(self):
        return self.conexao
    
