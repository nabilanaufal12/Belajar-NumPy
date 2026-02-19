# Belajar NumPy: Indexing, Slicing, dan Iterasi

## Pendahuluan

NumPy (Numerical Python) adalah pustaka fundamental dalam Python untuk komputasi ilmiah, terutama dalam bekerja dengan array multidimensional. Memahami cara **indexing (pengindeksan)**, **slicing (pemotongan)**, dan **iterasi (perulangan)** pada array NumPy sangat penting untuk manipulasi data yang efisien dan analisis data. Operasi-operasi ini memungkinkan kita untuk mengakses, memodifikasi, dan memproses bagian-bagian spesifik dari array.

## 1. Indexing (Pengindeksan)

Pengindeksan adalah proses mengakses elemen individual atau sekelompok elemen dalam array menggunakan indeksnya. NumPy mendukung pengindeksan yang kaya dan fleksibel.

### 1.1. Pengindeksan Satu Dimensi (1D Array)

Untuk array satu dimensi, pengindeksan mirip dengan list Python. Indeks dimulai dari 0.

*   **Mengakses elemen tunggal**: Menggunakan indeks integer positif atau negatif.
    ```python
    import numpy as np
    arr_1d = np.array([10, 20, 30, 40, 50])
    print(arr_1d[0])  # Output: 10
    print(arr_1d[3])  # Output: 40
    print(arr_1d[-1]) # Output: 50 (elemen terakhir)
    ```

### 1.2. Pengindeksan Multi-Dimensi (2D, 3D Array, dst.)

Untuk array multi-dimensi (misalnya, matriks 2D), pengindeksan dilakukan dengan menyediakan indeks untuk setiap dimensi, dipisahkan oleh koma. Format umumnya adalah `array[baris, kolom]`.

*   **Mengakses elemen tunggal**:
    ```python
    arr_2d = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    print(arr_2d[0, 0]) # Output: 1 (elemen di baris 0, kolom 0)
    print(arr_2d[1, 2]) # Output: 6 (elemen di baris 1, kolom 2)
    ```
*   **Mengakses seluruh baris**: Cukup berikan indeks baris.
    ```python
    print(arr_2d[0])    # Output: [1 2 3] (seluruh baris 0)
    ```
*   **Mengakses seluruh kolom**: Menggunakan operator slice `:` untuk baris dan indeks spesifik untuk kolom.
    ```python
    print(arr_2d[:, 1]) # Output: [2 5 8] (seluruh kolom 1)
    ```

### 1.3. Pengindeksan Boolean (Boolean Indexing)

Pengindeksan Boolean memungkinkan pemilihan elemen berdasarkan kondisi logis. Ini sangat berguna untuk memfilter data.

*   **Contoh**: Memilih semua elemen yang lebih besar dari 5.
    ```python
    arr = np.array([1, 7, 3, 9, 2, 8])
    kondisi = (arr > 5)
    print(kondisi)      # Output: [False  True False  True False  True]
    print(arr[kondisi]) # Output: [7 9 8] (elemen yang memenuhi kondisi)
    ```
    Ini juga dapat ditulis lebih ringkas:
    ```python
    print(arr[arr > 5]) # Output: [7 9 8]
    ```

### 1.4. Pengindeksan Integer (Fancy Indexing)

Pengindeksan integer memungkinkan pemilihan elemen non-berurutan menggunakan array atau list indeks.

*   **Contoh**: Memilih elemen pada indeks 0, 2, dan 4.
    ```python
    arr_1d = np.array([10, 20, 30, 40, 50])
    indeks = [0, 2, 4]
    print(arr_1d[indeks]) # Output: [10 30 50]
    ```
*   **Untuk 2D array**:
    ```python
    arr_2d = np.array([[1, 2, 3],
                       [4, 5, 6],
                       [7, 8, 9]])
    # Memilih elemen (0,0), (1,2), (2,1)
    baris_indeks = np.array([0, 1, 2])
    kolom_indeks = np.array([0, 2, 1])
    print(arr_2d[baris_indeks, kolom_indeks]) # Output: [1 6 8]
    ```

## 2. Slicing (Pemotongan)

Slicing adalah proses mengekstrak sub-array dari array yang lebih besar. Sintaks dasarnya adalah `[start:stop:step]`, di mana `stop` tidak inklusif.

### 2.1. Slicing Satu Dimensi (1D Array)

*   **Dasar**:
    ```python
    arr_1d = np.array([10, 20, 30, 40, 50, 60])
    print(arr_1d[1:4])   # Output: [20 30 40] (indeks 1 sampai sebelum 4)
    print(arr_1d[:3])    # Output: [10 20 30] (dari awal sampai sebelum 3)
    print(arr_1d[2:])    # Output: [30 40 50 60] (dari indeks 2 sampai akhir)
    print(arr_1d[:])     # Output: [10 20 30 40 50 60] (seluruh array)
    ```
