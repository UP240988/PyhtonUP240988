#Level 1
#1._Suma de dos números
def sumar_dos_numeros(a, b):
    return a + b

#2._Área de un círculo
import math

def area_del_circulo(radio):
    return math.pi * radio * radio

#3._Sumar múltiples números (con verificación)
def sumar_todos_los_numeros(*args):
    if all(isinstance(i, (int, float)) for i in args):
        return sum(args)
    else:
        return "Todos los elementos deben ser números."

#4._Conversión de Celsius a Fahrenheit
def convertir_celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32



#5._Determinar estación por mes
def verificar_estacion(mes):
    mes = mes.lower()
    estaciones = {
        "primavera": ["marzo", "abril", "mayo"],
        "verano": ["junio", "julio", "agosto"],
        "otoño": ["septiembre", "octubre", "noviembre"],
        "invierno": ["diciembre", "enero", "febrero"]
    }
    for estacion, meses in estaciones.items():
        if mes in meses:
            return estacion.capitalize()
    return "Mes inválido"

#7._Calcular pendiente de una recta
def calcular_pendiente(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "La pendiente es indefinida (división por cero)."
    return (y2 - y1) / (x2 - x1)

#8._Resolver ecuación cuadrática
import math

def resolver_ecuacion_cuadratica(a, b, c):
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales."
    x1 = (-b + math.sqrt(discriminante)) / (2*a)
    x2 = (-b - math.sqrt(discriminante)) / (2*a)
    return x1, x2



#9._Imprimir elementos de una lista
def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

#10._Invertir lista usando bucle
def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida



#11._Capitalizar elementos de una lista
def capitalizar_elementos_lista(lista):
    return [str(item).capitalize() for item in lista]



#12._Agregar ítem a una lista
def agregar_item(lista, item):
    lista.append(item)
    return lista



#13._Eliminar ítem de una lista
def eliminar_item(lista, item):
    if item in lista:
        lista.remove(item)
    return lista



#14._Sumar todos los números hasta N
def suma_de_numeros(n):
    return sum(range(n + 1))



#15._Sumar solo números impares
def suma_de_impares(n):
    return sum(i for i in range(n + 1) if i % 2 != 0)


#Sumar solo números pares
def suma_de_pares(n):
    return sum(i for i in range(n + 1) if i % 2 == 0)