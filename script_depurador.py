import random
import time


personas = []


archivo = open('D:\\CURSO FULL STACK DEV\\bot spam\\ListaAmigos.txt')
num = 3

nLinea = 1

for linea in archivo:
    word = linea.split()
    if(len(word)) == 0: continue
    if nLinea == num:
        where = word[0].find('\"')
        new = word[0]
        palabra = new[where +1:]
        palabra = palabra[:len(palabra) -1]
        print(palabra)
        personas.append(palabra)
        num = num + 3

    nLinea = nLinea + 1

time.sleep(3)

