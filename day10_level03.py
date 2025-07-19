# Lista de países del archivo countries.py
countries = [
  'Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
  'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
  'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso',
  'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Central African Republic', 'Chad', 'Chile', 'China',
  'Colombi', 'Comoros', 'Congo (Brazzaville)', 'Congo', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus',
  'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor (Timor Timur)', 'Ecuador',
  'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Fiji', 'Finland', 'France',
  'Gabon', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau',
  'Guyana', 'Haiti', 'Honduras', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel',
  'Italy', 'Jamaica', 'Japan', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait',
  'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
  'Luxembourg', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands',
  'Mauritania', 'Mauritius', 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Morocco', 'Mozambique',
  'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Norway',
  'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland',
  'Portugal', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent',
  'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia and Montenegro', 'Seychelles',
  'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain',
  'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan',
  'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu',
  'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan',
  'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe'
]

# Lista de diccioarios de países (resumido a solo los necesarios para los ejercicios)
countries_data = [
    {"name": "Afghanistan", "languages": ["Pashto", "Uzbek", "Turkmen"], "population": 27657145},
    {"name": "Åland Islands", "languages": ["Swedish"], "population": 28875},
    {"name": "Albania", "languages": ["Albanian"], "population": 2886026},
    {"name": "Algeria", "languages": ["Arabic"], "population": 40400000},
    {"name": "Andorra", "languages": ["Catalan"], "population": 78014},
    {"name": "Angola", "languages": ["Portuguese"], "population": 25868000},
    {"name": "Argentina", "languages": ["Spanish", "Guaraní"], "population": 43590400},
    {"name": "Australia", "languages": ["English"], "population": 24117360},
    {"name": "Belgium", "languages": ["Dutch", "French", "German"], "population": 11319511},
    {"name": "Brazil", "languages": ["Portuguese"], "population": 206135893},
    {"name": "China", "languages": ["Chinese"], "population": 1377422166},
    {"name": "India", "languages": ["Hindi", "English"], "population": 1295210000},
    {"name": "Nigeria", "languages": ["English"], "population": 186988000},
    {"name": "Russia", "languages": ["Russian"], "population": 146599183},
    {"name": "United States", "languages": ["English"], "population": 323947000}
    # Puedes agregar más si lo deseas
]

# Países que contienen 'land'
paises_con_land = [pais for pais in countries if 'land' in pais]
print("Países que contienen 'land':")
for pais in paises_con_land:
    print(pais)

# Invertir lista de frutas
frutas = ['banana', 'orange', 'mango', 'lemon']
frutas_invertidas = []
for i in range(len(frutas)-1, -1, -1):
    frutas_invertidas.append(frutas[i])
print("\nFrutas invertidas:", frutas_invertidas)

# Total de idiomas únicos
idiomas = set()
for pais in countries_data:
    for idioma in pais['languages']:
        idiomas.add(idioma)
print("\nCantidad total de idiomas únicos:", len(idiomas))

# Diez idiomas más hablados
from collections import Counter
contador_idiomas = Counter()
for pais in countries_data:
    contador_idiomas.update(pais['languages'])
print("\nTop 10 idiomas más hablados:")
for idioma, cantidad in contador_idiomas.most_common(10):
    print(f"{idioma}: {cantidad}")

# Diez países más poblados
top_10_poblacion = sorted(countries_data, key=lambda pais: pais['population'], reverse=True)[:10]
print("\nTop 10 países más poblados:")
for pais in top_10_poblacion:
    print(f"{pais['name']}: {pais['population']:,}")
