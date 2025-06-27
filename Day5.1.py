# Lista de edades
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Ordenar y encontrar min y max
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Agregar min y max otra vez
ages.append(min_age)
ages.append(max_age)

# Mediana
ages.sort()
n = len(ages)
if n % 2 == 0:
    median = (ages[n//2 - 1] + ages[n//2]) / 2
else:
    median = ages[n//2]
# Promedio
average = sum(ages) / len(ages)

# Rango
age_range = max_age - min_age

# Diferencias absolutas
diff_min = abs(min_age - average)
diff_max = abs(max_age - average)

print("Edades ordenadas:", ages)
print("Edad mínima:", min_age)
print("Edad máxima:", max_age)
print("Mediana:", median)
print("Promedio:", average)
print("Rango:", age_range)
print("|min - promedio|:", diff_min)
print("|max - promedio|:", diff_max)

# Lista de países (ejemplo reducido)
countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Argentina', 'Armenia', 'Australia', 'Austria', 'Azerbaijan']

# País(es) del medio
mid = len(countries) // 2
if len(countries) % 2 == 0:
    middle_countries = countries[mid - 1:mid + 1]
else:
    middle_countries = [countries[mid]]

# Dividir en dos mitades
first_half = countries[: (len(countries) + 1) // 2]
second_half = countries[(len(countries) + 1) // 2 :]

print("\nPaís(es) del medio:", middle_countries)
print("Primera mitad:", first_half)
print("Segunda mitad:", second_half)

# Unpacking de países
countries_list = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
china, russia, usa, *scandic_countries = countries_list

print("\nChina:", china)
print("Russia:", russia)
print("USA:", usa)
print("Países escandinavos:", scandic_countries)