import numpy as np

# Metode 1: Menggunakan Inverse Matriks
A = np.array([[2, 3],
              [1, 2]]) # Matriks koefisien

Y = np.array([[23],
              [14]]) # Matriks hasil

A_inverse = np.linalg.inv(A)

X1 = np.dot(A_inverse, Y)
print(X1)

# Metode 2: Menggunakan `np.linalg.solve()`
X2 = np.linalg.solve(A, Y)
print(X2)