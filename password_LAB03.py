import random
import string

def generate_secure_password():
    password = ''
    characters = string.ascii_letters + string.digits + string.punctuation
    password_length = 8
    for i in range(password_length):
        password += random.choice(characters)
    return password
secure_password = generate_secure_password()
print(secure_password)
