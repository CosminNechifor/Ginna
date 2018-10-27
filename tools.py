import os


def get_token():
    path = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(path, 'token.txt')
    token = open(token_path, 'r').read().rstrip()
    return token
