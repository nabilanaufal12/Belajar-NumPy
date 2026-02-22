# Mengurutkan Array NumPy

## Pendahuluan
Mengurutkan (sorting) array adalah operasi fundamental dalam analisis data yang melibatkan pengaturan elemen-elemen dalam urutan naik (ascending) atau turun (descending). NumPy menyediakan beberapa fungsi dan metode untuk melakukan sorting pada array, baik array satu dimensi (1D) maupun multi-dimensi (nD). Kemampuan untuk mengurutkan data sangat penting untuk mempermudah pencarian, analisis statistik, dan visualisasi data.

## Metode `np.sort()`
Fungsi `np.sort()` adalah cara paling umum untuk mengurutkan array NumPy. Fungsi ini mengembalikan salinan array yang telah diurutkan, tanpa mengubah array asli.

### Mengurutkan Array 1D
Untuk array satu dimensi, `np.sort()` akan mengurutkan semua elemen dari nilai terkecil ke terbesar secara default.

```python
import numpy as np

arr_1d = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_arr_1d = np.sort(arr_1d)
print(sorted_arr_1d)
# Output: [1 1 2 3 4 5 6 9]
```
Array `arr_1d` asli tidak berubah setelah operasi ini.

### Mengurutkan Array Multi-dimensi
Ketika bekerja dengan array multi-dimensi (misalnya, 2D), `np.sort()` memerlukan penentuan **axis** (sumbu) untuk menentukan bagaimana pengurutan akan dilakukan.

#### Mengurutkan Sepanjang Sumbu Terakhir (`axis=-1` atau default)
Secara *default*, `np.sort()` akan mengurutkan elemen sepanjang sumbu terakhir (baris untuk array 2D) jika `axis` tidak ditentukan atau diatur ke `-1`.

```python
arr_2d = np.array([[3, 1, 2],
                   [6, 5, 4],
                   [9, 8, 7]])

# Mengurutkan sepanjang sumbu terakhir (baris)
sorted_arr_2d_default = np.sort(arr_2d)
print(sorted_arr_2d_default)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
```
Setiap baris diurutkan secara independen.

#### Mengurutkan Sepanjang Sumbu 0 (`axis=0`)
Ketika `axis=0`, pengurutan dilakukan sepanjang kolom. Ini berarti elemen-elemen dalam setiap kolom akan diurutkan secara independen.

```python
arr_2d = np.array([[3, 1, 2],
                   [6, 5, 4],
                   [9, 8, 7]])

# Mengurutkan sepanjang sumbu 0 (kolom)
sorted_arr_2d_axis0 = np.sort(arr_2d, axis=0)
print(sorted_arr_2d_axis0)
# Output:
# [[3 1 2]
#  [6 5 4]
#  [9 8 7]]
```
*Koreksi:* Output di atas salah. Jika diurutkan sepanjang `axis=0`, kolom pertama `[3, 6, 9]` akan menjadi `[3, 6, 9]`, kolom kedua `[1, 5, 8]` akan menjadi `[1, 5, 8]`, dan kolom ketiga `[2, 4, 7]` akan menjadi `[2, 4, 7]`. Jadi, hasilnya tetap sama karena kolom-kolom tersebut sudah terurut secara individual. Mari kita gunakan contoh yang lebih jelas.

```python
arr_2d_b = np.array([[9, 1, 7],
                     [3, 5, 2],
                     [6, 8, 4]])

# Mengurutkan sepanjang sumbu 0 (kolom)
sorted_arr_2d_axis0_b = np.sort(arr_2d_b, axis=0)
print(sorted_arr_2d_axis0_b)
# Output:
# [[3 1 2]
#  [6 5 4]
#  [9 8 7]]
```
Pada contoh ini, kolom pertama `[9, 3, 6]` diurutkan menjadi `[3, 6, 9]`, kolom kedua `[1, 5, 8]` menjadi `[1, 5, 8]`, dan kolom ketiga `[7, 2, 4]` menjadi `[2, 4, 7]`.

#### Mengurutkan Sepanjang Sumbu 1 (`axis=1`)
Ketika `axis=1`, pengurutan dilakukan sepanjang baris. Ini adalah perilaku *default* jika `axis` tidak ditentukan untuk array 2D.

```python
arr_2d_c = np.array([[9, 1, 7],
                     [3, 5, 2],
                     [6, 8, 4]])

# Mengurutkan sepanjang sumbu 1 (baris)
sorted_arr_2d_axis1_c = np.sort(arr_2d_c, axis=1)
print(sorted_arr_2d_axis1_c)
# Output:
# [[1 7 9]
#  [2 3 5]
#  [4 6 8]]
```
Setiap baris diurutkan secara independen.

