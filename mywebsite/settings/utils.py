from django.utils.crypto import get_random_string


# From: https://stackoverflow.com/a/16630719
def generate_secret_key_file(directory):
    with open(directory, 'w') as arq:
        key = generate_secret_key_var()
        arq.write("\n" + key + "\n")


def generate_secret_key_var():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    key = get_random_string(50, chars)

    return "SECRET_KEY = '" + key + "'"
