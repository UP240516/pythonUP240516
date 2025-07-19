#1
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(es_primo(7))  
print(es_primo(10))  

#2
def son_unicos(lista):
    return len(lista) == len(set(lista))

print(son_unicos([1, 2, 3]))      
print(son_unicos([1, 2, 2, 3]))    

#3
def mismo_tipo(lista):
    if not lista:
        return True
    tipo = type(lista[0])
    return all(isinstance(i, tipo) for i in lista)

print(mismo_tipo([1, 2, 3]))        
print(mismo_tipo(['a', 'b', 3]))    

#4
def es_variable_valida(nombre):
    return nombre.isidentifier()

print(es_variable_valida('nombre_valido'))  # True
print(es_variable_valida('123abc'))         # False

#5
from collections import Counter

countries_data = [
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": ["Pashto", "Uzbek", "Turkmen"],
        "population": 27657145,
        "area": 652230
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": ["Albanian"],
        "population": 2886026,
        "area": 28748
    },
    {
        "name": "Algeria",
        "capital": "Algiers",
        "languages": ["Arabic"],
        "population": 40400000,
        "area": 2381741
    },
    {
        "name": "Andorra",
        "capital": "Andorra la Vella",
        "languages": ["Catalan"],
        "population": 78014,
        "area": 468
    },
    {
        "name": "Angola",
        "capital": "Luanda",
        "languages": ["Portuguese"],
        "population": 25868000,
        "area": 1246700
    },
     {
        "name": "Angola",
        "capital": "Luanda",
        "languages": ["Portuguese"],
        "population": 25868000,
        "area": 1246700
    },
     {
        "name": "Angola",
        "capital": "Luanda",
        "languages": ["Portuguese"],
        "population": 25868000,
        "area": 1246700
    },
     {
        "name": "Angola",
        "capital": "Luanda",
        "languages": ["Portuguese"],
        "population": 25868000,
        "area": 1246700
    },
     {
        "name": "Angola",
        "capital": "Luanda",
        "languages": ["Portuguese"],
        "population": 25868000,
        "area": 1246700
    },
   
]


def idiomas_mas_hablados(datos, cantidad=10):
    contador = Counter()
    for pais in datos:
        for idioma in pais['languages']:
            contador[idioma] += 1
    return contador.most_common(cantidad)
print("Idiomas más hablados:")
for idioma, cantidad in idiomas_mas_hablados(countries_data, 10):
    print(f"{idioma}: {cantidad} países")


