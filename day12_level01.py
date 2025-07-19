import random
import string
#1
def id_usuario_aleatorio():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=6))

print("ID aleatorio de 6 caracteres:")
print(id_usuario_aleatorio())


#2
def id_usuario_por_usuario():
    try:
        longitud = int(input("¿Cuántos caracteres debe tener cada ID?: "))
        cantidad = int(input("¿Cuántos IDs deseas generar?: "))
        caracteres = string.ascii_letters + string.digits
        print("IDs generados:")
        for _ in range(cantidad):
            print(''.join(random.choices(caracteres, k=longitud)))
    except ValueError:
        print("Entrada inválida. Escribe solo números enteros.")

id_usuario_por_usuario()


#3
def generar_color_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print("3 Color generado en formato RGB:")
print(generar_color_rgb())
