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