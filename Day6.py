#exercises day 6 level 1 

empty_tuple = ()
print(empty_tuple)                                                                      

hermanas = ( 'natalia', 'lucky',)
hermano = ('emilio',)
siblings = hermanas + hermano   
print(siblings)
print(len(siblings))
siblings = ('natalia', 'lucky', 'emilio')
papa = 'jorge' 
mama = 'lucila'
miembros_de_mi_familia = siblings +(papa, mama)
print(miembros_de_mi_familia)




padres = ('Emilio ', 'Lucila')
miembros_de_la_familia = siblings + padres
print(miembros_de_la_familia)

#Day 6 level 2
hermana1, hermana2, hermano, papa, mama = miembros_de_la_familia 
print("hermanas:", hermana1, "y", hermana2)
print("hermano:", hermano)
print("padre:", papa)
print("mama:", mama)

fruits = ( ' watermelon', 'strawberry', 'apple', ' kiwi')
vegetables = (' carrot', ' tomatoe', ' cucmber', 'abocado') 
animals = (' dog', 'cat', 'dolphin', ' shark')
food_stuff_tp = fruits + vegetables + animals 

food_stuff_lt = list(food_stuff_tp)
length = len(food_stuff_tp)

if length % 2 == 0:
    middle_items = food_stuff_tp[length//2 - 1 : length//2 + 1]
else:
    middle_items = (food_stuff_tp[length//2],)

print(middle_items)
food_stuff_lt = list(food_stuff_tp)

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print("First three items:", first_three)
print("Last three items:", last_three)

del food_stuff_tp

# Como ya borramos food_stuff_tp, usamos food_stuff_lt convertido en tupla de nuevo
food_tuple_check = tuple(food_stuff_lt)

if 'apple' in food_tuple_check:
    print("'apple' existe en la tupla.")
else:
    print("'apple' NO existe en la tupla.")
    nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)  # False
print('Iceland' in nordic_countries)  # True







