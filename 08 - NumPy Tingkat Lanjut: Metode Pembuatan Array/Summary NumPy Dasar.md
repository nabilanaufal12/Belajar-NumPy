# NumPy Tingkat Lanjut: Metode Pembuatan Array

Tutorial ini membahas berbagai metode lanjutan untuk membuat array NumPy, melampaui pembuatan array standar. Metode-metode ini memungkinkan kontrol lebih besar atas tipe data, struktur, dan cara array diinisialisasi.

## 1. Membuat Array dengan Tipe Data Spesifik (`dtype`)

Saat membuat array NumPy, kita dapat secara eksplisit menentukan tipe data (data type atau `dtype`) untuk semua elemen di dalamnya. Ini memastikan konsistensi dan efisiensi memori.

*   **Pembuatan Array Standar**: Array dasar dapat dibuat menggunakan `np.array()`.
    ```python
    import numpy as np

    A = np.array([[1, 2, 3], [3, 4, 5]])
    print(A)
    # Output:
    # [[1 2 3]
    #  [3 4 5]]
    ```

*   **Menentukan Tipe Data**: `dtype` dapat ditambahkan sebagai argumen untuk mengonversi semua elemen ke tipe yang diinginkan.
    *   **Integer**: Mengubah semua elemen menjadi integer.
        ```python
        A = np.array([[1, 2, 3], [3, 4, 5]], dtype=int)
        print(A)
        # Output:
        # [[1 2 3]
        #  [3 4 5]]
        ```
    *   **Float**: Mengubah semua elemen menjadi float (bilangan desimal).
        ```python
        A = np.array([[1, 2, 3], [3, 4, 5]], dtype=float)
        print(A)
        # Output:
        # [[1. 2. 3.]
        #  [3. 4. 5.]]
        ```
    *   **Boolean**: Mengubah semua elemen menjadi boolean.
        ```python
        A = np.array([[1, 2, 3], [3, 4, 5]], dtype=bool)
        print(A)
        # Output:
        # [[ True  True  True]
        #  [ True  True  True]]
        ```
*   **Fungsi `dtype`**: Dengan menentukan `dtype`, kita dapat membuat matriks dengan tipe data tertentu sesuai kebutuhan.

## 2. Membuat Array dari Fungsi (`np.fromfunction`)

`np.fromfunction` memungkinkan pembuatan array dengan mengisi elemen-elemennya berdasarkan hasil dari sebuah fungsi yang menerima koordinat (indeks baris dan kolom) sebagai input.

*   **Konsep**: Fungsi ini mengambil sebuah fungsi sebagai argumen pertama, diikuti oleh `shape` (ukuran matriks) dan `dtype`.
*   **Fungsi Kustom**: Fungsi yang diberikan harus menerima dua argumen: indeks baris (`baris` atau `y`) dan indeks kolom (`kolom` atau `x`).
    *   **Contoh Fungsi `kuadrat`**: Mengembalikan kuadrat dari indeks kolom.
        ```python
        def kuadrat(baris, kolom):
            return kolom**2

        # Contoh penggunaan fungsi kuadrat secara langsung
        print(kuadrat(1, 5)) # Output: 25
        ```
*   **Penggunaan `np.fromfunction`**:
    *   **Array 1D (Vector)**: Membuat array 1D dengan 10 elemen, di mana setiap elemen adalah kuadrat dari indeksnya.
        ```python
        B = np.fromfunction(kuadrat, (1, 10), dtype=int)
        print(B)
        # Output:
        # [[ 0  1  4  9 16 25 36 49 64 81]]
        ```
    *   **Array 2D (Matrix)**: Membuat matriks 4x4 di mana setiap elemen adalah hasil penjumlahan indeks baris dan kolomnya.
        ```python
        def jumlah(baris, kolom):
            return baris + kolom

        C = np.fromfunction(jumlah, (4, 4), dtype=float)
        print(C)
        # Output:
        # [[0. 1. 2. 3.]
        #  [1. 2. 3. 4.]
        #  [2. 3. 4. 5.]
        #  [3. 4. 5. 6.]]
        ```

## 3. Membuat Array dari Iterable (`np.fromiter`)

`np.fromiter` digunakan untuk membuat array NumPy dari objek *iterable* (sesuatu yang bisa diulang, seperti list, tuple, atau generator).

*   **Konsep Iterable**: Objek yang elemen-elemennya dapat diakses satu per satu melalui iterasi.
*   **List Comprehension/Generator Expression**: Sering digunakan untuk membuat iterable secara dinamis.
    *   **Contoh**: Membuat iterable yang menghasilkan kuadrat dari angka 0 hingga 4.
        ```python
        iterable_data = (x**2 for x in range(5))
        # Ini adalah generator expression, bukan list comprehension
        # (0, 1, 4, 9, 16)
        ```
*   **Penggunaan `np.fromiter`**:
    *   Membuat array dari `iterable_data` dengan tipe `int`.
        ```python
        D = np.fromiter(iterable_data, dtype=int)
        print(D)
        # Output: [ 0  1  4  9 16]
        ```
    *   **Contoh lain**: Membuat array dengan elemen dikalikan dua.
        ```python
        iterable_data_x2 = (x*2 for x in range(5))
        D_x2 = np.fromiter(iterable_data_x2, dtype=int)
        print(D_x2)
        # Output: [0 2 4 6 8]
        ```

## 4. Membuat Array Multi-Tipe (Structured Array)

NumPy memungkinkan pembuatan array yang elemen-elemennya memiliki tipe data yang berbeda, mirip dengan tabel database atau struktur C. Ini disebut **structured array** atau **multi-type array**.

*   **Tujuan**: Menggabungkan data heterogen (misalnya, string dan integer) dalam satu array.
*   **Data Input**: Data biasanya disiapkan sebagai list of tuples, di mana setiap tuple merepresentasikan satu "record" atau baris data.
    ```python
    data = [
        ("ucup", 150),
        ("otong", 160),
        ("mario", 180)
    ]
    print(data)
    # Output: [('ucup', 150), ('otong', 160), ('mario', 180)]
    ```
*   **Mendefinisikan `dtype` Kustom**: `dtype` untuk structured array didefinisikan sebagai list of tuples, di mana setiap tuple berisi `(nama_field, tipe_data_field)`.
    *   `'S255'` menunjukkan string dengan panjang maksimum 255 karakter.
    ```python
    custom_dtype = [
        ('nama', 'S255'), # Field 'nama' bertipe string max 255 karakter
        ('tinggi', int)    # Field 'tinggi' bertipe integer
    ]
    ```
*   **Pembuatan Array**: Gunakan `np.array()` dengan data dan `dtype` kustom yang telah didefinisikan.
    ```python
    E = np.array(data, dtype=custom_dtype)
    print(E)
    # Output:
    # [(b'ucup', 150) (b'otong', 160) (b'mario', 180)]
    ```
    *   Perhatikan bahwa string disimpan sebagai byte (`b'ucup'`).
*   **Mengakses Elemen**: Elemen dapat diakses berdasarkan indeks atau nama field.
    ```python
    print(E[0]) # Mengakses record pertama
    # Output: (b'ucup', 150)

    print(E['nama']) # Mengakses semua nilai dari field 'nama'
    # Output: [b'ucup' b'otong' b'mario']
    ```