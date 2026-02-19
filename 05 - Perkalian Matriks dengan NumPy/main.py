# Perkalian Matriks di NumPy
## 1. Operator `@` (Operator Matriks)
import numpy as np

# Membuat matriks A (2x3)
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Membuat matriks B (3x2)
B = np.array([[7, 8],
              [9, 10],
              [11, 12]])

# Perkalian matriks menggunakan operator @
C = A @ B
print("Hasil A @ B:\n", C)

## 2. Fungsi `np.dot()`
# Perkalian matriks menggunakan np.dot()
C_dot = np.dot(A, B)
print("\nHasil np.dot(A, B):\n", C_dot)

## 3. Fungsi `np.matmul()`
# Perkalian matriks menggunakan np.matmul()
C_matmul = np.matmul(A, B)
print("\nHasil np.matmul(A, B):\n", C_matmul)

# Perbedaan dengan Perkalian Element-wise
# Membuat matriks P (2x2)
P = np.array([[1, 2],
              [3, 4]])

# Membuat matriks Q (2x2)
Q = np.array([[5, 6],
              [7, 8]])

# Perkalian element-wise
R_element_wise = P * Q
print("\nHasil P * Q (element-wise):\n", R_element_wise)