# 1
edad = 25  
#2
altura = 1.75  
#3
numero_complejo = 3 + 4j  

#4
base = float(input("Ingresa la base del triángulo: "))
altura_triangulo = float(input("Ingresa la altura del triángulo: "))
area_triangulo = 0.5 * base * altura_triangulo
print("El área del triángulo es", area_triangulo)

#5
lado_a = float(input("Ingresa el lado a del triángulo: "))
lado_b = float(input("Ingresa el lado b del triángulo: "))
lado_c = float(input("Ingresa el lado c del triángulo: "))
perimetro_triangulo = lado_a + lado_b + lado_c
print("El perímetro del triángulo es", perimetro_triangulo)

# 6
largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

#7
radio = float(input("Ingresa el radio del círculo: "))
pi = 3.14
area_circulo = pi * radio * radio
circunferencia=2*pi*radio
print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)

#8
print("Pendiente:", 2)
print("Intersección con el eje x:", 1)
print("Intersección con el eje y:", -2)

#9
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente_puntos=(y2 - y1)/(x2 - x1)
distancia=((x2-x1)**2+(y2 - y1)**2)**0.5
print("Pendiente entre puntos:", pendiente_puntos)
print("Distancia euclídea:", distancia)

#10
print("¿Las pendientes son iguales?", 2 == pendiente_puntos)

#11
for x in range(-3, 1):
    y = x**2 + 6*x + 9
    print(f"x = {x}, y = {y}")
    if y == 0:
        print("El valor de y es 0 cuando x =", x)

#12
print("Longitud de 'python':", len("python"))
print("Longitud de 'dragon':", len("dragon"))
print("¿Las longitudes son diferentes?", len("python") != len("dragon"))

#13
print("¿'on' está en 'python' y 'dragon'?", 'on' in 'python' and 'on' in 'dragon')

#14
oracion = "Espero que este curso no esté lleno de jerga"
print("¿'jargon' está en la oración?", 'jerga' in oracion)

#15
print("¿'on' no está en 'python' ni en 'dragon'?", not ('on' in 'python' or 'on' in 'dragon'))

#16
longitud_python = len("python")
longitud_float = float(longitud_python)
longitud_cadena = str(longitud_float)
print("Longitud como float:", longitud_float)
print("Longitud como cadena:", longitud_cadena)

#17
numero = int(input("Ingresa un número para saber si es par: "))
print("¿Es número par?", numero%2==0)

#18
print("¿7 // 3 es igual a (2.7)?", 7 // 3 == int(2.7))

#19
print("¿El tipo de '10' es igual al tipo de 10?", type('10') == type(10))

# 20
print("¿int('9.8') == 10?", float('9.8') == 10)
 
# 21
horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
salario = horas*tarifa
print("Tu ingreso semanal es", salario)

#22
años_vividos = int(input("¿Cuántos años has vivido?: "))
segundos = años_vividos * 365 * 24 * 60 * 60
print("Has vivido aproximadamente", segundos, "segundos.")

#23
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")