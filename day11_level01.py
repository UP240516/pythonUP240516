#1
def sumar_dos_numeros(num1, num2):
    return num1 + num2

print(sumar_dos_numeros(3, 5)) 

#2
def area_circulo(radio):
    pi = 3.1416
    return pi * radio * radio

print(area_circulo(10))  

#3
def sumar_todos(*numeros):
    suma = 0
    for numero in numeros:
        if not isinstance(numero, (int, float)):
            return "Todos los elementos deben ser números"
        suma += numero
    return suma

print(sumar_todos(1, 2, 3))        
print(sumar_todos(1, 'a', 3))       

#4
def convertir_c_f(celsius):
    return (celsius * 9/5) + 32

print(convertir_c_f(0))   
print(convertir_c_f(100))

#5
def estacion_por_mes(mes):
    mes = mes.lower()
    if mes in ['diciembre', 'enero', 'febrero']:
        return 'Invierno'
    elif mes in ['marzo', 'abril', 'mayo']:
        return 'Primavera'
    elif mes in ['junio', 'julio', 'agosto']:
        return 'Verano'
    elif mes in ['septiembre', 'octubre', 'noviembre']:
        return 'Otoño'
    else:
        return 'Mes no válido'

print(estacion_por_mes('abril')) 

#6
def calcular_pendiente(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

print(calcular_pendiente(1, 2, 3, 6))  # 2.0

#7
import math

def resolver_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No tiene soluciones reales"
    elif discriminante == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2*a)
        x2 = (-b - math.sqrt(discriminante)) / (2*a)
        return x1, x2

print(resolver_cuadratica(1, -3, 2))  

#8
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

imprimir_lista(['manzana', 'pera', 'uva'])

#9
def invertir_lista(lista):
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    return invertida

print(invertir_lista([1, 2, 3, 4, 5]))   
print(invertir_lista(["A", "B", "C"]))       


#10
def capitalizar_lista(lista):
    return [item.capitalize() for item in lista]

print(capitalizar_lista(['pan', 'leche', 'queso']))  # ['Pan', 'Leche', 'Queso']

#11
def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

alimentos = ['Papa', 'Tomate', 'Mango', 'Leche']
print(agregar_elemento(alimentos, 'Carne'))

numeros = [2, 3, 7, 9]
print(agregar_elemento(numeros, 5))

#12
def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

alimentos = ['Papa', 'Tomate', 'Mango', 'Leche']
print(eliminar_elemento(alimentos, 'Mango'))

numeros = [2, 3, 7, 9]
print(eliminar_elemento(numeros, 3))

#13
def suma_de_numeros(n):
    return sum(range(n+1))

print(suma_de_numeros(5))   
print(suma_de_numeros(10))  
print(suma_de_numeros(100)) 

#14
def suma_impares(n):
    return sum(i for i in range(n+1) if i % 2 != 0)

print(suma_impares(10))  

#15
def suma_pares(n):
    return sum(i for i in range(n+1) if i % 2 == 0)

print(suma_pares(10))  




