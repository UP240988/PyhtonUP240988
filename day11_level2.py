#Level 2
#1._Llama a tu función factorial, toma un número entero como parámetro y devuelve un factorial del número.
def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
print(factorial(5)) 
#2._Llama a tu función is_empty, toma un parámetro y verifica si está vacío o no
def is_empty(valor):
    return not bool(valor)

print(is_empty(""))      
print(is_empty([]))      
print(is_empty("texto")) 

#3._ Escribe diferentes funciones que tomen listas y calculen media, mediana, moda, rango, varianza y desviación estándar.

def calculate_mean(lista):
    return sum(lista) / len(lista)

def calculate_median(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    mitad = n // 2
    if n % 2 == 0:
        return (lista_ordenada[mitad - 1] + lista_ordenada[mitad]) / 2
    else:
        return lista_ordenada[mitad]

def calculate_mode(lista):
    from collections import Counter
    conteo = Counter(lista)
    max_freq = max(conteo.values())
    modos = [k for k, v in conteo.items() if v == max_freq]
    if len(modos) == 1:
        return modos[0]
    return modos  # Puede haber más de una moda

def calculate_range(lista):
    return max(lista) - min(lista)

def calculate_variance(lista):
    media = calculate_mean(lista)
    return sum((x - media) ** 2 for x in lista) / len(lista)

def calculate_std(lista):
    import math
    return math.sqrt(calculate_variance(lista))

# Ejemplo de uso:
datos = [1, 2, 2, 3, 4]

print("Media:", calculate_mean(datos))
print("Mediana:", calculate_median(datos))
print("Moda:", calculate_mode(datos))
print("Rango:", calculate_range(datos))
print("Varianza:", calculate_variance(datos))
print("Desviación estándar:", calculate_std(datos))