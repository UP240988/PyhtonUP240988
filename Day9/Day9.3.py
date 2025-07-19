#Day 9 level 3

# Diccionario de la persona
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# 1️⃣ Verificar si existe la clave 'skills' y mostrar la skill del medio
if 'skills' in person:
    skills = person['skills']
    middle = len(skills) // 2
    print("Middle skill:", skills[middle])

    # 2️⃣ Verificar si tiene la skill 'Python'
    print("Has Python skill?", 'Python' in skills)

    # 3️⃣ Evaluar título de desarrollador
    skills_set = set(skills)
    if skills_set == {'JavaScript', 'React'}:
        print("He is a front end developer")
    elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
        print("He is a backend developer")
    elif {'React', 'Node', 'MongoDB'}.issubset(skills_set):
        print("He is a fullstack developer")
    else:
        print("Unknown title")

# 4️⃣ Verificar si está casado y vive en Finlandia
if person.get('is_marred') and person.get('country') == 'Finland':
    full_name = person['first_name'] + ' ' + person['last_name']
    print(f"{full_name} lives in Finland. He is married.")