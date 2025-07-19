# Day 10 level 3 

countries = [
    'Finland', 'Sweden', 'Iceland', 'Denmark', 'Norway', 'Ireland',
    'Thailand', 'Poland', 'Switzerland', 'Netherlands', 'New Zealand',
    'Germany', 'Canada', 'Mexico'
]

land_countries = []

for country in countries:
    if 'land' in country:
        land_countries.append(country)

print("Países que contienen 'land':", land_countries)

fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits = []

for i in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[i])

print("Lista de frutas invertida:", reversed_fruits)

countries_data = [
    {'name': 'China', 'population': 1444216107, 'languages': ['Chinese']},
    {'name': 'India', 'population': 1393409038, 'languages': ['Hindi', 'English']},
    {'name': 'United States', 'population': 331893745, 'languages': ['English']},
    {'name': 'Indonesia', 'population': 273523621, 'languages': ['Indonesian']},
    {'name': 'Pakistan', 'population': 220892331, 'languages': ['Urdu', 'English']},
    {'name': 'Brazil', 'population': 212559409, 'languages': ['Portuguese']},
    {'name': 'Nigeria', 'population': 206139587, 'languages': ['English']},
    {'name': 'Bangladesh', 'population': 164689383, 'languages': ['Bengali']},
    {'name': 'Russia', 'population': 145934460, 'languages': ['Russian']},
    {'name': 'Mexico', 'population': 128932753, 'languages': ['Spanish']},
    {'name': 'Germany', 'population': 83783945, 'languages': ['German']},
    {'name': 'France', 'population': 65273512, 'languages': ['French']},
]

all_languages = set()

for country in countries_data:
    for lang in country['languages']:
        all_languages.add(lang)

print("Número total de idiomas únicos:", len(all_languages))

from collections import Counter

language_counter = Counter()

for country in countries_data:
    for lang in country['languages']:
        language_counter[lang] += 1

most_spoken = language_counter.most_common(10)
print("10 idiomas más hablados:")
for lang, count in most_spoken:
    print(f"{lang}: {count} países")

most_populated = sorted(countries_data, key=lambda x: x['population'], reverse=True)[:10]

print("10 países más poblados:")
for country in most_populated:
    print(f"{country['name']}: {country['population']}")