## Metode `.sort()` (In-place)
Selain fungsi `np.sort()`, array NumPy juga memiliki metode `.sort()` yang dapat dipanggil langsung pada objek array. Perbedaan utama adalah bahwa metode `.sort()` akan **mengurutkan array secara in-place**, yang berarti array asli akan dimodifikasi dan tidak ada salinan baru yang dikembalikan. Metode ini mengembalikan `None`.

```python
arr_inplace = np.array([5, 2, 8, 1, 9])
print("Array sebelum diurutkan:", arr_inplace) # Output: [5 2 8 1 9]

arr_inplace.sort()
print("Array setelah diurutkan:", arr_inplace) # Output: [1 2 5 8 9]
```
Metode `.sort()` juga mendukung argumen `axis` untuk array multi-dimensi, bekerja dengan cara yang sama seperti `np.sort()`.

## Fungsi `np.argsort()`
Fungsi `np.argsort()` tidak mengurutkan elemen array secara langsung, melainkan mengembalikan **indeks-indeks** yang akan mengurutkan array tersebut. Ini sangat berguna ketika Anda perlu mengurutkan satu array berdasarkan nilai-nilai di array lain, atau ketika Anda ingin mempertahankan hubungan antara elemen-elemen di beberapa array.

### Penggunaan pada Array 1D
`np.argsort()` akan mengembalikan array indeks yang, jika digunakan untuk mengindeks array asli, akan menghasilkan array yang diurutkan.

```python
arr_args = np.array([3, 1, 4, 1, 5, 9, 2, 6])
sorted_indices = np.argsort(arr_args)
print("Indeks yang diurutkan:", sorted_indices)
# Output: [1 3 6 0 2 4 7 5]

# Menggunakan indeks untuk mendapatkan array yang diurutkan
sorted_arr_from_indices = arr_args[sorted_indices]
print("Array yang diurutkan:", sorted_arr_from_indices)
# Output: [1 1 2 3 4 5 6 9]
```
Indeks `1` dan `3` keduanya menunjuk ke nilai `1` dalam `arr_args`. Indeks `6` menunjuk ke `2`, dan seterusnya.

### Penggunaan pada Array Multi-dimensi
Sama seperti `np.sort()`, `np.argsort()` juga dapat menerima argumen `axis` untuk menentukan sumbu pengurutan.

```python
arr_2d_args = np.array([[3, 1, 2],
                        [6, 5, 4],
                        [9, 8, 7]])

# Mengurutkan indeks sepanjang sumbu terakhir (baris)
sorted_indices_2d = np.argsort(arr_2d_args)
print("Indeks yang diurutkan (axis=-1):\n", sorted_indices_2d)
# Output:
# [[1 2 0]
#  [2 1 0]
#  [2 1 0]]

# Mengurutkan indeks sepanjang sumbu 0 (kolom)
sorted_indices_2d_axis0 = np.argsort(arr_2d_args, axis=0)
print("Indeks yang diurutkan (axis=0):\n", sorted_indices_2d_axis0)
# Output:
# [[0 0 0]
#  [1 1 1]
#  [2 2 2]]
```
Untuk `axis=-1`, baris pertama `[3, 1, 2]` memiliki elemen terkecil di indeks `1` (nilai `1`), lalu indeks `2` (nilai `2`), dan terakhir indeks `0` (nilai `3`), sehingga menghasilkan `[1, 2, 0]`.

## Urutan Pengurutan (Order)
Secara *default*, semua fungsi pengurutan NumPy mengurutkan dalam urutan naik (ascending). Untuk mengurutkan dalam urutan turun (descending), Anda dapat mengurutkan dalam urutan naik lalu membalik hasilnya.

```python
arr_desc = np.array([3, 1, 4, 1, 5])
sorted_desc = np.sort(arr_desc)[::-1]
print(sorted_desc)
# Output: [5 4 3 1 1]
```
Atau, jika menggunakan `argsort()`, Anda bisa membalik indeksnya.

```python
arr_desc_args = np.array([3, 1, 4, 1, 5])
sorted_indices_desc = np.argsort(arr_desc_args)[::-1]
sorted_arr_desc_from_indices = arr_desc_args[sorted_indices_desc]
print(sorted_arr_desc_from_indices)
# Output: [5 4 3 1 1]
```