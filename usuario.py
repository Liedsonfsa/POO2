class Usuario:
    __slots__ = ['_nome', '_user', '_senha', '_email', '_postagens']

    def __init__(self, nome, user, senha, email):
        self._nome = nome
        self._user = user
        self._senha = senha
        self._email = email
        self._postagens = ''

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, novo_user):
        self._user = novo_user

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, novo_email):
        self._email = novo_email
    
    def getPosts(self, mensagem):
        # print(self._postagens + mensagem._mensagem)
        self._postagens = self._postagens + f'{mensagem._data}\n{mensagem._mensagem}\n\n'
    
    
    def posts(self):
        lista = []
        for post in self._postagens:
            lista.append(post)
        return lista
    
    def avancar(self):
        # print(self._postagens)
        return self._postagens
    
    def voltar(self, value):
        return self._postagens[value]

        

