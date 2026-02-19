# Stacking Vertikal (`np.vstack()`)
import numpy as np

# Contoh array
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

# Stacking vertikal
c = np.vstack((a, b))
print("Hasil Stacking Vertikal:")
print(c)


# Stacking Horizontal (`np.hstack()`)
# Contoh array
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

# Stacking horizontal
c = np.hstack((a, b))
print("\nHasil Stacking Horizontal:")
print(c)

# Stacking Sepanjang Sumbu Baru (`np.stack()`)
# Contoh array (harus memiliki shape yang sama)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stacking sepanjang sumbu baru (axis=0)
c_axis_0 = np.stack((a, b), axis=0)
print("\nHasil Stacking Sepanjang sumbu baru (axis=0):")
print(c_axis_0)

# Stacking sepanjang sumbu baru (axis=1)
c_axis_1 = np.stack((a, b), axis=1)
print("\nHasil Stacking Sepanjang sumbu baru (axis=1):")
print(c_axis_1)

# Contoh dengan array 2D
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

z = np.stack((x, y), axis=0)
print("\nHasil Stacking Sepanjang sumbu baru (axis=0) untuk array 2D:")
print(z)


# Stacking Kedalaman (`np.dstack()`)
# Contoh array
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# Stacking kedalaman
c = np.dstack((a, b))
print("\nHasil Stacking Kedalaman:")
print(c)