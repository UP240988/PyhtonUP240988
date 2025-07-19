#Level 2
#1._Escriba una función list_of_hexa_colors que devuelva cualquier número de colores hexadecimales en una matriz (seis números hexadecimales escritos después de #. El sistema de numeración hexadecimal está formado por 16 símbolos, del 0 al 9 y las primeras 6 letras del alfabeto, de la a a la f. Consulte la tarea 6 para ver ejemplos de salida).
import random

def list_of_hexa_colors(n):
    colores = []
    for _ in range(n):
        color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
        colores.append(color)
    return colores

print(list_of_hexa_colors(5)) 

#2._Escriba una función list_of_rgb_colors que devuelva cualquier número de colores RGB en una matriz.
def list_of_rgb_colors(n):
    colores = []
    for _ in range(n):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colores.append(f"rgb({r},{g},{b})")
    return colores
print(list_of_rgb_colors(5))

#3._Escriba una función generate_colors que pueda generar cualquier cantidad de colores hexadecimales o rgb.
def generate_colors(tipo, cantidad):
    colores = []
    if tipo == 'hexa':
        for _ in range(cantidad):
            color = '#' + ''.join(random.choices('0123456789abcdef', k=6))
            colores.append(color)
    elif tipo == 'rgb':
        for _ in range(cantidad):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            colores.append(f"rgb({r},{g},{b})")
    return colores


print(generate_colors('hexa', 3))
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))