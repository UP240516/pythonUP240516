#1
numeros = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numeros if n <= 0]
print("Números negativos y ceros:", negativos_y_ceros)

#2
lista_de_listas = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
lista_aplanada = [n for sub1 in lista_de_listas for sub2 in sub1 for n in sub2]
print("Lista aplanada:", lista_aplanada)

#3
tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print("Lista de tuplas:")
for t in tuplas:
    print(t)

#4
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
transformado = [[nombre.upper(), nombre[:3].upper(), capital.upper()] for [(nombre, capital)] in paises]
print("Países transformados:", transformado)

#5
paises = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
diccionarios = [{'pais': nombre.upper(), 'ciudad': capital.upper()} for [(nombre, capital)] in paises]
print("Diccionarios de países:")
for d in diccionarios:
    print(d)


#6
nombres = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
nombres_completos = [f"{nombre} {apellido}" for [(nombre, apellido)] in nombres]
print("Nombres completos:", nombres_completos)


#7
pendiente = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1) if x2 != x1 else 'Infinita'
print("Pendiente:", pendiente(2, 3, 5, 11))


interseccion_y = lambda m, x, y: y - m * x
print("Intersección en Y:", interseccion_y(2, 1, 4))  # y = 2x + 2 ⇒ b = 2

