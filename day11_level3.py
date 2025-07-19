#Level 3
#1._Escriba una función llamada is_prime, que verifique si un número es primo.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(7))  
print(is_prime(10)) 

#2._ Escribe una función que verifique si todos los elementos de una lista son únicos.
def all_unique(lista):
    return len(lista) == len(set(lista))


print(all_unique([1, 2, 3, 4]))      
print(all_unique([1, 2, 2, 4]))      

#3._ Escribe una función que verifique si todos los elementos de una lista son del mismo tipo de dato.
def same_type(lista):
    if not lista:
        return True
    tipo = type(lista[0])
    return all(type(item) == tipo for item in lista)

print(same_type([1, 2, 3]))           
print(same_type([1, "2", 3]))         
print(same_type([]))    

#4._ Escribe una función que verifique si una variable proporcionada es un nombre de variable válido en Python.
def is_valid_variable(nombre):
    return nombre.isidentifier() and not nombre in {"False", "None", "True", "and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try", "while", "with", "yield"}

print(is_valid_variable("variable1"))   
print(is_valid_variable("1variable"))   
print(is_valid_variable("for"))         
print(is_valid_variable("my_var")) 

# Accede a los datos de países
datos_paises = [
    {"nombre": "China", "poblacion": 1409517397, "idiomas": ["Chino"]},
    {"nombre": "India", "poblacion": 1339180127, "idiomas": ["Hindi", "Inglés"]},
    {"nombre": "Estados Unidos", "poblacion": 324459463, "idiomas": ["Inglés"]},
    {"nombre": "Indonesia", "poblacion": 263991379, "idiomas": ["Indonesio"]},
    {"nombre": "Brasil", "poblacion": 209288278, "idiomas": ["Portugués"]},
    {"nombre": "Pakistán", "poblacion": 197015955, "idiomas": ["Urdu", "Inglés"]},
    {"nombre": "Nigeria", "poblacion": 190886311, "idiomas": ["Inglés"]},
    {"nombre": "Bangladés", "poblacion": 164669751, "idiomas": ["Bengalí"]},
    {"nombre": "Rusia", "poblacion": 143989754, "idiomas": ["Ruso"]},
    {"nombre": "México", "poblacion": 129163276, "idiomas": ["Español"]},
    {"nombre": "Japón", "poblacion": 127484450, "idiomas": ["Japonés"]}
]
#Función: Idiomas más hablados
from collections import Counter

def idiomas_mas_hablados(paises, top=10):
    contador_idiomas = Counter()
    for pais in paises:
        for idioma in pais["idiomas"]:
            contador_idiomas[idioma] += 1
    return contador_idiomas.most_common(top)

#Resultado esperado:
print(idiomas_mas_hablados(datos_paises, 5))
# [('Inglés', 4), ('Chino', 1), ('Hindi', 1), ('Indonesio', 1), ('Portugués', 1)]


#Función: Países más poblados
def paises_mas_poblados(paises, top=10):
    paises_ordenados = sorted(paises, key=lambda x: x["poblacion"], reverse=True)
    return paises_ordenados[:top]


#Respuesta:
for pais in paises_mas_poblados(datos_paises, 5):
    print(f'{pais["nombre"]}: {pais["poblacion"]}')


#Imprime los países más poblados:
China: 1409517397
India: 1339180127
Estados : 324459463
Indonesia: 263991379
Brasil: 209288278