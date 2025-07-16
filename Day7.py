#Day 7 level 1 

it_companies = set()
print(len(it_companies))
it_companies.add("Twitter")
it_companies.update(["Spotify", "Youtube music", "Epic Games", "Amazon", "Google"])
it_companies.remove("Youtube music")
print(it_companies)
# remove se usa para eliminar un elemento específico
#discard se usa para eliminar un elemento específico sin generar error si no existe

#Day 7 level 2 
st1 = {"A"}
st2 = {"B"}
unidos = st1.union(st2)
print(unidos)
st1.intersection(st2)
print(st1.intersection(st2))  # Resultado: set() 

st1.issubset(st2)
print(st1.issubset(st2))  # false 

st1.isdisjoint(st2)
print(st1.isdisjoint(st2))  # true 

st1.union(st2)
print(st1.union(st2)) # Resultado: {'B', 'A'}
st2.union(st1)
print(st2.union(st1))  # Resultado: {'B', 'A'}

print(st1.symmetric_difference(st2)) # Resultado: {'B', 'A'}

del st1 
del st2 
