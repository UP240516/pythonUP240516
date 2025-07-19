#1
suma_total = 0
for numero in range(101):
    suma_total += numero
print("La suma total es:", suma_total)

#2
suma_pares = 0
suma_impares = 0

for numero in range(101):
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print("La suma de pares es:", suma_pares)
print("La suma de impares es:", suma_impares)



