#Create an empty tuple
empty_tuple = ()
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
siblings = ("Alice", "Bob", "Charlie", "Diana")
#Join brothers and sisters tuples and assign it to siblings
brothers = ("Bob", "Charlie")
sisters = ("Alice", "Diana")
siblings = brothers + sisters
#How many siblings do you have?
num_siblings = len(siblings)
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father = "John"
mother = "Jane"
family_members = siblings + (father, mother)



#Exercises: Level 2
# 1. Separar hermanos y padres
solo_hermanos, padre, madre = siblings
print("Hermanos y hermanas:", solo_hermanos)
print("Padre:", padre)
print("Madre:", madre)

# 2
frutas = ('platano', 'manzana', 'naranja')
vegetales = ('zanahoria', 'espinaca', 'papa')
productos_animales = ('leche', 'queso', 'huevo')

# 3
alimentos = frutas + vegetales + productos_animales

# 4
lista_alimentos = list(alimentos)

# 5
indice_medio = len(lista_alimentos) // 2
if len(lista_alimentos) % 2 == 0:
    elementos_medio = lista_alimentos[indice_medio-1:indice_medio+1]
else:
    elementos_medio = [lista_alimentos[indice_medio]]
print("Elemento(s) del medio:", elementos_medio)

# 6
primeros_tres = lista_alimentos[:3]
ultimos_tres = lista_alimentos[-3:]
print("Primeros 3 elementos:", primeros_tres)
print("Últimos 3 elementos:", ultimos_tres)

# 7
del alimentos 
