import random

#1
def mezclar_lista(lista):
    lista_mezclada = lista[:]  
    random.shuffle(lista_mezclada)
    return lista_mezclada

print("#1 Lista mezclada:")
lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Original:", lista_original)
print("Mezclada:", mezclar_lista(lista_original))


#2
def siete_numeros_aleatorios_unicos():
    return random.sample(range(10), 7)

print("\n#2 Siete números únicos aleatorios (0-9):")
print(siete_numeros_aleatorios_unicos())
