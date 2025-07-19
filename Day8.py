# 1️ Crear un diccionario vacío llamado dog
dog = {}

# 2️ Agregar name, color, breed, legs, age al diccionario dog
dog['name'] = 'Max'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# 3️ Crear un diccionario student con múltiples claves
student = {
    'first_name': 'Jorge',
    'last_name': 'Muñoz',
    'gender': 'Male',
    'age': 22,
    'marital_status': 'Single',
    'skills': ['Python', 'Data Analysis'],
    'country': 'México',
    'city': 'Aguascalientes',
    'address': {
        'street': 'Calle 123',
        'zipcode': '20296'
    }
}

# 4️ Obtener la longitud del diccionario student
print(len(student))  # Resultado: 9

# 5️ Obtener el valor de skills y verificar su tipo de dato
print(student['skills'])        # ['Python', 'Data Analysis']
print(type(student['skills']))  # <class 'list'>

# 6️ Modificar skills agregando uno o dos más
student['skills'].extend(['GitHub', 'Machine Learning'])

# 7️ Obtener las claves como lista
print(list(student.keys()))

# 8️ Obtener los valores como lista
print(list(student.values()))

# 9️ Convertir el diccionario en una lista de tuplas usando items()
print(list(student.items()))

#  Eliminar un item del diccionario (por ejemplo, marital_status)
del student['marital_status']

# 1️ 1️ Eliminar completamente el diccionario dog
del dog