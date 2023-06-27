A = [[1, 2, 3, 4],
     [-5, 12, 7, 21],
     [-6, 30, 5, 23]]

# print(A)
# print(A[0][3])
# print(A[1][-1])


X = [[2, 4, 5],
     [6, 5, 6],
     [9, 3, 1]]

Y = [[3, 5, 9],
     [4, 6, 7],
     [5, 7, 2]]

# Спочатку потрібно згенерувати нульову матрицю
Z = [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]]

# Додавання і віднімання матриці

for i in range(len(X)):
     for j in range(len(X[0])):
          Z[i][j] = X[i][j] - Y[i][j]

# for r in Z:
     # print(r)

# множення матриць

for i in range(len(X)):
     for j in range(len(Y[0])):
          for k in range(len(Y)):
               Z[i][j] = X[i][k] * Y[k][j]
               # print(f'Z[{i}][{j}] = X[{i}][{k}] * Y[{k}][{j}]')

for r in Z:
     print(r)

# трансопнування матриці

XXX = [[5, 12],
       [45, 17],
       [56, 23]]

ZZZ = [[0, 0, 0],
       [0, 0, 0]]

for i in range(len(XXX)):
     for j in range(len(XXX[0])):
          ZZZ[j][i] = XXX[i][j]

# for r in ZZZ:
     # print(r)

import numpy as np
a = [[1, 2, 3]]
b = [[4],
     [5],
     [6]]


z = [[0, 0, 0,],
     [0, 0, 0,],
     [0, 0, 0,]]
for i in range(len(X)):
     for j in range(len(Y[0])):
          for k in range(len(Y)):
               z[i][j] += X[i][k] * Y[k][j]
print('*'*40)
# for i in z:
#      print(i)
A = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])
B = np.array([[1, 2],
              [2, 3],
              [3, 4]])
C = np.matmul(A, B)
print('*'*40)
# print(A)
# print(B)
print('*'*40)
# print(C)
c = A.dot(B)
print(c)