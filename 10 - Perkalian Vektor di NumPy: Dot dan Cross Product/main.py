import numpy as np

# Dot Product (Produk Skalar)
# `numpy.dot()` fungsi
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

dot_product_result = np.dot(v1, v2)
# Hasil: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
print("dot_product_result:")
print(dot_product_result)

# Operator @ (Python 3.5+)
v1 = np.array([1, 2, 3])
v2 = np.array([4, 5, 6])

dot_product_result_at = v1 @ v2
print("\ndot_product_result_at:")
print(dot_product_result_at)


# Cross Product (Produk Vektor)
# `numpy.cross()` fungsi
v1 = np.array([1, 0, 0]) # Vektor di sepanjang sumbu x
v2 = np.array([0, 1, 0]) # Vektor di sepanjang sumbu y

cross_product_result = np.cross(v1, v2)
# Hasil: [0, 0, 1] (Vektor di sepanjang sumbu z, sesuai kaidah tangan kanan)
print("\ncross_product_result:")
print(cross_product_result)

v3 = np.array([1, 2, 3])
v4 = np.array([4, 5, 6])

cross_product_result_2 = np.cross(v3, v4)
# Hasil: [(2*6 - 3*5), (3*4 - 1*6), (1*5 - 2*4)] = [12-15, 12-6, 5-8] = [-3, 6, -3]
print("\ncross_product_result_2:")
print(cross_product_result_2)

# Cross Product dengan Vektor 2D
v5 = np.array([1, 0])
v6 = np.array([0, 1])

cross_product_2d = np.cross(v5, v6)
print("\ncross_product_2d:")
print(cross_product_2d)