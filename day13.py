#Level 1
#1._Filtrar solo los negativos y ceros en la lista usando la comprensión de listas
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negativos_y_ceros = [n for n in numbers if n <= 0]
print(negativos_y_ceros)

#2._Aplana la siguiente lista de listas de listas a una lista unidimensional
list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened = [num for sublist1 in list_of_lists for sublist2 in sublist1 for num in sublist2]
print(flattened)

#3._Usando la comprensión de listas, cree la siguiente lista de tuplas
tuplas = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]
print(tuplas)

#4._Aplana la siguiente lista para formar una nueva lista
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def simplificar_lista(paises):
    nueva_lista = []
    for grupo in paises:
        for pais, capital in grupo:
            nombre_mayus = pais.upper()
            abreviatura = nombre_mayus[:3]
            capital_mayus = capital.upper()
            nueva_lista.append([nombre_mayus, abreviatura, capital_mayus])
    return nueva_lista


print(simplificar_lista(countries))

#5._Cambie la siguiente lista a una lista de diccionarios
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

def convertir_a_diccionarios(paises):
    nueva_lista = []
    for grupo in paises:
        for pais, ciudad in grupo:
            nuevo_diccionario = {
                'country': pais.upper(),
                'city': ciudad.upper()
            }
            nueva_lista.append(nuevo_diccionario)
    return nueva_lista


print(convertir_a_diccionarios(countries))

#6._Cambie la siguiente lista de listas a una lista de cadenas concatenadas
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

def concatenar_nombres(lista):
    resultado = []
    for grupo in lista:
        for nombre, apellido in grupo:
            cadena = f"{nombre} {apellido}"
            resultado.append(cadena)
    return resultado


print(concatenar_nombres(names))

#7._Escriba una función lambda que pueda resolver una pendiente o una intersección con el eje y de funciones lineales
def pendiente_interseccion(x1, y1, x2, y2):
    pendiente = lambda x: (y2 - y1) / (x2 - x1) * (x - x1) + y1
    return pendiente    