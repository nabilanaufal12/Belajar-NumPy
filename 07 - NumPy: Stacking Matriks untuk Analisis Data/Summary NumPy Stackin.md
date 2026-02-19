# NumPy: Stacking Matriks untuk Analisis Data

## Pengantar Stacking Matriks

**Stacking** dalam NumPy adalah operasi yang menggabungkan dua atau lebih array (matriks) menjadi satu array yang lebih besar. Proses ini sangat penting dalam analisis data untuk mengorganisir dan memanipulasi data yang berasal dari berbagai sumber atau yang perlu digabungkan untuk pemrosesan lebih lanjut. NumPy menyediakan beberapa fungsi untuk melakukan stacking, masing-masing dengan tujuan yang berbeda.

Fungsi-fungsi utama untuk stacking meliputi:
*   `np.vstack()`: Stacking secara vertikal (baris demi baris).
*   `np.hstack()`: Stacking secara horizontal (kolom demi kolom).
*   `np.stack()`: Stacking sepanjang sumbu baru.
*   `np.dstack()`: Stacking sepanjang sumbu kedalaman (depth).

## Stacking Vertikal (`np.vstack()`)

Fungsi `np.vstack()` digunakan untuk menggabungkan array secara vertikal, yaitu menumpuk array satu di atas yang lain. Ini berarti array-array yang digabungkan harus memiliki jumlah kolom yang sama.

*   **Tujuan**: Menggabungkan array sebagai baris-baris baru.
*   **Syarat**: Semua array input harus memiliki jumlah kolom yang sama.
*   **Contoh Konseptual**: Jika Anda memiliki dua matriks 2x3, `np.vstack()` akan menghasilkan matriks 4x3.

```python
import numpy as np

# Contoh array
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

# Stacking vertikal
c = np.vstack((a, b))
# Hasil:
# [[ 1,  2,  3],
#  [ 4,  5,  6],
#  [ 7,  8,  9],
#  [10, 11, 12]]
```

## Stacking Horizontal (`np.hstack()`)

Fungsi `np.hstack()` digunakan untuk menggabungkan array secara horizontal, yaitu menempatkan array satu di samping yang lain. Ini berarti array-array yang digabungkan harus memiliki jumlah baris yang sama.

*   **Tujuan**: Menggabungkan array sebagai kolom-kolom baru.
*   **Syarat**: Semua array input harus memiliki jumlah baris yang sama.
*   **Contoh Konseptual**: Jika Anda memiliki dua matriks 2x3, `np.hstack()` akan menghasilkan matriks 2x6.

```python
import numpy as np

# Contoh array
a = np.array([[1, 2, 3],
              [4, 5, 6]])

b = np.array([[7, 8, 9],
              [10, 11, 12]])

# Stacking horizontal
c = np.hstack((a, b))
# Hasil:
# [[ 1,  2,  3,  7,  8,  9],
#  [ 4,  5,  6, 10, 11, 12]]
```

## Stacking Sepanjang Sumbu Baru (`np.stack()`)

Fungsi `np.stack()` adalah fungsi stacking yang lebih umum dan fleksibel. Fungsi ini menggabungkan array-array input sepanjang sumbu (axis) baru. Ini berarti array-array yang digabungkan harus memiliki dimensi (shape) yang sama.

*   **Tujuan**: Menggabungkan array dengan menambahkan dimensi baru.
*   **Syarat**: Semua array input harus memiliki dimensi yang sama.
*   **Parameter `axis`**: Menentukan di mana sumbu baru akan ditambahkan.
    *   `axis=0`: Menambahkan sumbu baru di awal (mirip `vstack` untuk array 1D).
    *   `axis=1`: Menambahkan sumbu baru di posisi kedua (mirip `hstack` untuk array 1D).
    *   Untuk array 2D, `axis=0` akan membuat array 3D di mana setiap array input menjadi "slice" pertama, `axis=1` akan membuat array 3D di mana setiap array input menjadi "slice" kedua, dst.

```python
import numpy as np

# Contoh array (harus memiliki shape yang sama)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Stacking sepanjang sumbu baru (axis=0)
c_axis_0 = np.stack((a, b), axis=0)
# Hasil:
# [[1, 2, 3],
#  [4, 5, 6]]
# Shape: (2, 3) - Mirip vstack untuk array 1D

# Stacking sepanjang sumbu baru (axis=1)
c_axis_1 = np.stack((a, b), axis=1)
# Hasil:
# [[1, 4],
#  [2, 5],
#  [3, 6]]
# Shape: (3, 2) - Mirip hstack untuk array 1D

# Contoh dengan array 2D
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])

z = np.stack((x, y), axis=0)
# Hasil:
# [[[1, 2],
#   [3, 4]],
#  [[5, 6],
#   [7, 8]]]
# Shape: (2, 2, 2)
```

## Stacking Kedalaman (`np.dstack()`)

Fungsi `np.dstack()` digunakan untuk menggabungkan array sepanjang sumbu kedalaman (depth). Ini adalah kasus khusus dari `np.stack()` di mana `axis=2` untuk array 2D, atau `axis=1` untuk array 1D setelah diubah menjadi 2D.

*   **Tujuan**: Menggabungkan array dengan menambahkan dimensi ketiga (kedalaman).
*   **Syarat**: Semua array input harus memiliki jumlah baris dan kolom yang sama.
*   **Contoh Konseptual**: Jika Anda memiliki dua matriks 2x3, `np.dstack()` akan menghasilkan matriks 2x3x2. Ini sering digunakan untuk menggabungkan saluran warna (misalnya, R, G, B) menjadi satu gambar.

```python
import numpy as np

# Contoh array
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6],
              [7, 8]])

# Stacking kedalaman
c = np.dstack((a, b))
# Hasil:
# [[[1, 5],
#   [2, 6]],
#  [[3, 7],
#   [4, 8]]]
# Shape: (2, 2, 2)
```

## Ringkasan dan Perbandingan

| Fungsi          | Deskripsi                                                                 | Syarat Input                                   | Perubahan Dimensi (Contoh 2D) |
| :-------------- | :------------------------------------------------------------------------ | :--------------------------------------------- | :---------------------------- |
| `np.vstack()`   | Menggabungkan array secara vertikal (menambah baris).                     | Jumlah kolom harus sama.                       | `(M, N)` + `(P, N)` -> `(M+P, N)` |
| `np.hstack()`   | Menggabungkan array secara horizontal (menambah kolom).                   | Jumlah baris harus sama.                       | `(M, N)` + `(M, P)` -> `(M, N+P)` |
| `np.stack(axis=k)` | Menggabungkan array sepanjang sumbu baru `k`.                           | Dimensi (shape) harus sama.                    | `(M, N)` + `(M, N)` -> `(2, M, N)` (jika `axis=0`) atau `(M, 2, N)` (jika `axis=1`) atau `(M, N, 2)` (jika `axis=2`) |
| `np.dstack()`   | Menggabungkan array sepanjang sumbu kedalaman (axis=2 untuk 2D array).    | Jumlah baris dan kolom harus sama.             | `(M, N)` + `(M, N)` -> `(M, N, 2)` |

Pemilihan fungsi stacking yang tepat tergantung pada bagaimana Anda ingin menggabungkan data dan struktur array yang diinginkan untuk analisis selanjutnya.