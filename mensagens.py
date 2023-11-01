from datetime import datetime

class Mensagens:
    def __init__(self, mensagem, perfil):
        self._mensagem = mensagem
        self._perfil = perfil
        self._data = datetime.now()
        self._likes = 0
        self._comentarios = []
        
    
