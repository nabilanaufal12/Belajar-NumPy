# 1. Indexing (Pengindeksan)
## 1.1. Pengindeksan Satu Dimensi (1D Array)
import numpy as np

print("Mengakses elemen tunggal")
arr_1d = np.array([10, 20, 30, 40, 50])

print(arr_1d[0])
print(arr_1d[3])
print(arr_1d[-1])

## 1.2. Pengindeksan Multi-Dimensi (2D, 3D Array, dst.)
print("\nMengakses elemen tunggal")
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(arr_2d[0, 0])
print(arr_2d[1, 2])

print("\nMengakses seluruh baris")
print(arr_2d[0])

print("\nMengakses seluruh kolom")
print(arr_2d[:, 1])

## 1.3. Pengindeksan Boolean (Boolean Indexing)
print("\nPengindeksan Boolean")
arr = np.array([1, 7, 3, 9, 2, 8])
kondisi = (arr > 5)

print(kondisi)
print(arr[kondisi])
print(arr[arr > 5])

## 1.4. Pengindeksan Integer (Fancy Indexing)
print("\nPengindeksan Integer")
arr_1d = np.array([10, 20, 30, 40, 50])
indeks = [0, 2, 4]

print(arr_1d[indeks])

print("\nUntuk 2D array")
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
# Memilih elemen (0,0), (1,2), (2,1)
baris_indeks = np.array([0, 1, 2])
kolom_indeks = np.array([0, 2, 1])

print(arr_2d[baris_indeks, kolom_indeks])


# 2. Slicing (Pemotongan)
## 2.1. Slicing Satu Dimensi (1D Array)
print("\nDasar")
arr_1d = np.array([10, 20, 30, 40, 50, 60])

print(arr_1d[1:4])
print(arr_1d[:3])
print(arr_1d[2:])
print(arr_1d[:])

print("\nDengan `step`")
print(arr_1d[::2])
print(arr_1d[1::2])
print(arr_1d[::-1])

## 2.2. Slicing Multi-Dimensi (2D Array)
print("\nMengambil sub-matriks")
arr_2d = np.array([[1, 2, 3, 4],
                   [5, 6, 7, 8],
                   [9, 10, 11, 12],
                   [13, 14, 15, 16]])
# Mengambil baris 0 dan 1, kolom 1 dan 2
sub_array = arr_2d[0:2, 1:3]

print(sub_array)

print("\nMengambil semua baris, kolom tertentu")
print(arr_2d[:, 0])

print("\nMengambil baris tertentu, semua kolom")
print(arr_2d[1, :])

print("\nMenggunakan `...` (Ellipsis)")
arr_3d = np.array([[[1, 2], [3, 4]],
                   [[5, 6], [7, 8]]])

print(arr_3d[..., 0])


# 3. Iterasi (Perulangan)
## 3.1. Iterasi Dasar
print("\n1D Array")
arr_1d = np.array([10, 20, 30])
for x in arr_1d:
    print(x)

print("\n2D Array")
arr_2d = np.array([[1, 2], [3, 4]])
for baris in arr_2d:
    print(baris)

print("\n")
for baris in arr_2d:
    for elemen in baris:
        print(elemen)

## 3.2. Menggunakan `np.nditer()`
print("\nIterasi semua elemen")
arr_2d = np.array([[1, 2], [3, 4]])
for x in np.nditer(arr_2d):
    print(x)

print("\nMengubah nilai saat iterasi")
arr = np.array([1, 2, 3])
for x in np.nditer(arr, op_flags=['readwrite']):
    x[...] = x * 2 # Mengubah nilai elemen di tempat
print(arr)

print("\nIterasi dengan indeks (multi-indeks)")
arr_2d = np.array([[1, 2], [3, 4]])
for indeks, elemen in np.ndenumerate(arr_2d):
    print(f"Indeks: {indeks}, Elemen: {elemen}")
