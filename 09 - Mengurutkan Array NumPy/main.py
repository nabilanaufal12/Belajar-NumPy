# Metode `np.sort()`
import numpy as np

## Mengurutkan Array 1D
arr_1d = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_arr_1d = np.sort(arr_1d)
print("sorted_arr_1d:", sorted_arr_1d)

## Mengurutkan Array Multi-dimensi
### Mengurutkan Sepanjang Sumbu Terakhir (`axis=-1` atau default)
arr_2d = np.array([[3, 1, 2],
                   [6, 5, 4],
                   [9, 8, 7]])

# Mengurutkan sepanjang sumbu terakhir (baris)
sorted_arr_2d_default = np.sort(arr_2d)
print("\nsorted_arr_2d_default:")
print(sorted_arr_2d_default)

### Mengurutkan Sepanjang Sumbu 0 (`axis=0`)
arr_2d = np.array([[3, 1, 2],
                   [6, 5, 4],
                   [9, 8, 7]])

# Mengurutkan sepanjang sumbu 0 (kolom)
sorted_arr_2d_axis0 = np.sort(arr_2d, axis=0)
print("\nsorted_arr_2d_axis0:")
print(sorted_arr_2d_axis0)

arr_2d_b = np.array([[9, 1, 7],
                     [3, 5, 2],
                     [6, 8, 4]])

# Mengurutkan sepanjang sumbu 0 (kolom)
sorted_arr_2d_axis0_b = np.sort(arr_2d_b, axis=0)
print("\nsorted_arr_2d_axis0_b:")
print(sorted_arr_2d_axis0_b)

### Mengurutkan Sepanjang Sumbu 1 (`axis=1`)
arr_2d_c = np.array([[9, 1, 7],
                     [3, 5, 2],
                     [6, 8, 4]])

# Mengurutkan sepanjang sumbu 1 (baris)
sorted_arr_2d_axis1_c = np.sort(arr_2d_c, axis=1)
print("\nsorted_arr_2d_axis1_c:")
print(sorted_arr_2d_axis1_c)


# Metode `.sort()` (In-place)
arr_inplace = np.array([5, 2, 8, 1, 9])
print("\nArray sebelum diurutkan:", arr_inplace)

arr_inplace.sort()
print("Array setelah diurutkan:", arr_inplace)


# Fungsi `np.argsort()`
arr_args = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_indices = np.argsort(arr_args)
print("\nIndeks yang diurutkan:", sorted_indices)

# Menggunakan indeks untuk mendapatkan array yang diurutkan
sorted_arr_from_indices = arr_args[sorted_indices]
print("Array yang diurutkan:", sorted_arr_from_indices)

## Penggunaan pada Array Multi-dimensi
arr_2d_args = np.array([[3, 1, 2],
                        [6, 5, 4],
                        [9, 8, 7]])

# Mengurutkan indeks sepanjang sumbu terakhir (baris)
sorted_indices_2d = np.argsort(arr_2d_args)
print("\nIndeks yang diurutkan (axis=-1):")
print(sorted_indices_2d)

# Mengurutkan indeks sepanjang sumbu 0 (kolom)
sorted_indices_2d_axis0 = np.argsort(arr_2d_args, axis=0)
print("Indeks yang diurutkan (axis=0):")
print(sorted_indices_2d_axis0)


# Urutan Pengurutan (Order)
arr_desc = np.array([3, 1, 4, 1, 5])
sorted_desc = np.sort(arr_desc)[::-1]
print("\nSorted in descending order:")
print(sorted_desc)

arr_desc_args = np.array([3, 1, 4, 1, 5])
sorted_indices_desc = np.argsort(arr_desc_args)[::-1]
sorted_arr_desc_from_indices = arr_desc_args[sorted_indices_desc]
print("Array yang diurutkan secara descending:")
print(sorted_arr_desc_from_indices)