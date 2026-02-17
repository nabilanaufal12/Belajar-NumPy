# Belajar NumPy: Membuat Array

NumPy (Numerical Python) adalah pustaka fundamental dalam Python untuk komputasi numerik, terutama untuk bekerja dengan array multidimensi. Array NumPy lebih efisien dalam penyimpanan dan operasi dibandingkan dengan list Python standar, menjadikannya pilihan utama untuk analisis data dan pembelajaran mesin.

## Mengapa Menggunakan NumPy Array?

Penggunaan array NumPy menawarkan beberapa keuntungan signifikan dibandingkan list Python biasa:
*   **Efisiensi Memori**: Array NumPy menyimpan data secara kontigu di memori, yang mengurangi *overhead* dan memungkinkan akses data yang lebih cepat.
*   **Kecepatan**: Operasi pada array NumPy diimplementasikan dalam C, sehingga jauh lebih cepat daripada iterasi manual pada list Python.
*   **Fungsionalitas**: NumPy menyediakan berbagai fungsi matematika dan operasi *broadcasting* yang kuat, memungkinkan operasi kompleks pada seluruh array dengan mudah.

## Cara Membuat NumPy Array

Ada beberapa cara untuk membuat array NumPy, tergantung pada kebutuhan.

### 1. Dari List atau Tuple Python

Cara paling umum untuk membuat array NumPy adalah dengan mengonversi list atau tuple Python menggunakan fungsi `np.array()`.

```python
import numpy as np

# Membuat array 1D dari list
list_1d = [1, 2, 3, 4, 5]
array_1d = np.array(list_1d)
print("Array 1D:", array_1d)
# Output: Array 1D: [1 2 3 4 5]

# Membuat array 2D dari list of lists
list_2d = [[1, 2, 3], [4, 5, 6]]
array_2d = np.array(list_2d)
print("Array 2D:\n", array_2d)
# Output:
# Array 2D:
#  [[1 2 3]
#  [4 5 6]]

# Membuat array dari tuple
tuple_data = (10, 20, 30)
array_from_tuple = np.array(tuple_data)
print("Array dari tuple:", array_from_tuple)
# Output: Array dari tuple: [10 20 30]
```

### 2. Menggunakan Fungsi Bawaan NumPy

NumPy menyediakan berbagai fungsi untuk membuat array dengan nilai-nilai tertentu atau pola tertentu secara efisien.

#### `np.zeros()`
Membuat array yang diisi dengan nol. Dapat menentukan bentuk (shape) dan tipe data (dtype).

```python
# Array 1D berisi nol
zeros_1d = np.zeros(5)
print("Zeros 1D:", zeros_1d)
# Output: Zeros 1D: [0. 0. 0. 0. 0.]

# Array 2D berisi nol (3 baris, 4 kolom)
zeros_2d = np.zeros((3, 4))
print("Zeros 2D:\n", zeros_2d)
# Output:
# Zeros 2D:
#  [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]
```

#### `np.ones()`
Membuat array yang diisi dengan satu.

```python
# Array 1D berisi satu
ones_1d = np.ones(3)
print("Ones 1D:", ones_1d)
# Output: Ones 1D: [1. 1. 1.]

# Array 2D berisi satu (2 baris, 2 kolom) dengan tipe data integer
ones_2d_int = np.ones((2, 2), dtype=int)
print("Ones 2D (int):\n", ones_2d_int)
# Output:
# Ones 2D (int):
#  [[1 1]
#  [1 1]]
```

#### `np.empty()`
Membuat array tanpa menginisialisasi entri, yang berarti array akan diisi dengan nilai-nilai acak yang ada di memori pada saat itu. Ini lebih cepat daripada `zeros()` atau `ones()` jika nilai akan segera ditimpa.

```python
# Array kosong 2x3
empty_array = np.empty((2, 3))
print("Empty Array:\n", empty_array)
# Output: (Nilai acak, contoh: [[1. 2. 3.] [4. 5. 6.]])
```

