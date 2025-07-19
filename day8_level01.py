#1
perro = {}
#2
perro["nombre"] = "Juan"
perro["color"] = "marrón"
perro["raza"] = "labrador"
perro["patas"] = 4
perro["edad"] = 5
print(perro)

#3
estudiante = {
    'nombre': 'Samuel',
    'apellido': 'Reyes',
    'genero': 'masculino',
    'edad': '18',
    'estado_civil': 'soltero',
    'habilidades': ['Hacer trucos en la bici', 'comer'],
    'pais': 'México',
    'ciudad': 'Encarnacion de Díaz',
    'direccion': {
        'calle': '13 de Septiembre',
        'codigo_postal': '47270'
    }
}
#4
print(len(estudiante)) 

#5
print(estudiante['habilidades'])       
print(type(estudiante['habilidades']))

#6
estudiante['habilidades'].append('Cocinar')
estudiante['habilidades'].append('Programar')
print(estudiante['habilidades']) 

#7
llaves = list(estudiante.keys())
print(llaves)

#8
valores = list(estudiante.values())
print(valores)

#9
tuplas = list(estudiante.items())
print(tuplas)

#10
del estudiante['estado_civil']
print(estudiante)

#11
del estudiante






