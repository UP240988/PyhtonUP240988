#================================================================
# 🚨 Reglas de la evaluación (LEER ANTES DE COMENZAR)
# ================================================================
# - La evaluación debe realizarse de forma individual.
# - Está estrictamente prohibido el plagio:
#     - No copies código de otros compañeros.
#     - No busques soluciones en internet.
#     - No uses IA como ChatGPT, Copilot u otras herramientas externas.
# - Solo puedes tener abierto:
#     - Este archivo en Codespaces (VS Code en el navegador)
#     - El repositorio de GitHub de esta tarea.
# - Si se detecta copia o incumplimiento de estas reglas,
#   la calificación será cero.
# ================================================================

# Ingresa el número del ejercicio que deseas ejecutar (del 1 al 10):
ejercicio = input("Ingresa el numero: ").strip()

# --- Ejercicio 1 ---
if ejercicio == "1":
    jercicio = input("Ingresa el numero: ").strip()

# --- Ejercicio 1 ---
if ejercicio == "1":
    # Imprime una línea de saludo usando concatenación de strings.
    # Debe decir exactamente: ¡Bienvenido, estudiante de Python!
    contactena = ["¡Bienvenido, " + "estudiante de " + "Python!"]
    print(contactena)
    pass
# --- Ejercicio 2 ---
elif ejercicio == "2":
    # Calcula el cuadrado de la suma de 3 y 5.
    # Resultado esperado: 64
    suma= 3 + 5
    cuadrado = suma ** 2
    print(cuadrado)  
    pass

# --- Ejercicio 3 ---
elif ejercicio == "3":
    # Convierte el texto "3.14" a tipo float y súmale 2.86
    fo=float(3.14)
    agg= fo + 2.86
    print(agg)
    pass

# --- Ejercicio 4 ---
elif ejercicio == "4":
    # Dado el texto "programación", imprime cuántas letras tiene
    nletras= "programación" 
    print(len(nletras))

    pass

# --- Ejercicio 5 ---
elif ejercicio == "5":
    # Imprime el menor número entre -3, 0 y 2 multiplicado por -1 usando función min
    resultado = min(-3, 0, 2) * -1
    print(resultado)
    pass

# --- Ejercicio 6 ---
elif ejercicio == "6":
    # Dados los valores nombre = "Ana" y edad = 21,
    # imprime exactamente: Nombre: Ana - Edad: 21 años
    nombre = "Ana"
    edad = 21

    print("Nombre: " , nombre + " - Edad: " + str(edad) + " años")
    pass

# --- Ejercicio 7 ---
elif ejercicio == "7":
    # Dado el booleano `acceso = True`, imprime:
    # Acceso permitido si acceso es True, o Acceso denegado si es False.
    acceso = True

    print(acceso and "Acceso permitido" or "Acceso denegado")

# --- Ejercicio 8 ---
elif ejercicio == "8":
    # Dado el string "robot", imprime sus caracteres separados por comas usando un método.
    # Resultado esperado: r,o,b,o,t
    palabra = "robot"
    print(",".join(palabra))
    pass

# --- Ejercicio 9 ---
elif ejercicio == "9":
    # Dado el texto "  hola mundo  ", imprime la frase en mayúsculas
    # sin espacios al inicio ni al final usando un método.
    texto = "  hola mundo  "
    print(texto.strip().upper())
    pass

# --- Ejercicio 10 ---
elif ejercicio == "10":
    # Escribe un programa donde declare una variable anios = 28.
    # Calcula cuántos segundos hay en ese número de años,
    # asumiendo que cada año tiene 365 días.
    anios = 28
    segundos = anios and anios * 365 * 24 * 60 * 60 or 0
    print("Hay", segundos, "segundos en", anios, "años.")

    pass
    contactena = ["¡Bienvenido, " + "estudiante de " + "Python!"]
    print(contactena)
    pass
# --- Ejercicio 2 ---
elif ejercicio == "2":
    # Calcula el cuadrado de la suma de 3 y 5.
    # Resultado esperado: 64
    suma= 3 + 5
    cuadrado = suma ** 2
    print(cuadrado)  
    pass

# --- Ejercicio 3 ---
elif ejercicio == "3":
    # Convierte el texto "3.14" a tipo float y súmale 2.86
    fo=float(3.14)
    agg= fo + 2.86
    print(agg)
    pass

# --- Ejercicio 4 ---
elif ejercicio == "4":
    # Dado el texto "programación", imprime cuántas letras tiene
    nletras= "programación" 
    print(len(nletras))

    pass

# --- Ejercicio 5 ---
elif ejercicio == "5":
    # Imprime el menor número entre -3, 0 y 2 multiplicado por -1 usando función min
    resultado = min(-3, 0, 2) * -1
    print(resultado)
    pass

# --- Ejercicio 6 ---
elif ejercicio == "6":
    # Dados los valores nombre = "Ana" y edad = 21,
    # imprime exactamente: Nombre: Ana - Edad: 21 años
    nombre = "Ana"
    edad = 21

    print("Nombre: " , nombre + " - Edad: " + str(edad) + " años")
    pass

# --- Ejercicio 7 ---
elif ejercicio == "7":
    # Dado el booleano `acceso = True`, imprime:
    # Acceso permitido si acceso es True, o Acceso denegado si es False.
    acceso = True

    print(acceso and "Acceso permitido" or "Acceso denegado")

# --- Ejercicio 8 ---
elif ejercicio == "8":
    # Dado el string "robot", imprime sus caracteres separados por comas usando un método.
    # Resultado esperado: r,o,b,o,t
    palabra = "robot"
    print(",".join(palabra))
    pass

# --- Ejercicio 9 ---
elif ejercicio == "9":
    # Dado el texto "  hola mundo  ", imprime la frase en mayúsculas
    # sin espacios al inicio ni al final usando un método.
    texto = "  hola mundo  "
    print(texto.strip().upper())
    pass

# --- Ejercicio 10 ---
elif ejercicio == "10":
    # Escribe un programa donde declare una variable anios = 28.
    # Calcula cuántos segundos hay en ese número de años,
    # asumiendo que cada año tiene 365 días.
    anios = 28
    segundos = anios and anios * 365 * 24 * 60 * 60 or 0
    print("Hay", segundos, "segundos en", anios, "años.")

    pass