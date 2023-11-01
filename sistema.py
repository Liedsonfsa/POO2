class Sistema:
    __slot__ = ['_usuarios']

    def __init__(self):
        self._usuarios = []
    

    def cadastrar(self, usuario):
        for pessoa in self._usuarios:
            if usuario.user == pessoa.user:
                return False 
        self._usuarios.append(usuario)
        print(f'nome: {usuario.nome}, user: {usuario.user}, email: {usuario.email}, senha: {usuario.senha}')
        return True
    
    def cadastrado(self, user):
        for usuario in self._usuarios:
            if usuario.user == user:
                return usuario
        return False
    
    def checkEmail(self, email):
        for usuario in self._usuarios:
            if usuario.email == email:
                return True
        
        return False
    
    
    def checkPassword(self, user, userpassword):
        for usuario in self._usuarios:
            if (usuario.user == user and usuario.senha == userpassword):
                return usuario
        
        return False
    
