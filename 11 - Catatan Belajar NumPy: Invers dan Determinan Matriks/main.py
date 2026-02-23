# Menghitung Invers Matriks dengan NumPy
import numpy as np

A = np.array([[1, -1],
              [1,  1]])

print("Matriks A:")
print(A)

# Menghitung invers matriks A
A_inverse = np.linalg.inv(A) #
print("\nInvers Matriks A:")
print(A_inverse)

# Verifikasi dengan dot product
hasil_perkalian = np.dot(A, A_inverse) #
print("\nHasil A * A_inverse:")
print(hasil_perkalian)

# Menghitung determinan matriks A
det_A = np.linalg.det(A) #
print("\nDeterminan Matriks A:")
print(det_A)

# Menghitung determinan invers matriks A
det_A_inverse = np.linalg.det(A_inverse) #
print("\nDeterminan Invers Matriks A:")
print(det_A_inverse)