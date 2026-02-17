# NumPy untuk Analisis Data Python: Instalasi dan Pengantar

## Gambaran Umum

NumPy adalah *package* fundamental dalam ekosistem Python untuk komputasi ilmiah dan analisis data. Ia menyediakan objek *array* N-dimensi berkinerja tinggi dan alat untuk bekerja dengan *array* ini. Tutorial ini membahas instalasi NumPy dalam *virtual environment* dan demonstrasi dasar perbedaannya dengan *list* Python standar, terutama dalam operasi matematika.

## Ekosistem Komputasi Ilmiah

Sebelum masuk ke analisis data, *Artificial Intelligence*, atau *Machine Learning* dengan Python, penting untuk memahami *package* yang mendukung komputasi ilmiah.

### Alat Komputasi Ilmiah Tradisional

Secara tradisional, orang yang melakukan komputasi ilmiah sering menggunakan perangkat lunak seperti:
*   **MATLAB**: Perangkat lunak berbayar.
*   **Octave**: Alternatif *open-source* yang mirip dengan MATLAB.
*   **SciLab**: Alternatif *open-source* lain yang mirip dengan MATLAB.
*   **R/RStudio**: Populer untuk statistik dan juga *open-source*.

### *Package* Python untuk Komputasi Ilmiah

Python memiliki beberapa *package* *open-source* yang memungkinkan komputasi ilmiah:
*   **NumPy**: Menyediakan tipe data *array* dasar yang bisa digunakan untuk komputasi ilmiah. Ini adalah fokus utama tutorial ini.
*   **Matplotlib**: Digunakan untuk *plotting* atau visualisasi data.
*   **SymPy**: Untuk matematika simbolik.
*   **SciPy**: *Package* yang lebih lengkap dan mencakup banyak fungsi dari *package* lain.
*   **Scikit-learn**: Untuk *machine learning*.

## Instalasi NumPy dalam *Virtual Environment*

Disarankan untuk menggunakan *virtual environment* agar manajemen *package* lebih rapi dan terisolasi dari instalasi Python utama sistem.

### Membuat dan Mengaktifkan *Virtual Environment*

1.  **Melihat *package* yang terinstal**: Gunakan `pip 3 list` untuk melihat *package* yang sudah ada di sistem.
2.  **Membuat *virtual environment***:
    *   Navigasi ke folder proyek Anda.
    *   Jalankan perintah `python 3 -m venv Env` untuk membuat *virtual environment* bernama `Env`.
3.  **Mengaktifkan *virtual environment***:
    *   Jalankan `Source Env/bin/activate`.
    *   Verifikasi aktivasi dengan `which python` atau `which python 3`; *path* Python harus mengarah ke dalam folder `Env`.
    *   Setelah aktif, perintah `python` akan merujuk pada Python di dalam *virtual environment*.
4.  **Memperbarui PIP**: Setelah mengaktifkan *virtual environment*, disarankan untuk memperbarui `pip` dengan `pip install --upgrade pip`.
5.  **Memeriksa *package* dalam *virtual environment***: Gunakan `pip list` lagi; seharusnya hanya ada `pip` dan `setuptools`.

### Menginstal NumPy

1.  **Instalasi**: Setelah *virtual environment* aktif, instal NumPy dengan perintah `pip install numpy`. Proses ini akan mengunduh dan menginstal *package* NumPy.
2.  **Verifikasi**: Setelah instalasi selesai, jalankan `pip list` untuk memastikan NumPy terdaftar sebagai *package* yang terinstal.

## Penggunaan Dasar NumPy: Perbandingan dengan *List* Python

NumPy memperkenalkan tipe data **array** yang berbeda secara fundamental dari *list* Python standar, terutama dalam cara mereka menangani operasi matematika.

### Membuat *Array* NumPy dan *List* Python

1.  **Mengimpor NumPy**: Dalam kode Python, impor NumPy biasanya dilakukan dengan `import numpy as np`.
2.  **Membuat *array* NumPy**: Gunakan `np.array()` untuk membuat *array* NumPy.
    ```python
    import numpy as np
    A = np.array([1, 2, 3, 4])
    ```
    Ketika dicetak, *array* NumPy akan menampilkan `array([1, 2, 3, 4])`.
3.  **Membuat *list* Python**: *List* Python dibuat dengan kurung siku.
    ```python
    B = [1, 2, 3, 4]
    ```
    Ketika dicetak, *list* Python akan menampilkan `[1, 2, 3, 4]`.

### Perbedaan dalam Operasi Matematika

Perbedaan utama terlihat saat melakukan operasi aritmatika:

*   **NumPy Array**: Ketika sebuah skalar ditambahkan ke *array* NumPy, operasi tersebut diterapkan secara **element-wise** ke setiap komponen *array*.
    ```python
    A = np.array([1, 2, 3, 4])
    A_plus_one = A + 1
    # Hasil: array([2, 3, 4, 5])
    ```
    Ini sangat berguna untuk operasi matematika pada setiap elemen *array*.

*   **Python List**: Ketika sebuah *list* ditambahkan ke *list* Python lain, operasi tersebut melakukan **konkatenasi** (penggabungan *list*).
    ```python
    B = [1, 2, 3, 4]
    B_plus_one = B + [1]
    # Hasil: [1, 2, 3, 4, 1]
    ```
    Untuk melakukan operasi element-wise pada *list* Python, diperlukan *loop* atau *list comprehension*.

## Langkah Selanjutnya

Setelah memahami instalasi dan penggunaan dasar NumPy, tutorial selanjutnya akan membahas operasi matriks dan komputasi lainnya yang biasa dilakukan di MATLAB atau bahasa pemrograman lain, namun menggunakan NumPy di Python.