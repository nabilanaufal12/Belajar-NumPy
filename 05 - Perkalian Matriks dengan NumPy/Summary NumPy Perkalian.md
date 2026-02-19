# Perkalian Matriks dengan NumPy

NumPy adalah pustaka fundamental dalam Python untuk komputasi numerik, terutama dalam operasi array dan matriks. Salah satu operasi penting yang didukungnya adalah perkalian matriks, yang berbeda dari perkalian elemen-demi-elemen.

## Konsep Dasar Matriks

Matriks adalah susunan angka dalam baris (horizontal) dan kolom (vertikal). Ukuran matriks dinyatakan sebagai $m \times n$, di mana $m$ adalah jumlah baris dan $n$ adalah jumlah kolom.

### Aturan Perkalian Matriks

Untuk mengalikan dua matriks, misalnya matriks $A$ dan matriks $B$, ada aturan dimensi yang harus dipenuhi:
*   Jumlah **kolom** matriks pertama ($A$) harus sama dengan jumlah **baris** matriks kedua ($B$).
*   Jika matriks $A$ berukuran $m \times p$ dan matriks $B$ berukuran $p \times n$, maka hasil perkalian $C = A \times B$ akan berukuran $m \times n$.

Setiap elemen $c_{ij}$ dalam matriks hasil $C$ dihitung dengan menjumlahkan hasil perkalian elemen-elemen dari baris $i$ matriks $A$ dengan kolom $j$ matriks $B$.

Contoh:
Jika $A = \begin{bmatrix} a_{11} & a_{12} & a_{13} \\ a_{21} & a_{22} & a_{23} \end{bmatrix}$ (ukuran $2 \times 3$) dan $B = \begin{bmatrix} b_{11} & b_{12} \\ b_{21} & b_{22} \\ b_{31} & b_{32} \end{bmatrix}$ (ukuran $3 \times 2$),
maka hasil $C$ akan berukuran $2 \times 2$.
Elemen $c_{11}$ dihitung sebagai: $c_{11} = (a_{11} \times b_{11}) + (a_{12} \times b_{21}) + (a_{13} \times b_{31})$.

## Perkalian Matriks di NumPy

NumPy menyediakan beberapa cara untuk melakukan perkalian matriks:

### 1. Operator `@` (Operator Matriks)

Operator `@` adalah cara yang paling intuitif dan direkomendasikan untuk perkalian matriks di Python 3.5 ke atas.

```python
import numpy as np

# Membuat matriks A (2x3)
A = np.array([[1, 2, 3],
              [4, 5, 6]]) # src-1:03:00

# Membuat matriks B (3x2)
B = np.array([[7, 8],
              [9, 10],
              [11, 12]]) # src-1:03:20

# Perkalian matriks menggunakan operator @
C = A @ B
print("Hasil A @ B:\n", C)
# Output:
# [[ 58  64]
#  [139 154]]
```

### 2. Fungsi `np.dot()`

Fungsi `np.dot()` dapat digunakan untuk perkalian dot product antara dua array. Untuk matriks 2D, ini akan melakukan perkalian matriks standar.

```python
# Perkalian matriks menggunakan np.dot()
C_dot = np.dot(A, B)
print("Hasil np.dot(A, B):\n", C_dot)
# Output:
# [[ 58  64]
#  [139 154]]
```

Untuk matriks 2D, `np.dot()` dan operator `@` menghasilkan hasil yang sama.

### 3. Fungsi `np.matmul()`

Fungsi `np.matmul()` (matrix multiply) juga melakukan perkalian matriks. Untuk matriks 2D, perilakunya identik dengan `np.dot()` dan operator `@`.

```python
# Perkalian matriks menggunakan np.matmul()
C_matmul = np.matmul(A, B)
print("Hasil np.matmul(A, B):\n", C_matmul)
# Output:
# [[ 58  64]
#  [139 154]]
```

Meskipun `np.dot()`, `np.matmul()`, dan `@` memberikan hasil yang sama untuk matriks 2D, ada perbedaan perilaku saat menangani array dengan dimensi yang lebih tinggi (lebih dari 2D) atau saat berinteraksi dengan skalar. Untuk perkalian matriks standar (2D), operator `@` adalah yang paling direkomendasikan karena kejelasannya.

## Perbedaan dengan Perkalian Element-wise

Penting untuk membedakan antara perkalian matriks (`@`, `np.dot()`, `np.matmul()`) dan perkalian element-wise (`*`).

*   **Perkalian Element-wise (`*`)**: Mengalikan setiap elemen pada posisi yang sama di dua matriks. Ini membutuhkan kedua matriks memiliki dimensi yang persis sama.
*   **Perkalian Matriks (`@`)**: Mengikuti aturan perkalian matriks matematis yang telah dijelaskan sebelumnya, di mana dimensi tengah harus cocok ($m \times p$ dan $p \times n$).

Contoh perkalian element-wise:
```python
# Membuat matriks P (2x2)
P = np.array([[1, 2],
              [3, 4]])

# Membuat matriks Q (2x2)
Q = np.array([[5, 6],
              [7, 8]])

# Perkalian element-wise
R_element_wise = P * Q
print("Hasil P * Q (element-wise):\n", R_element_wise)
# Output:
# [[ 5 12]
#  [21 32]]
```

Jika dimensi matriks tidak cocok untuk perkalian element-wise, NumPy akan menghasilkan error atau melakukan *broadcasting* jika memungkinkan. Untuk perkalian matriks, jika aturan dimensi tidak terpenuhi, NumPy akan menghasilkan `ValueError`.