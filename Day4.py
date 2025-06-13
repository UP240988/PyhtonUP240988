# 1. Concatenar cadenas
print(' '.join(['Thirty', 'Days', 'Of', 'Python']))
print(' '.join(['Coding', 'For', 'All']))

print()

# 2. Declarar variable
company = "Coding For All"

print()

# 3. Imprimir la variable
print(company)

print()

# 4. Imprimir longitud
print(len(company))

print()

# 5. Convertir a mayúsculas
print(company.upper())

print()

# 6. Convertir a minúsculas
print(company.lower())

print()

# 7. Capitalizar, formato título, invertir mayúsculas/minúsculas
print(company.capitalize())
print(company.title())
print(company.swapcase())

print()

# 8. Extraer la primera palabra (slice)
print(company[0:6])

print()

# 9. Verificar si contiene 'Coding' y encontrar su índice
print('Coding' in company)
print(company.find('Coding'))
print(company.index('Coding'))

print()

# 10. Reemplazar 'Coding' con 'Python'
print(company.replace('Coding', 'Python'))

print()

# 11. Reemplazar 'Everyone' con 'All'
print('Python for Everyone'.replace('Everyone', 'All'))

print()

# 12. Dividir por espacio
print(company.split())

print()

# 13. Dividir por coma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(', '))

print()

# 14. Carácter en el índice 0
print(company[0])

print()

# 15. Carácter del último índice
print(company[-1])

print()

# 16. Carácter en el índice 10
print(company[10])

print()

# 17. Acrónimo de 'Python For Everyone'
print(''.join([word[0] for word in 'Python For Everyone'.split()]))

print()

# 18. Acrónimo de 'Coding For All'
print(''.join([word[0] for word in company.split()]))

print()

# 19. Índice de la primera 'C'
print(company.index('C'))

print()

# 20. Índice de la primera 'F'
print(company.index('F'))

print()


# 21. Encontrar la última 'l' (desde la derecha)
print('Coding For All People'.rfind('l'))

print()


# 22-27. Manejo de una oración con 'porque'
# Se cambió la variable sentence al español
sentence = 'No puedes terminar una oración con porque porque porque es una conjunción'
# Encontrar el primer 'porque'
print(sentence.find('porque'))
# Encontrar el último 'porque'
print(sentence.rindex('porque'))
# Extraer la subcadena que contiene todos los 'porque' consecutivos
start = sentence.find('porque')
end = sentence.rindex('porque') + len('porque')
print(sentence[start:end])

print()


# 28. Verificar si comienza o termina con una cadena específica
print(company.startswith('Coding'))
print(company.endswith('coding'))

print()


# 29. Eliminar espacios en blanco
print('   Coding For All     '.strip())

print()


# 30. Comprobar si es un identificador válido
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

print()


# 31. Unir una lista con un hash como separador
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries))

print()


# 32. Secuencia de escape para nueva línea
print("Estoy disfrutando este desafío.\nSolo me pregunto qué sigue.")

print()


# 33. Secuencia de escape para tabulación
print("Nombre\tEdad\tPaís\tCiudad")
print("Asabeneh\t250\tFinlandia\tHelsinki")

print()


# 34. Formateo de cadena para el área de un círculo
radius = 10
area = 3.14 * radius ** 2
print("El área de un círculo con radio {} es {:.0f} metros cuadrados.".format(radius, area))

print()

# 35. Operaciones aritméticas con formato
a, b = 8, 6
print(str(a) + " + " + str(b) + " = " + str(a + b))
print(str(a) + " - " + str(b) + " = " + str(a - b))
print(str(a) + " * " + str(b) + " = " + str(a * b))
print(str(a) + " / " + str(b) + " = {:.2f}".format(a / b))
print(str(a) + " % " + str(b) + " = " + str(a % b))
print(str(a) + " // " + str(b) + " = " + str(a // b))
print(str(a) + " * " + str(b) + " = " + str(a * b))