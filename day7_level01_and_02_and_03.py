# 
empresas_tecnologicas = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# 1
print("Cantidad de empresas:", len(empresas_tecnologicas))

# 2
empresas_tecnologicas.add('Twitter')
print("Empresas después de agregar Twitter:", empresas_tecnologicas)

# 3
empresas_tecnologicas.update(['Tesla', 'Samsung', 'Intel'])
print("Empresas después de agregar varias:", empresas_tecnologicas)

# 4
empresas_tecnologicas.remove('Oracle')
print("Empresas después de eliminar Oracle:", empresas_tecnologicas)

# 5. ¿Cuál es la diferencia entre remove y discard?
# - remove() lanza error si el elemento no existe.
# - discard() NO lanza error si el elemento no existe.

#LEVEL 2

#
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1
union_AB = A.union(B)
print("Unión de A y B:", union_AB)

# 2
interseccion_AB = A.intersection(B)
print("Intersección de A y B:", interseccion_AB)

# 3
print("¿A es subconjunto de B?", A.issubset(B))

# 4
print("¿A y B son disjuntos?", A.isdisjoint(B))

# 5
A.update(B)
print("A unido con B:", A)

B.update(A)
print("B unido con A:", B)

# 6
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
diferencia_simetrica = A.symmetric_difference(B)
print("Diferencia simétrica entre A y B:", diferencia_simetrica)

# 7
del A
del B

#LEVEL 3
# 1
edades = [22, 19, 24, 25, 26, 24, 25, 24]
conjunto_edades = set(edades)

print("Longitud de la lista de edades:", len(edades))        
print("Longitud del conjunto de edades:", len(conjunto_edades)) 


# 2. Explicar la diferencia entre: string, list, tuple, set
# String: texto (cadena de caracteres)
# Lista (list): colección ordenada y modificable
# Tupla (tuple): colección ordenada pero inmodificable
# Conjunto (set): colección no ordenada y sin elementos duplicados

# 3.
oracion = "Soy un profesor y me encanta inspirar y enseñar a las personas"
palabras = oracion.split()
palabras_unicas = set(palabras)

print("Palabras únicas:", palabras_unicas)
print("Cantidad de palabras únicas:", len(palabras_unicas))