*   **Dengan `step`**:
    ```python
    print(arr_1d[::2])   # Output: [10 30 50] (setiap elemen kedua)
    print(arr_1d[1::2])  # Output: [20 40 60] (dimulai dari indeks 1, setiap elemen kedua)
    print(arr_1d[::-1])  # Output: [60 50 40 30 20 10] (membalik array)
    ```

### 2.2. Slicing Multi-Dimensi (2D Array)

Slicing pada array multi-dimensi dilakukan dengan memberikan slice untuk setiap dimensi.

*   **Mengambil sub-matriks**:
    ```python
    arr_2d = np.array([[1, 2, 3, 4],
                       [5, 6, 7, 8],
                       [9, 10, 11, 12],
                       [13, 14, 15, 16]])
    # Mengambil baris 0 dan 1, kolom 1 dan 2
    sub_array = arr_2d[0:2, 1:3]
    print(sub_array)
    # Output:
    # [[2 3]
    #  [6 7]]
    ```
*   **Mengambil semua baris, kolom tertentu**:
    ```python
    print(arr_2d[:, 0]) # Output: [ 1  5  9 13] (kolom pertama)
    ```
*   **Mengambil baris tertentu, semua kolom**:
    ```python
    print(arr_2d[1, :]) # Output: [5 6 7 8] (baris kedua)
    ```
*   **Menggunakan `...` (Ellipsis)**: `...` adalah singkatan untuk `:, :, ...` yang diperlukan untuk mengisi dimensi yang hilang.
    ```python
    arr_3d = np.array([[[1, 2], [3, 4]],
                       [[5, 6], [7, 8]]])
    print(arr_3d[..., 0]) # Output: [[1 3] [5 7]] (mengambil elemen pertama dari dimensi terakhir)
    ```

### 2.3. Perbedaan antara Slicing dan Pengindeksan Fancy

*   **Slicing** menghasilkan *view* dari array asli, yang berarti perubahan pada slice akan memengaruhi array asli.
*   **Pengindeksan Fancy** (menggunakan array indeks) menghasilkan *copy* dari array asli, sehingga perubahan pada hasilnya tidak akan memengaruhi array asli.

## 3. Iterasi (Perulangan)

Iterasi adalah proses mengunjungi setiap elemen dalam array.

### 3.1. Iterasi Dasar

Secara default, perulangan pada array NumPy akan mengiterasi sepanjang dimensi pertama (baris untuk array 2D).

*   **1D Array**:
    ```python
    arr_1d = np.array([10, 20, 30])
    for x in arr_1d:
        print(x)
    # Output:
    # 10
    # 20
    # 30
    ```
*   **2D Array**:
    ```python
    arr_2d = np.array([[1, 2], [3, 4]])
    for baris in arr_2d:
        print(baris)
    # Output:
    # [1 2]
    # [3 4]
    ```
    Untuk mengiterasi elemen individual dalam 2D array, Anda perlu perulangan bersarang:
    ```python
    for baris in arr_2d:
        for elemen in baris:
            print(elemen)
    # Output: 1, 2, 3, 4 (masing-masing pada baris baru)
    ```

### 3.2. Menggunakan `np.nditer()`

Fungsi `np.nditer()` menyediakan cara yang sangat fleksibel dan efisien untuk mengiterasi elemen array, terlepas dari dimensinya. Ini sangat berguna untuk array multi-dimensi yang kompleks.

*   **Iterasi semua elemen**:
    ```python
    arr_2d = np.array([[1, 2], [3, 4]])
    for x in np.nditer(arr_2d):
        print(x)
    # Output:
    # 1
    # 2
    # 3
    # 4
    ```
*   **Mengubah nilai saat iterasi**: Gunakan argumen `op_flags=['readwrite']`.
    ```python
    arr = np.array([1, 2, 3])
    for x in np.nditer(arr, op_flags=['readwrite']):
        x[...] = x * 2 # Mengubah nilai elemen di tempat
    print(arr) # Output: [2 4 6]
    ```
*   **Iterasi dengan indeks (multi-indeks)**: Gunakan `np.ndenumerate()`.
    ```python
    arr_2d = np.array([[1, 2], [3, 4]])
    for indeks, elemen in np.ndenumerate(arr_2d):
        print(f"Indeks: {indeks}, Elemen: {elemen}")
    # Output:
    # Indeks: (0, 0), Elemen: 1
    # Indeks: (0, 1), Elemen: 2
    # Indeks: (1, 0), Elemen: 3
    # Indeks: (1, 1), Elemen: 4
    ```

## Kesimpulan

Pengindeksan, pemotongan, dan iterasi adalah operasi dasar yang memungkinkan manipulasi array NumPy secara efektif. Memahami perbedaan antara pengindeksan dasar, pengindeksan Boolean, pengindeksan fancy, serta cara kerja slicing dan iterasi, sangat penting untuk menulis kode Python yang efisien dan kuat untuk analisis data.