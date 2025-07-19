#Level 1
#1._Escribe una función que genere un ID de usuario aleatorio de seis dígitos/caracteres.
import random
import string

def random_user_id():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choices(caracteres, k=6))
print(random_user_id())

#2._Modifique la tarea anterior. Declare una función llamada user_id_gen_by_user. No acepta parámetros, pero acepta dos entradas mediante input(). Una de las entradas es el número de caracteres y la otra, el número de ID que se generarán.
import random
import string

def user_id_gen_by_user():
    num_chars = int(input("Número de caracteres por ID: "))
    num_ids = int(input("Número de IDs a generar: "))
    caracteres = string.ascii_letters + string.digits
    for _ in range(num_ids):
        print(''.join(random.choices(caracteres, k=num_chars)))
user_id_gen_by_user()

#3._Escriba una función llamada rgb_color_gen. Esta generará colores RGB (tres valores de 0 a 255 cada uno).
def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"  
print(rgb_color_gen())