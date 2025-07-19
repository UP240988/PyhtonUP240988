#Level 3
#1._Llama a tu función shuffle_list, toma una lista como parámetro y devuelve una lista aleatoria
import random

def shuffle_list(lista):
    lista_copia = lista[:]
    random.shuffle(lista_copia)
    return lista_copia


print(shuffle_list([1, 2, 3, 4, 5]))

#2._Escriba una función que devuelva un array de siete números aleatorios del 0 al 9. Todos los números deben ser únicos.
def unique_random_seven():
    return random.sample(range(10), 7)

print(unique_random_seven())