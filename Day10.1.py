#Day 10 level 1 

# Usando for
for i in range(11):
    print(i)

# Usando while
i = 0
while i <= 10:
    print(i)
    i += 1

    # Usando for
for i in range(10, -1, -1):
    print(i)

# Usando while
i = 10
while i >= 0:
    print(i)
    i -= 1
for i in range(1, 8):
    print('#' * i)

for i in range(8):
    for j in range(8):
        print('#', end=' ')
    print()  

for i in range(11):
    print(f"{i} x {i} = {i * i}")

techs = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for tech in techs:
    print(tech)  


for i in range(101):
    if i % 2 == 0:
        print(i)

for i in range(101):
    if i % 2 != 0:
        print(i)

