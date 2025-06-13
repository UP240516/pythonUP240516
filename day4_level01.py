# 2
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))  
print(' '.join(['Coding', 'For', 'All'])) 

# 3
company = "Coding For All"

# 4
print(company)

# 5
print(len(company))

# 6
print(company.upper())

# 7
print(company.lower())

# 8
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9
print(company[7:]) 
# 10
print(company.find('Coding') != -1) 
print(company.index('Coding'))

# 11
print(company.replace('Coding', 'Python'))

# 12
print("Python for Everyone".replace('Everyone', 'All'))

# 13
print(company.split())

# 14
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

# 15
print(company[0])

# 16
print(company[-1])

# 17
print(company[10])

# 18
frase= 'Python For Everyone'
print(''.join([frase[0] for frase in frase.split()]))

# 19
frase2= "Coding For All"
print(''.join([frase2[0] for frase2 in frase2.split()]))

# 20
print(company.index('C'))

# 21
print(company.index('F'))

# 22
print("Coding For All People".rfind('l'))

# 23
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))

# 24
print(sentence.rindex('because'))

# 25
print(sentence[31:54])

# 26
print(sentence.find('because'))

# 27
print(sentence[sentence.find('because'):sentence.find('because') + len('because because because')])

# 28
print(company.startswith('Coding'))

# 29
print(company.endswith('coding'))

# 30
print('   Coding For All      '.strip())

# 31
print("30DaysOfPython".isidentifier())  
print("thirty_days_of_python".isidentifier())

# 32
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

# 33
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# 35
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} es {int(area)} meters square.")

# 36
a, b = 8, 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
