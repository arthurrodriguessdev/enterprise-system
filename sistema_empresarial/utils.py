import random
import string

def gerar_matricula():
    numero_matricula = random.choices(string.digits, k=8)
    return ''.join(numero_matricula)