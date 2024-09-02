# Escreva um programa que inverta os caracteres de um string.

def inversor(s):
    lista = list(s)

    inicio_lista = 0
    fim_lista = len(lista) - 1

    while inicio_lista < fim_lista:
        lista[inicio_lista], lista[fim_lista] = lista[fim_lista], lista[inicio_lista]
        inicio_lista += 1
        fim_lista -= 1
    
    return ''.join(lista)

string1 = input("Adicione uma frase/palavra: ")
string2 = inversor(string1)
print(string1)
print(string2)
