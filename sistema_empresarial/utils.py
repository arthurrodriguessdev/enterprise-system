import random
import string


def gerar_sequencia():
    sequencia = random.choices(string.digits, k=8)
    return ''.join(sequencia)