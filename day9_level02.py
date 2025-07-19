#1
puntaje = int(input("Ingresa tu calificación (0-100): "))

if 80 <= puntaje <= 100:
    print("Tu calificación es A")
elif 70 <= puntaje <= 89:
    print("Tu calificación es B")
elif 60 <= puntaje <= 69:
    print("Tu calificación es C")
elif 50 <= puntaje <= 59:
    print("Tu calificación es D")
elif 0 <= puntaje < 50:
    print("Tu calificación es F")
else:
    print("Puntaje inválido")

#2
mes = input("Ingresa el nombre del mes: ").capitalize()

if mes in ["Septiembre", "Octubre", "Noviembre"]:
    print("La estación es Otoño")
elif mes in ["Diciembre", "Enero", "Febrero"]:
    print("La estación es Invierno")
elif mes in ["Marzo", "Abril", "Mayo"]:
    print("La estación es Primavera")
elif mes in ["Junio", "Julio", "Agosto"]:
    print("La estación es Verano")
else:
    print("Mes inválido")

#3
frutas = ['banana', 'naranja', 'mango', 'limón']
fruta = input("Ingresa el nombre de una fruta: ").lower()

if fruta in frutas:
    print("Esa fruta ya está en la lista.")
else:
    frutas.append(fruta)
    print("Fruta añadida. Lista actualizada:", frutas)