#### `np.arange()`
Mirip dengan fungsi `range()` bawaan Python, tetapi mengembalikan array NumPy. Berguna untuk membuat urutan angka.

```python
# Urutan dari 0 hingga 9
arr_range = np.arange(10)
print("Arange (0-9):", arr_range)
# Output: Arange (0-9): [0 1 2 3 4 5 6 7 8 9]

# Urutan dari 2 hingga 10 dengan langkah 2
arr_step = np.arange(2, 11, 2)
print("Arange (2-10, step 2):", arr_step)
# Output: Arange (2-10, step 2): [ 2  4  6  8 10]
```

#### `np.linspace()`
Membuat array dengan jumlah elemen yang ditentukan, didistribusikan secara merata dalam interval yang ditentukan.

```python
# 5 angka yang didistribusikan secara merata antara 0 dan 10
arr_linspace = np.linspace(0, 10, 5)
print("Linspace (0-10, 5 elemen):", arr_linspace)
# Output: Linspace (0-10, 5 elemen): [ 0.   2.5  5.   7.5 10. ]
```

#### `np.full()`
Membuat array dengan bentuk tertentu yang diisi dengan nilai tunggal yang ditentukan.

```python
# Array 2x3 yang diisi dengan angka 7
full_array = np.full((2, 3), 7)
print("Full Array (2x3, value 7):\n", full_array)
# Output:
# Full Array (2x3, value 7):
#  [[7 7 7]
#  [7 7 7]]
```

#### `np.eye()`
Membuat array identitas (matriks identitas) dengan diagonal utama berisi satu dan elemen lainnya nol.

```python
# Matriks identitas 3x3
identity_matrix = np.eye(3)
print("Identity Matrix (3x3):\n", identity_matrix)
# Output:
# Identity Matrix (3x3):
#  [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
```

### 3. Tipe Data (Data Types - `dtype`)

NumPy mendukung berbagai tipe data numerik. Saat membuat array, tipe data dapat ditentukan secara eksplisit menggunakan argumen `dtype`. Jika tidak ditentukan, NumPy akan mencoba menyimpulkan tipe data terbaik berdasarkan nilai yang diberikan.

```python
# Array dengan tipe data integer 64-bit
int_array = np.array([1, 2, 3], dtype=np.int64)
print("Int Array:", int_array, "Dtype:", int_array.dtype)
# Output: Int Array: [1 2 3] Dtype: int64

# Array dengan tipe data float 32-bit
float_array = np.array([1.0, 2.5, 3.7], dtype=np.float32)
print("Float Array:", float_array, "Dtype:", float_array.dtype)
# Output: Float Array: [1.  2.5 3.7] Dtype: float32

# Array dengan tipe data boolean
bool_array = np.array([True, False, True])
print("Boolean Array:", bool_array, "Dtype:", bool_array.dtype)
# Output: Boolean Array: [ True False  True] Dtype: bool
```

### 4. Mengubah Bentuk Array (`.reshape()`)

Array yang sudah ada dapat diubah bentuknya (jumlah baris dan kolom) menggunakan metode `.reshape()`. Jumlah total elemen dalam array harus tetap sama.

```python
# Array 1D
arr_original = np.arange(1, 10) # [1 2 3 4 5 6 7 8 9]
print("Original Array:", arr_original)

# Mengubah menjadi array 3x3
arr_reshaped = arr_original.reshape(3, 3)
print("Reshaped Array (3x3):\n", arr_reshaped)
# Output:
# Reshaped Array (3x3):
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

# Mengubah menjadi array 3x3 menggunakan -1 untuk inferensi dimensi
arr_reshaped_infer = arr_original.reshape(3, -1)
print("Reshaped Array (3x-1):\n", arr_reshaped_infer)
# Output:
# Reshaped Array (3x-1):
#  [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
```