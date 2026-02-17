# Cara Membuat NumPy Array

## 1. Dari List atau Tuple Python
import numpy as np

# Membuat array 1D dari list
list_1d = [1, 2, 3, 4, 5]
array_1d = np.array(list_1d)
print("Array 1D:", array_1d)

# Membuat array 2D dari list of lists
list_2d = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(list_2d)
print("\nArray 2D:\n", array_2d)

# Membuat array dari tuple
tuple_data = (10, 20, 30)
array_from_tuple = np.array(tuple_data)
print("\nArray dari tuple:", array_from_tuple)

## 2. Menggunakan Fungsi Bawaan NumPy
### `np.zeros()`
# Array 1D berisi nol
zeros_1d = np.zeros(5)
print("\nZeros 1D:", zeros_1d)

# Array 2D berisi nol (3 baris, 4 kolom)
zeros_2d = np.zeros((3, 4))
print("\nZeros 2D:\n", zeros_2d)

### `np.ones()`
# Array 1D berisi satu
ones_1d = np.ones(3)
print("\nOnes 1D:", ones_1d)

# Array 2D berisi satu (2 baris, 2 kolom) dengan tipe data integer
ones_2d_int = np.ones((2, 2), dtype=int)
print("\nOnes 2D (int):\n", ones_2d_int)

### `np.empty()`
# Array kosong 2x3
empty_array = np.empty((2, 3))
print("\nEmpty Array:\n", empty_array)

### `np.arange()`
# Urutan dari 0 hingga 9
arr_range = np.arange(10)
print("\nArange (0-9):", arr_range)

# Urutan dari 2 hingga 10 dengan langkah 2
arr_step = np.arange(2, 11, 2)
print("\nArange (2-10, step 2):", arr_step)

### `np.linspace()`
# 5 angka yang didistribusikan secara merata antara 0 dan 10
arr_linspace = np.linspace(0, 10, 5)
print("\nLinspace (0-10, 5 elemen):", arr_linspace)

### `np.full()`
# Array 2x3 yang diisi dengan angka 7
full_array = np.full((2, 3), 7)
print("\nFull Array (2x3, value 7):\n", full_array)

### `np.eye()`
# Matriks identitas 3x3
identity_matrix = np.eye(3)
print("\nIdentity Matrix (3x3):\n", identity_matrix)

## 3. Tipe Data (Data Types - `dtype`)
# Array dengan tipe data integer 64-bit
int_array = np.array([1, 2, 3], dtype=np.int64)
print("\nInt Array:", int_array, "Dtype:", int_array.dtype)

# Array dengan tipe data float 32-bit
float_array = np.array([1.0, 2.5, 3.7], dtype=np.float32)
print("\nFloat Array:", float_array, "Dtype:", float_array.dtype)

# Array dengan tipe data boolean
bool_array = np.array([True, False, True])
print("\nBoolean Array:", bool_array, "Dtype:", bool_array.dtype)

## 4. Mengubah Bentuk Array (`.reshape()`)
# Array 1D
arr_original = np.arange(1, 10) # [1 2 3 4 5 6 7 8 9]
print("\nOriginal Array:", arr_original)

# Mengubah menjadi array 3x3
arr_reshaped = arr_original.reshape(3, 3)
print("Reshaped Array (3x3):\n", arr_reshaped)

# Mengubah menjadi array 3x3 menggunakan -1 untuk inferensi dimensi
arr_reshaped_infer = arr_original.reshape(3, -1)
print("Reshaped Array (3x-1):\n", arr_reshaped_infer)