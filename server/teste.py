email = "nuke@gmail.com"
extensions = "@gmail.com"

size = len(email)

limit = size - 10

print(email[limit:])

ext = email[limit:]

true = False

if ext == extensions:
    true = not true

print(true)
