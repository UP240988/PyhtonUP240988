# exercise level 3

entero= 16 #Integer

decimal = 3.14 #Float

numero_complejo = 7 + 7j # complex bumber

string = "hola python" #String

booleano = True #Boolean

lista = [1, 2, 3, 4, 5] #List se puede modificar

tupla = (6, 7, 8, 9) #Tuple no se puede modificar

#set 
personas = personas = [
    {"nombre": "Jorgge", "edad": 25, "lenguaje": "Python"},
    {"nombre": "Ana", "edad": 22, "lenguaje": "JavaScript"},
    {"nombre": "Luis", "edad": 30, "lenguaje": "C++"}
]

# Imprimir los nombres de todas las personas
for persona in personas:
    print(persona["nombre"])

    # Euclidian distance 
import math

x1 , y1 = 2, 3 
x2 , y2 = 10, 8

distancia = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("Distancia euclidiana:", distancia)
