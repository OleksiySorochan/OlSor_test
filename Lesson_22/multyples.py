# A = [2, 3, 6, 12, 5, 23, 73]
A = {2, 3, 6, 12, 5, 23, 73}
print(A)
print(len(A))

B = set([1, 2, 5, 7, 12, 10, 8])
print(B)
C = {1, 2, 5}
D = {0, 100, 200}

x = 3

print(min(A))
print(max(B))

print(x in A)
print(x not in B)

# Special Operations
print(A == B)
print(C < B)
print(A > B)
print(A != B)
# пересічення, спільні елементи двох множин
print(A & B)
# різниця між множинами, показує елементи які є в В але не має в А
print(A - B)
# сімметрічна різність, вибирає всі елементи множини А і В кірм спільних
print(A ^ B)

# C = A ^ B
# print(C)
# print(C := A ^ B)

# Methods
# Повертає True як що множина А немає пересіченя із множиною В
print(A.isdisjoint(D))
# Визначає чи є множина А підмножиною В, A < B
print(C.issubset(B))
# A > B
print(A.issuperset(B))
# об'єднання множин, може приймати одну або декілька множин
print(A.union(B, C, D))
# Пересічення , A & B
print(A.intersection(B))
# різниця
print(A.difference(B))
# сіметрична різниця
print(A.symmetric_difference(B))
A.symmetric_difference_update(B)
print(A)
A.update([100, 200, 300])
print(A)

A.add(1000)
print(A)
A.remove(1000)
print(A)
A.discard(1000)
A.pop() # видаляє довільний елемент
print(A)
A.clear()
print(A)