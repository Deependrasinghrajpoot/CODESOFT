import random
import string

def generate_password(length=9):
    chars =string.ascii_letters + string.digits + string.punctuation
    password ="".join(random.choice(chars) for i in range(length))
    return password

print(generate_password())