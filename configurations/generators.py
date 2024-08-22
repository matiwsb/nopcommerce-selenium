import random
import string

def generate_random_password():
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f'{password}'

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = random.choice(['gmail.com', 'yahoo.com', 'outlook.com'])
    return f'{username}@{domain}'