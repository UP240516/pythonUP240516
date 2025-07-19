import random

#1
def lista_colores_hexadecimal(cantidad):
    colores = []
    for _ in range(cantidad):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color)
    return colores

print("#1 Lista de colores hexadecimales:")
print(lista_colores_hexadecimal(5)) 

#2
def lista_colores_rgb(cantidad):
    colores = []
    for _ in range(cantidad):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores.append(f"rgb({r},{g},{b})")
    return colores

print("\n#2 Lista de colores RGB:")
print(lista_colores_rgb(5))  


#3
def generar_colores(tipo, cantidad):
    if tipo == 'hexa':
        return lista_colores_hexadecimal(cantidad)
    elif tipo == 'rgb':
        return lista_colores_rgb(cantidad)
    else:
        return ["Formato inválido. Usa 'hexa' o 'rgb'."]

print("\n#3 Colores generados con 'generate_colors':")
print(generar_colores('hexa', 3))
print(generar_colores('rgb', 2))
print(generar_colores('otro', 1))
