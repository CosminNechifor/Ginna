import os


def get_token():
    path = os.path.dirname(os.path.abspath(__file__))
    token_path = os.path.join(path, 'token.txt')
    token = open(token_path, 'r').read().rstrip()
    return token


def save_to_notes(msg):
    first_name, last_name, message = msg
    file_name = first_name + '_' + last_name + '.txt'
    with open(file_name, 'a') as file:
        file.write(message + '\n')


def read_from_notes(user):
    first_name, last_name = user
    file_name = first_name + '_' + last_name + '.txt'
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except Exception:
        return "No content"
