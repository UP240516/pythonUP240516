#LEVEL 2

#
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# 1
union_AB = A.union(B)
print("Unión de A y B:", union_AB)

# 2
interseccion_AB = A.intersection(B)
print("Intersección de A y B:", interseccion_AB)

# 3
print("¿A es subconjunto de B?", A.issubset(B))

# 4
print("¿A y B son disjuntos?", A.isdisjoint(B))

# 5
A.update(B)
print("A unido con B:", A)

B.update(A)
print("B unido con A:", B)

# 6
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
diferencia_simetrica = A.symmetric_difference(B)
print("Diferencia simétrica entre A y B:", diferencia_simetrica)

# 7
del A
del B
