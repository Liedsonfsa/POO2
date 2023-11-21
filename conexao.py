import mysql.connector

class Conexao:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='26.212.178.226',
            user='root',
            password='root',
            database='mydb'
        )
    
    def getConexao(self):
        return self.conexao
    
