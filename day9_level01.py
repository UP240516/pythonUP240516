#LEVEL 01
#1
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Tienes la edad suficiente para aprender a conducir.")
else:
    años_faltantes = 18 - edad
    print(f"Te faltan {años_faltantes} años para aprender a conducir.")

#2
edad1 = 25
edad2 = int(input("Ingresa tu edad: "))

if edad2 > edad1:
    diferencia = edad2 - edad1
    if diferencia == 1:
        print("Eres 1 año mayor que yo.")
    else:
        print(f"Eres {diferencia} años mayor que yo.")
elif edad2 < edad1:
    diferencia = edad1 - edad2
    if diferencia == 1:
        print("Soy 1 año mayor que tú.")
    else:
        print(f"Soy {diferencia} años mayor que tú.")
else:
    print("Tenemos la misma edad.")


#3
numero_uno = int(input("Ingresa el primer número: "))
numero_dos = int(input("Ingresa el segundo número: "))

if numero_uno > numero_dos:
    print(f"{numero_uno} es mayor que {numero_dos}")
elif numero_uno < numero_dos:
    print(f"{numero_uno} es menor que {numero_dos}")
else:
    print("Ambos números son iguales")

