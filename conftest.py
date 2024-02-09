import random
import string

import pytest


@pytest.fixture
def generate_email():
    # с тремя числами начинают появляться коллизии когда аккаунт уже существует достаточно быстро
    email = 'alysakov5' + str(random.randint(0, 9999999)) + '@ya.ru'
    return email


@pytest.fixture
def generate_valid_password():
    letters = string.ascii_lowercase
    password = ''.join(random.choice(letters) for i in range(6))
    return password
