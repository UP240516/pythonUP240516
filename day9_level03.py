#1
persona = {
    'nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'pais': 'Finlandia',
    'casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'Calle Espacial',
        'codigo_postal': '02210'
    }
}

# 1. Mostrar la habilidad del medio si existe
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    posicion_media = len(habilidades) // 2
    print("Habilidad del medio:", habilidades[posicion_media])

# 2. Verificar si tiene Python
if 'habilidades' in persona:
    tiene_python = 'Python' in persona['habilidades']
    print("¿Tiene Python?", tiene_python)

# 3. Clasificar tipo de desarrollador
if set(persona['habilidades']) == {'JavaScript', 'React'}:
    print("Es desarrollador frontend")
elif all(h in persona['habilidades'] for h in ['Node', 'Python', 'MongoDB']):
    print("Es desarrollador backend")
elif all(h in persona['habilidades'] for h in ['React', 'Node', 'MongoDB']):
    print("Es desarrollador fullstack")
else:
    print("Título desconocido")

# 4. Verificar estado civil y país
if persona['casado'] and persona['pais'] == 'Finlandia':
    print(f"{persona['nombre']} {persona['apellido']} vive en {persona['pais']}. Está casado.")


