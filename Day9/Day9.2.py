#Day 9 level 2 
fruits = ['banana', 'orange', 'mango', 'lemon']

#  1. Asignar calificación según la puntuación

score = int(input("Enter your score (0-100): "))

if 80 <= score <= 100:
    print("Grade: A")
elif 70 <= score < 80:
    print("Grade: B")
elif 60 <= score < 70:
    print("Grade: C")
elif 50 <= score < 60:
    print("Grade: D")
elif 0 <= score < 50:
    print("Grade: F")
else:
    print("Invalid score. Please enter a number between 0 and 100.")

#  2. Determinar la estación del año según el mes

month = input("Enter the month: ").strip().capitalize()

if month in ['September', 'October', 'November']:
    print("Season: Autumn")
elif month in ['December', 'January', 'February']:
    print("Season: Winter")
elif month in ['March', 'April', 'May']:
    print("Season: Spring")
elif month in ['June', 'July', 'August']:
    print("Season: Summer")
else:
    print("Invalid month name.")

# 🍊 3. Verificar si una fruta está en la lista

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit: ").lower()

if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Updated fruits list:", fruits)