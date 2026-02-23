# Catatan Belajar NumPy: Invers dan Determinan Matriks

Catatan ini membahas konsep dasar invers matriks dan determinan, serta implementasinya menggunakan pustaka NumPy di Python. Pemahaman tentang kedua konsep ini sangat penting dalam aljabar linear dan aplikasi komputasi, termasuk untuk menyelesaikan sistem persamaan linear.

## 1. Invers Matriks

**Invers matriks** adalah kebalikan dari suatu matriks. Jika kita memiliki matriks $A$, inversnya dilambangkan dengan $A^{-1}$.

### 1.1. Konsep Dasar Invers

Secara analogi dengan bilangan skalar, jika kita memiliki bilangan $A = 5$, maka inversnya adalah $A^{-1} = 1/5$. Ketika $A$ dikalikan dengan $A^{-1}$, hasilnya adalah 1 ($5 \times 1/5 = 1$).

Pada matriks, konsepnya serupa: jika matriks $A$ dikalikan dengan inversnya $A^{-1}$, hasilnya adalah **matriks satuan** (atau **matriks identitas**).

### 1.2. Matriks Satuan (Matriks Identitas)

**Matriks satuan** adalah matriks persegi di mana semua elemen pada diagonal utamanya bernilai 1, dan elemen lainnya bernilai 0. Contoh matriks satuan 2x2 adalah:
$$
I = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}
$$
Jadi, untuk membuktikan bahwa suatu matriks adalah invers dari matriks lain, hasil perkalian kedua matriks tersebut haruslah matriks satuan.

### 1.3. Kondisi Keberadaan Invers

Tidak semua matriks memiliki invers. Matriks tidak memiliki invers jika determinannya bernilai nol. Matriks yang tidak memiliki invers disebut **matriks singular**. Ini mirip dengan pembagian dengan nol pada bilangan skalar, yang menghasilkan nilai tak terdefinisi.

### 1.4. Menghitung Invers Matriks dengan NumPy

NumPy menyediakan fungsi untuk menghitung invers matriks melalui sub-modul `linalg` (linear algebra).

*   **Langkah-langkah**:
    1.  Import pustaka NumPy.
    2.  Definisikan matriks sebagai `np.array`.
    3.  Gunakan `np.linalg.inv()` untuk menghitung invers.

*   **Contoh Kode**:
    ```python
    import numpy as np

    A = np.array([[1, -1],
                  [1,  1]])
    print("Matriks A:\n", A)

    # Menghitung invers matriks A
    A_inverse = np.linalg.inv(A) #
    print("\nInvers Matriks A:\n", A_inverse)
    ```

### 1.5. Verifikasi Invers Matriks

Untuk memverifikasi bahwa `A_inverse` benar-benar invers dari `A`, kita dapat mengalikan kedua matriks tersebut menggunakan **perkalian dot product** (`np.dot()`). Hasilnya harus mendekati matriks satuan.

*   **Contoh Kode Verifikasi**:
    ```python
    # Verifikasi dengan dot product
    hasil_perkalian = np.dot(A, A_inverse) #
    print("\nHasil A * A_inverse:\n", hasil_perkalian)
    ```
    Output yang diharapkan adalah matriks satuan (misalnya, `[[1. 0.], [0. 1.]]`).

## 2. Determinan Matriks

**Determinan** adalah nilai skalar yang dapat dihitung dari elemen-elemen matriks persegi. Determinan seringkali dianggap sebagai "nilai" dari matriks.

### 2.1. Hubungan Determinan dengan Invers

Matriks yang dapat di-inverse (non-singular) pasti memiliki determinan yang **bukan nol**. Jika determinan suatu matriks adalah nol, maka matriks tersebut tidak memiliki invers.

### 2.2. Menghitung Determinan Matriks dengan NumPy

Sama seperti invers, NumPy menyediakan fungsi untuk menghitung determinan melalui `np.linalg.det()`.

*   **Langkah-langkah**:
    1.  Definisikan matriks.
    2.  Gunakan `np.linalg.det()` untuk menghitung determinannya.

*   **Contoh Kode**:
    ```python
    # Menghitung determinan matriks A
    det_A = np.linalg.det(A) #
    print("\nDeterminan Matriks A:", det_A)
    ```

### 2.3. Determinan Invers Matriks

Determinan dari invers suatu matriks memiliki hubungan khusus dengan determinan matriks aslinya:
$$
\det(A^{-1}) = \frac{1}{\det(A)}
$$
Ini berarti jika $\det(A) = 2$, maka $\det(A^{-1}) = 0.5$.

*   **Contoh Kode Determinan Invers**:
    ```python
    # Menghitung determinan invers matriks A
    det_A_inverse = np.linalg.det(A_inverse) #
    print("Determinan Invers Matriks A:", det_A_inverse)
    ```

## 3. Aplikasi

Invers matriks dan determinan memiliki banyak kegunaan dalam matematika dan ilmu komputer, salah satunya adalah untuk **menyelesaikan sistem persamaan linear**.