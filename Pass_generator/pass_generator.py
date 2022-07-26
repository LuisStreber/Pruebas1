import random
import random as rd

letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '!#$&/?¡@'

unidos = f'{letras}{numeros}{simbolos}'

passwords = ''.join(rd.sample(unidos,10))
print(passwords)


