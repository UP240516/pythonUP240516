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

