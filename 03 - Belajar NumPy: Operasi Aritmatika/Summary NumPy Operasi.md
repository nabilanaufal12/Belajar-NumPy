# Belajar NumPy: Operasi Aritmatika

## Pengantar Operasi Aritmatika NumPy

NumPy adalah pustaka fundamental di Python untuk komputasi numerik, terutama dalam analisis data. Salah satu kekuatan utamanya adalah kemampuannya untuk melakukan operasi aritmatika secara efisien pada array multidimensi. Operasi ini sangat penting untuk manipulasi data, perhitungan statistik, dan berbagai algoritma pembelajaran mesin.

NumPy memungkinkan operasi aritmatika dilakukan secara **element-wise** (berdasarkan elemen) pada array, yang jauh lebih cepat dibandingkan dengan melakukan iterasi melalui list Python standar.

## Membuat Array untuk Demonstrasi

Sebelum melakukan operasi, kita perlu membuat beberapa array NumPy. Array ini bisa berupa satu dimensi (vektor) atau multidimensi (matriks).

```python
import numpy as np

# Array satu dimensi
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])

# Array dua dimensi
matriks_a = np.array([[1, 2], [3, 4]])
matriks_b = np.array([[5, 6], [7, 8]])
```

## Operasi Aritmatika Dasar

NumPy mendukung semua operasi aritmatika dasar yang diterapkan secara element-wise.

### Penjumlahan (`+`)

Penjumlahan dua array NumPy akan menambahkan elemen-elemen pada posisi yang sesuai dari kedua array.

```python
hasil_penjumlahan_1d = a + b
# Output: [11 22 33 44]

hasil_penjumlahan_2d = matriks_a + matriks_b
# Output:
# [[ 6  8]
#  [10 12]]
```

### Pengurangan (`-`)

Pengurangan dua array NumPy akan mengurangi elemen-elemen pada posisi yang sesuai.

```python
hasil_pengurangan_1d = a - b
# Output: [ 9 18 27 36]

hasil_pengurangan_2d = matriks_a - matriks_b
# Output:
# [[-4 -4]
#  [-4 -4]]
```

### Perkalian (`*`)

Perkalian dua array NumPy secara default adalah perkalian element-wise, bukan perkalian matriks.

```python
hasil_perkalian_1d = a * b
# Output: [ 10  40  90 160]

hasil_perkalian_2d = matriks_a * matriks_b
# Output:
# [[ 5 12]
#  [21 32]]
```
Untuk perkalian matriks (dot product), digunakan fungsi `np.dot()` atau operator `@`.

```python
dot_product = matriks_a @ matriks_b
# Output:
# [[19 22]
#  [43 50]]
```

### Pembagian (`/`)

Pembagian dua array NumPy akan membagi elemen-elemen pada posisi yang sesuai.

```python
hasil_pembagian_1d = a / b
# Output: [10.  10.  10.  10.]

hasil_pembagian_2d = matriks_a / matriks_b
# Output:
# [[0.2        0.33333333]
#  [0.42857143 0.5       ]]
```

## Operasi Scalar

NumPy juga memungkinkan operasi antara array dan sebuah nilai tunggal (scalar). Operasi ini akan diterapkan ke setiap elemen dalam array.

```python
array_scalar_penjumlahan = a + 5
# Output: [15 25 35 45]

array_scalar_perkalian = b * 10
# Output: [10 20 30 40]

array_scalar_pembagian = a / 2
# Output: [ 5. 10. 15. 20.]
```

## Operasi Lainnya

### Modulus (`%`)

Operator modulus mengembalikan sisa dari pembagian element-wise.

```python
c = np.array([10, 11, 12, 13])
d = np.array([2, 3, 4, 5])

hasil_modulus = c % d
# Output: [0 2 0 3]
```

### Pangkat (`**`)

Operator pangkat akan memangkatkan setiap elemen array dengan nilai tertentu atau elemen array lain secara element-wise.

```python
hasil_pangkat_scalar = b ** 2
# Output: [ 1  4  9 16]

e = np.array([2, 3, 4, 5])
f = np.array([2, 2, 2, 2])
hasil_pangkat_array = e ** f
# Output: [ 4  9 16 25]
```

### Operasi Perbandingan

Operasi perbandingan seperti `>`, `<`, `==`, `>=`, `<=`, `!=` juga dilakukan secara element-wise dan menghasilkan array boolean.

```python
perbandingan_lebih_besar = a > b
# Output: [ True  True  True  True]

perbandingan_sama_dengan = a == (b * 10)
# Output: [ True  True  True  True]
```

## Broadcasting

**Broadcasting** adalah mekanisme kuat di NumPy yang memungkinkan operasi aritmatika pada array dengan bentuk (shape) yang berbeda. Ini terjadi ketika NumPy secara otomatis "meregangkan" array yang lebih kecil agar sesuai dengan bentuk array yang lebih besar, tanpa perlu membuat salinan data secara eksplisit.

Aturan dasar broadcasting:
1.  Jika array tidak memiliki jumlah dimensi yang sama, bentuk array yang lebih kecil akan ditambahkan dimensi di depannya hingga jumlah dimensinya sama.
2.  Dua dimensi dikatakan kompatibel jika:
    *   Keduanya sama.
    *   Salah satunya adalah 1.
3.  Jika aturan ini tidak terpenuhi, error `ValueError` akan muncul.

Contoh broadcasting:

```python
g = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
h = np.array([10, 20, 30])           # Shape (3,)

hasil_broadcasting = g + h
# Output:
# [[11 22 33]
#  [14 25 36]]
```
Dalam contoh di atas, array `h` (shape `(3,)`) secara otomatis diperluas menjadi `(1, 3)` dan kemudian direplikasi di sepanjang sumbu pertama agar sesuai dengan `g` (shape `(2, 3)`), memungkinkan operasi penjumlahan element-wise.