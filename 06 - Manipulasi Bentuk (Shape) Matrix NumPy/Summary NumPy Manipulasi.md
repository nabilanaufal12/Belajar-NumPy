# Manipulasi Bentuk (Shape) Matrix NumPy

Tutorial ini membahas berbagai metode untuk memanipulasi bentuk (shape) matrix menggunakan library NumPy di Python, termasuk transpose, flatten (ravel), reshape, dan resize. Pemahaman manipulasi bentuk sangat penting dalam analisis data dan machine learning untuk mempersiapkan data sesuai kebutuhan model.

## Inisialisasi Matrix Awal

Pertama, kita akan membuat sebuah matrix contoh untuk demonstrasi. Matrix ini akan memiliki ukuran 2x3 (2 baris, 3 kolom).

*   **Matrix A**:
    ```python
    import numpy as np

    A = np.array([[1, 2, 3],
                  [4, 5, 6]])
    ```
*   **Bentuk (Shape) Matrix A**: `A.shape` akan menghasilkan `(2, 3)`, menunjukkan 2 baris dan 3 kolom.

## Transpose Matrix

**Transpose matrix** adalah operasi yang mengubah baris menjadi kolom dan kolom menjadi baris. Elemen-elemen matrix diputar sedemikian rupa sehingga elemen `(i, j)` menjadi `(j, i)`.

*   **Cara Kerja**: Jika matrix awal `A` berukuran `(m, n)`, maka matrix transpose `A^T` akan berukuran `(n, m)`. Contoh, baris `[1, 2, 3]` akan menjadi kolom pertama.
*   **Metode Transpose**: NumPy menyediakan beberapa cara untuk melakukan transpose:
    1.  **Metode `.transpose()`**: `A.transpose()`
    2.  **Fungsi `np.transpose()`**: `np.transpose(A)`
    3.  **Properti `.T` (Getter/Setter)**: `A.T`
*   **Contoh Output**:
    ```
    [[1 4]
     [2 5]
     [3 6]]
    ```
*   **Penting**: Operasi transpose **tidak mengubah** matrix `A` asli. Ia mengembalikan matrix baru yang sudah ditranspose.

## Flatten Matrix (Ravel)

**Flatten matrix** adalah operasi yang mengubah matrix multidimensi menjadi vektor satu dimensi (baris). Semua elemen matrix dijajarkan secara berurutan.

*   **Cara Kerja**: Semua elemen dari baris pertama diikuti oleh elemen dari baris kedua, dan seterusnya, membentuk satu baris panjang.
*   **Metode Flatten**:
    1.  **Metode `.ravel()`**: `A.ravel()`
    2.  **Fungsi `np.ravel()`**: `np.ravel(A)`
*   **Contoh Output**:
    ```
    [1 2 3 4 5 6]
    ```
*   **Penting**: Operasi flatten **tidak mengubah** matrix `A` asli. Ia mengembalikan array baru yang sudah di-flatten.

## Reshape Matrix

**Reshape matrix** adalah operasi yang mengubah bentuk matrix menjadi dimensi baru tanpa mengubah jumlah total elemen.

*   **Cara Kerja**: Jumlah total elemen dalam matrix harus tetap sama sebelum dan sesudah reshape. Jika matrix awal `A` berukuran `(2, 3)` (total 6 elemen), kita bisa mengubahnya menjadi `(3, 2)` (total 6 elemen) atau `(6, 1)` (total 6 elemen).
*   **Metode Reshape**: `A.reshape(new_rows, new_cols)`
*   **Perbedaan dengan Transpose**: Reshape mengubah urutan elemen untuk menyesuaikan bentuk baru secara berurutan (baris demi baris), sedangkan transpose memutar elemen.
    *   **Transpose**: `[[1,2,3],[4,5,6]]` menjadi `[[1,4],[2,5],[3,6]]`
    *   **Reshape (2x3 ke 3x2)**: `[[1,2,3],[4,5,6]]` menjadi `[[1,2],[3,4],[5,6]]`
*   **Contoh Output (reshape ke 3x2)**:
    ```
    [[1 2]
     [3 4]
     [5 6]]
    ```
*   **Contoh Output (reshape ke 6x1)**:
    ```
    [[1]
     [2]
     [3]
     [4]
     [5]
     [6]]
    ```
*   **Penting**: Operasi reshape **tidak mengubah** matrix `A` asli. Ia mengembalikan matrix baru dengan bentuk yang diubah.

## Resize Matrix

**Resize matrix** adalah operasi yang mengubah bentuk matrix dan **memodifikasi matrix asli secara in-place**. Ini adalah perbedaan krusial dibandingkan dengan `transpose`, `ravel`, dan `reshape`.

*   **Cara Kerja**: Mirip dengan reshape dalam hal mengubah dimensi, tetapi `resize` langsung memodifikasi objek matrix yang dipanggil. Jika jumlah elemen baru berbeda dari jumlah elemen asli, NumPy akan menambahkan elemen nol atau memotong elemen yang berlebih (tergantung implementasi dan versi NumPy).
*   **Metode Resize**: `A.resize(new_rows, new_cols)`
*   **Output `A.resize()`**: Ketika `A.resize()` dipanggil, ia mengembalikan `None` karena operasi dilakukan secara in-place pada `A`.
*   **Dampak pada Matrix Asli**: Setelah `A.resize(3, 2)` dipanggil, jika kita mencetak `A`, bentuknya akan berubah menjadi `(3, 2)`.
*   **Contoh Output (setelah `A.resize(3, 2)` dan mencetak `A`)**:
    ```
    [[1 2]
     [3 4]
     [5 6]]
    ```
*   **Penting**: `resize` **mengubah matrix `A` asli secara permanen**.

## Perbandingan Utama

| Operasi    | Deskripsi                                                                                              | Mengubah Matrix Asli? | Mengembalikan Nilai? |
| :--------- | :----------------------------------------------------------------------------------------------------- | :-------------------- | :------------------- |
| **Transpose** | Memutar baris menjadi kolom dan kolom menjadi baris.                                                   | Tidak                 | Matrix baru          |
| **Flatten** | Mengubah matrix menjadi array 1D.                                                                      | Tidak                 | Array 1D baru        |
| **Reshape** | Mengubah bentuk matrix ke dimensi baru dengan jumlah elemen yang sama, menjaga urutan elemen secara berurutan. | Tidak                 | Matrix baru          |
| **Resize** | Mengubah bentuk matrix ke dimensi baru. **Memodifikasi matrix asli secara in-place.**                  | Ya                    | `None`               |

Penting untuk memahami perbedaan ini, terutama antara `reshape` dan `resize`, untuk menghindari efek samping yang tidak diinginkan pada data Anda.