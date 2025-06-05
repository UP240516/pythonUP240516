# Verificación de tipos de datos
first_name = "Samuel"
last_name = "López"
age = 25
height = 1.75
is_student = True

print(type(first_name))   # str
print(type(last_name))    # str
print(type(age))          # int
print(type(height))       # float
print(type(is_student))   # bool

# Longitud del nombre
print("Longitud del nombre:", len(first_name))

# Comparación de longitudes
if len(first_name) > len(last_name):
    print("El nombre es más largo.")
elif len(last_name) > len(first_name):
    print("El apellido es más largo.")
else:
    print("Ambos tienen la misma longitud.")

# Operaciones matemáticas
num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print("Suma:", total)
print("Resta:", diff)
print("Multiplicación:", product)
print("División:", division)
print("Residuo:", remainder)
print("Exponente:", exp)
print("División entera:", floor_division)

# Área y circunferencia de un círculo con radio 30
radius = 30
pi = 3.1416
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

# Área con input del usuario
user_radius = float(input("Ingresa el radio del círculo: "))
user_area = pi * user_radius ** 2
print("Área del círculo ingresado:", user_area)

# Input de datos personales
first_name_input = input("Nombre: ")
last_name_input = input("Apellido: ")
country = input("País: ")
age_input = input("Edad: ")

print(f"{first_name_input} {last_name_input} de {country}, tiene {age_input} años.")

# Palabras reservadas de Python
help('keywords')
