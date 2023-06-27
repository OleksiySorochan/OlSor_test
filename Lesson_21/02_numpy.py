import numpy as np

a = np.array([1, 2, 3])
print(a)
print(type(a))

A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)

B = np.array([[1.3, 2, 3], [3, 4, 5]])
print(B)

C = np.array([[1, 2, 3], [3, 4, 5]], dtype=complex)
print(C)

z_matrix = np.zeros((2, 4), dtype=int)
print(z_matrix)

one_matrix = np.ones((3, 6), dtype=int)
print(one_matrix)

print(np.shape(A))
A = np.arange(12).reshape(2, 6)
print(A)

AAA = A.reshape(1, 12)
print(AAA)

print(A[0][-1])

A = np.array([[1, 2, 3], [3, 4, 5]])
B = np.array([[1, 2, 3], [3, 4, 5]])

C = A + B
print(C)
A = np.array([[1, 2, 3]])
B = np.array([[4],[5],[6]])
print(B)
C = A.dot(B)
print('this')
print(C)

S = np.array([[1, 2], [2, 1], [3, -3]])

# print(S)
# print(S.transpose())

a = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])

b = np.array([[1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4],
              [1, 2, 3, 4]])

d = a + b

print(d)