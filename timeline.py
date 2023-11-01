class Timeline:
    __slots__ = ['_timeline']

    def __init__(self):
        self._timeline = ''
        pass

    
    def getPost(self, mensagem):
        print(self._timeline)
        self._timeline = self._timeline + f'{mensagem._perfil}\n{mensagem._mensagem}\n\n'
    
    def posts(self):
        return self._timeline
    
