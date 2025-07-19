#1
def pares_e_impares(numero):
    pares = 0
    impares = 0
    for i in range(numero + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return f"Número de pares: {pares}, número de impares: {impares}"

print(pares_e_impares(100))

#2
def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

print(factorial(5))

#3
def esta_vacio(valor):
    return valor == "" or valor == [] or valor == {} or valor is None

print(esta_vacio(""))        
print(esta_vacio([1, 2]))    

#4
def calcular_promedio(lista):
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]
from collections import Counter

def calcular_moda(lista):
    conteo = Counter(lista)
    max_apariciones = max(conteo.values())
    modas = [k for k, v in conteo.items() if v == max_apariciones]
    return modas

def calcular_rango(lista):
    return max(lista) - min(lista)

def calcular_varianza(lista):
    promedio = calcular_promedio(lista)
    return sum((x - promedio) ** 2 for x in lista) / len(lista)

import math

def calcular_desviacion(lista):
    return math.sqrt(calcular_varianza(lista))

numeros = [1, 2, 3, 4, 5, 5, 6]

print("Promedio:", calcular_promedio(numeros))
print("Mediana:", calcular_mediana(numeros))
print("Moda:", calcular_moda(numeros))
print("Rango:", calcular_rango(numeros))
print("Varianza:", calcular_varianza(numeros))
print("Desviación estándar:", calcular_desviacion(numeros))
