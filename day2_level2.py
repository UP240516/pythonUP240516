#1
first_name = "Samuel"
last_name = "Reyes"
age = 25
height = 1.75
is_student = True

print(type(first_name))  
print(type(last_name))    
print(type(age))         
print(type(height))       
print(type(is_student))   

#2
print("Longitud del nombre:", len(first_name))

#3
if len(first_name) > len(last_name):
    print("El nombre es más largo.")
elif len(last_name) > len(first_name):
    print("El apellido es más largo.")
else:
    print("Ambos tienen la misma longitud.")

#4
num1 = 5
num2 = 4
#5
total = num1 + num2
#6
diff = num1 - num2
#7
product = num1* num2
#8
division = num1 / num2
#9
remainder = num2 % num2
#10
exp = num1 ** num2
#11
floor_division = num1 // num2
#resultados de las anteriores oeraciones
print("Suma:", total)
print("Resta:", diff)
print("Multiplicación:", product)
print("División:", division)
print("Residuo:", remainder)
print("Exponente:", exp)
print("División entera:", floor_division)

# 12
radius = 30
pi = 3.1416
area_of_circle = pi * radius ** 2
circum_of_circle = 2 * pi * radius

print("Área del círculo:", area_of_circle)
print("Circunferencia del círculo:", circum_of_circle)

us_radio = float(input("Ingresa el radio del círculo: "))
us_area = pi * us_radio ** 2
print("Área del círculo ingresado:", us_area)

#13
first_name_input = input("Nombre: ")
last_name_input = input("Apellido: ")
country = input("País: ")
age_input = input("Edad: ")

print(f"{first_name_input} {last_name_input} de {country}, tiene {age_input} años.")

#14
help('keywords')



    