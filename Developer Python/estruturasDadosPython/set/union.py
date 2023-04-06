conjunto_a = {1,2}
conjunto_b = {3,4}

print(conjunto_a, conjunto_b)
print(conjunto_a.union(conjunto_b))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.intersection(conjunto_b))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.difference(conjunto_b))
print(conjunto_b.difference(conjunto_a))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4}

print(conjunto_a.symmetric_difference(conjunto_b))
print(conjunto_b.symmetric_difference(conjunto_a))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4,5,6}

print(conjunto_a.issubset(conjunto_b))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4,5,6}

print(conjunto_a.issubset(conjunto_b))
print(conjunto_b.issubset(conjunto_a))

conjunto_a = {1,2,3}
conjunto_b = {2,3,4,5,6}
conjunto_c = {4,0}

print(conjunto_a.isdisjoint(conjunto_b))
print(conjunto_a.isdisjoint(conjunto_c))

