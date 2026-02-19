# Inisialisasi Matrix Awal
import numpy as np

print("Matrix A")
A = np.array([[1, 2, 3],
              [4, 5, 6]])

print(A)

print("\nBentuk (Shape) Matrix A")
print(A.shape)

# Transpose Matrix
print("\nTranspose matrix")
print("A.transpose():\n", A.transpose())
print("np.transpose(A):\n", np.transpose(A))
print("A.T:\n", A.T)

# Flatten Matrix (Ravel)
print("\nFlatten Matrix (Ravel)")
print("A.ravel():\n", A.ravel())
print("np.ravel(A):\n", np.ravel(A))

# Reshape Matrix
print("\nReshape Matrix")
print("A.reshape(new_rows, new_cols)")
print("A.reshape(3, 2):\n", A.reshape(3, 2))
print("A.reshape(6, 1):\n", A.reshape(6, 1))

# Resize Matrix
print("\nResize Matrix")
print("A.resize(new_rows, new_cols)")
A.resize(3, 2)
print("A.resize(3, 2):\n", A)