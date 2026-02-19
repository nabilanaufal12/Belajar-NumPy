import numpy as np

# Array satu dimensi
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Array dua dimensi
matriks_a = np.array([[1, 2], [3, 4]])
matriks_b = np.array([[5, 6], [7, 8]])

# Operasi Aritmatika Dasar
## Penjumlahan (`+`)
hasil_penjumlahan_1d = a + b
print("Hasil Penjumlahan 1D:", hasil_penjumlahan_1d)

hasil_penjumlahan_2d = matriks_a + matriks_b
print("Hasil Penjumlahan 2D:\n", hasil_penjumlahan_2d)

## Pengurangan (`-`)
hasil_pengurangan_1d = a - b
print("\nHasil Pengurangan 1D:", hasil_pengurangan_1d)

hasil_pengurangan_2d = matriks_a - matriks_b
print("Hasil Pengurangan 2D:\n", hasil_pengurangan_2d)

## Perkalian (`*`)
hasil_perkalian_1d = a * b
print("\nHasil Perkalian 1D:", hasil_perkalian_1d)

hasil_perkalian_2d = matriks_a * matriks_b
print("Hasil Perkalian 2D:\n", hasil_perkalian_2d)

dot_product = matriks_a @ matriks_b
print("Hasil Perkalian Dot Product:\n", dot_product)

## Pembagian (`/`)
hasil_pembagian_1d = a / b
print("\nHasil Pembagian 1D:", hasil_pembagian_1d)

hasil_pembagian_2d = matriks_a / matriks_b
print("Hasil Pembagian 2D:\n", hasil_pembagian_2d)


# Operasi Scalar
array_scalar_penjumlahan = a + 5
print("\nPenjumlahan Skalar:", array_scalar_penjumlahan)

array_scalar_perkalian = b * 10
print("\nPerkalian Skalar:", array_scalar_perkalian)

array_scalar_pembagian = a / 2
print("\nPembagian Skalar:", array_scalar_pembagian)


# Operasi Lainnya
## Modulus (`%`)
c = np.array([10, 11, 12, 13])
d = np.array([2, 3, 4, 5])

hasil_modulus = c % d
print("\bHasil Modulus:", hasil_modulus)

## Pangkat (`**`)
hasil_pangkat_scalar = b ** 2
print("\nHasil Pangkat Skalar:", hasil_pangkat_scalar)

e = np.array([2, 3, 4, 5])
f = np.array([2, 2, 2, 2])
hasil_pangkat_array = e ** f
print("Hasil Pangkat Array:", hasil_pangkat_array)

## Operasi Perbandingan
perbandingan_lebih_besar = a > b
print("\nPerbandingan Lebih Besar:", perbandingan_lebih_besar)

perbandingan_sama_dengan = a == (b * 10)
print("Perbandingan Sama Dengan:", perbandingan_sama_dengan)


# Broadcasting
g = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
h = np.array([10, 20, 30])           # Shape (3,)

hasil_broadcasting = g + h
print("\nHasil Broadcasting:\n", hasil_broadcasting)