# Belajar NumPy: Solusi Persamaan Linear

## Pendahuluan
Persamaan linear adalah persamaan aljabar di mana setiap suku memiliki pangkat satu, dan tidak ada perkalian antar variabel. Dalam konteks analisis data dan matematika, seringkali kita perlu menyelesaikan sistem persamaan linear untuk menemukan nilai variabel yang tidak diketahui. Video ini menjelaskan cara menyelesaikan persamaan linear menggunakan pustaka NumPy di Python.

Tujuan utama dalam menyelesaikan persamaan linear adalah menemukan nilai variabel (misalnya $X_1, X_2$) ketika kita mengetahui hasil (misalnya $Y_1, Y_2$) dan koefisien dari variabel tersebut.

## Representasi Persamaan Linear dalam Bentuk Matriks
Sistem persamaan linear dapat direpresentasikan dalam bentuk matriks, yang memudahkan penyelesaiannya menggunakan operasi matriks.

### Contoh Sistem Persamaan Linear
Diberikan dua persamaan linear sebagai berikut:
1.  $Y_1 = 2X_1 + 3X_2$
2.  $Y_2 = 1X_1 + 2X_2$

Jika diketahui $X_1 = 4$ dan $X_2 = 5$, maka nilai $Y_1$ dan $Y_2$ adalah:
*   $Y_1 = (2 \times 4) + (3 \times 5) = 8 + 15 = 23$
*   $Y_2 = (1 \times 4) + (2 \times 5) = 4 + 10 = 14$

### Transformasi ke Bentuk Matriks $AX = Y$
Sistem persamaan di atas dapat direpresentasikan dalam bentuk matriks $AX = Y$, di mana:
*   **Matriks Koefisien ($A$)**: Berisi koefisien dari variabel $X_1$ dan $X_2$.
*   **Matriks Variabel ($X$)**: Berisi variabel yang tidak diketahui ($X_1, X_2$).
*   **Matriks Hasil ($Y$)**: Berisi nilai hasil dari persamaan ($Y_1, Y_2$).

Dari contoh di atas, representasi matriksnya adalah:
$$
\begin{bmatrix} Y_1 \\ Y_2 \end{bmatrix} = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix} \begin{bmatrix} X_1 \\ X_2 \end{bmatrix}
$$
Sehingga:
*   $A = \begin{bmatrix} 2 & 3 \\ 1 & 2 \end{bmatrix}$
*   $X = \begin{bmatrix} X_1 \\ X_2 \end{bmatrix}$
*   $Y = \begin{bmatrix} Y_1 \\ Y_2 \end{bmatrix}$

Dalam kasus penyelesaian persamaan linear, kita biasanya mengetahui matriks $A$ dan $Y$, dan ingin mencari matriks $X$.

## Penyelesaian Persamaan Linear dengan NumPy
NumPy menyediakan dua metode utama untuk menyelesaikan sistem persamaan linear.

### Metode 1: Menggunakan Inverse Matriks
Jika $AX = Y$, maka untuk mencari $X$, kita dapat mengalikan kedua sisi dengan invers dari $A$ ($A^{-1}$), sehingga $X = A^{-1}Y$.

#### Langkah-langkah di NumPy:
1.  **Definisikan Matriks A dan Y**: Gunakan `np.array()` untuk membuat matriks koefisien dan matriks hasil. Matriks $Y$ harus dalam bentuk kolom (vertikal).
    ```python
    import numpy as np

    A = np.array([[2, 3],
                  [1, 2]]) # Matriks koefisien

    Y = np.array([[23],
                  [14]]) # Matriks hasil
    ```
2.  **Hitung Inverse Matriks A**: Gunakan fungsi `np.linalg.inv()` untuk menghitung invers dari matriks $A$.
    ```python
    A_inverse = np.linalg.inv(A)
    ```
3.  **Kalikan Inverse A dengan Y**: Gunakan fungsi `np.dot()` untuk perkalian matriks $A^{-1}$ dengan $Y$ untuk mendapatkan $X$.
    ```python
    X = np.dot(A_inverse, Y)
    print(X)
    ```
#### Output:
Hasil dari `print(X)` akan menunjukkan nilai $X_1$ dan $X_2$:
```
[[4.]
 [5.]]
```
Ini berarti $X_1 = 4$ dan $X_2 = 5$, yang sesuai dengan nilai awal yang kita gunakan untuk menghitung $Y_1$ dan $Y_2$.

### Metode 2: Menggunakan `np.linalg.solve()`
NumPy menyediakan fungsi yang lebih ringkas dan efisien, `np.linalg.solve()`, yang secara langsung menyelesaikan sistem persamaan linear tanpa perlu menghitung invers secara eksplisit. Fungsi ini juga lebih stabil secara numerik untuk beberapa kasus.

#### Langkah-langkah di NumPy:
1.  **Definisikan Matriks A dan Y**: Sama seperti metode pertama.
    ```python
    import numpy as np

    A = np.array([[2, 3],
                  [1, 2]])

    Y = np.array([[23],
                  [14]])
    ```
2.  **Gunakan `np.linalg.solve()`**: Masukkan matriks $A$ dan $Y$ sebagai argumen.
    ```python
    X_solve = np.linalg.solve(A, Y)
    print(X_solve)
    ```
#### Output:
Hasil dari `print(X_solve)` akan sama dengan metode inverse:
```
[[4.]
 [5.]]
```
Ini juga menghasilkan $X_1 = 4$ dan $X_2 = 5$.

## Perbandingan Kedua Metode
Kedua metode menghasilkan solusi yang sama untuk sistem persamaan linear:
*   **Metode Inverse**: Melibatkan dua langkah terpisah (menghitung invers, lalu perkalian matriks). Ini memberikan pemahaman yang lebih jelas tentang dasar matematika di baliknya ($X = A^{-1}Y$).
*   **Metode `np.linalg.solve()`**: Lebih ringkas dan seringkali lebih disukai karena efisiensi komputasi dan stabilitas numeriknya, terutama untuk matriks besar atau ill-conditioned.

Pilihan metode tergantung pada kebutuhan spesifik dan preferensi pengguna.