# Visualisasi Data dengan NumPy dan Matplotlib

## Pendahuluan: NumPy dan Matplotlib untuk Visualisasi Data

NumPy dan Matplotlib adalah dua *package* Python yang sering digunakan bersama untuk analisis dan visualisasi data. NumPy menyediakan kemampuan komputasi numerik yang efisien, sementara Matplotlib memungkinkan pembuatan berbagai jenis plot dan grafik untuk memvisualisasikan hasil perhitungan NumPy.

## Instalasi Matplotlib

Sebelum menggunakan Matplotlib, *package* ini perlu diinstal.
1.  **Memeriksa *package* yang terinstal**: Gunakan perintah `pip list` untuk melihat daftar *package* Python yang sudah ada.
2.  **Menginstal Matplotlib**: Jalankan perintah `pip install matplotlib` di terminal. Proses instalasi memerlukan koneksi internet.
3.  **Verifikasi instalasi**: Setelah instalasi selesai, `pip list` akan menunjukkan Matplotlib beserta dependensinya telah terinstal.

## Mengimpor Pustaka

Untuk menggunakan Matplotlib, impor modul `pyplot` yang umumnya di-*alias* sebagai `plt`:
```python
import numpy as np
import matplotlib.pyplot as plt
```

## Membuat Plot Persamaan Garis Lurus

Contoh visualisasi pertama adalah persamaan garis lurus $y = 2x + 3$.

1.  **Mendefinisikan data X**: Gunakan `np.arange()` untuk membuat *array* nilai $X$ dari 0 hingga 10 dengan *step* 1.
    ```python
    x = np.arange(0, 11, 1) # Hasil: [0, 1, 2, ..., 10]
    ```
2.  **Mendefinisikan data Y**: Hitung nilai $Y$ berdasarkan persamaan garis.
    ```python
    y = 2 * x + 3
    ```
3.  **Membuat plot**: Gunakan fungsi `plt.plot()` dengan $X$ sebagai sumbu horizontal dan $Y$ sebagai sumbu vertikal.
    ```python
    plt.plot(x, y)
    ```
4.  **Menampilkan plot**: Panggil `plt.show()` untuk menampilkan grafik yang telah dibuat.
    ```python
    plt.show()
    ```

## Membuat Plot Lingkaran

Untuk membuat plot lingkaran, kita akan menggunakan koordinat polar yang dikonversi ke koordinat Kartesius.

1.  **Mendefinisikan jari-jari**: Tentukan nilai jari-jari lingkaran.
    ```python
    jari_jari = 5
    ```
2.  **Mendefinisikan sudut**: Gunakan `np.linspace()` untuk membuat *array* sudut dari $0$ hingga $2\pi$ (satu putaran penuh) dengan sejumlah titik tertentu (misalnya, 100 titik) untuk menghasilkan lingkaran yang halus.
    ```python
    sudut = np.linspace(0, 2 * np.pi, 100)
    ```
    *Catatan*: Penggunaan `np.arange()` dengan *step* besar (misalnya, 1) untuk sudut akan menghasilkan plot yang tidak menyerupai lingkaran. `np.linspace()` lebih cocok untuk kasus ini.
3.  **Menghitung koordinat X dan Y**: Gunakan fungsi trigonometri `np.cos()` dan `np.sin()` untuk mengonversi sudut dan jari-jari ke koordinat Kartesius.
    ```python
    x = jari_jari * np.cos(sudut)
    y = jari_jari * np.sin(sudut)
    ```
4.  **Membuat dan menampilkan plot**:
    ```python
    plt.plot(x, y)
    plt.show()
    ```

## Mengelola Beberapa Plot (Figures)

Matplotlib memungkinkan untuk menampilkan beberapa grafik secara terpisah dalam jendela *figure* yang berbeda.

1.  **Membuat *figure* terpisah**: Gunakan `plt.figure()` dengan nomor identifikasi unik untuk setiap *figure*.
    ```python
    # Plot pertama (misalnya, garis lurus)
    plt.figure(1)
    plt.plot(x1, y1) # Asumsikan x1, y1 sudah didefinisikan

    # Plot kedua (misalnya, lingkaran)
    plt.figure(2)
    plt.plot(x2, y2) # Asumsikan x2, y2 sudah didefinisikan
    ```
2.  **Menampilkan semua *figure***: Panggil `plt.show()` sekali di akhir kode untuk menampilkan semua *figure* yang telah dibuat. Ini akan membuka beberapa jendela grafik secara bersamaan.

## Kesimpulan

Tutorial ini menunjukkan dasar-dasar penggunaan NumPy dan Matplotlib untuk visualisasi data sederhana seperti garis lurus dan lingkaran. Kemampuan ini sudah cukup untuk melakukan perhitungan dan memvisualisasikannya, bahkan dapat menggantikan perangkat lunak seperti MATLAB untuk tugas-tugas tertentu.