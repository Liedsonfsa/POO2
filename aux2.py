from hashlib import sha256

senha = 'teste'

s = sha256(senha.encode())

print(s.hexdigest())
