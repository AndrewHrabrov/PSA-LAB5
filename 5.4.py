import random
import string


def rand_name_file(length=1, expansion='txt'):
    new_name_file = ''.join(random.choices(string.ascii_letters, k=length))
    if expansion[0] != '.':
        new_name_file += '.' + expansion
    else:
        new_name_file += expansion
    return new_name_file



