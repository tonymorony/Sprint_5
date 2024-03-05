import random
import string


def generate_email():
    email = 'alysakov5' + str(random.randint(0, 9999999)) + '@ya.ru'
    return email


def generate_valid_password():
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(6))
    return password
