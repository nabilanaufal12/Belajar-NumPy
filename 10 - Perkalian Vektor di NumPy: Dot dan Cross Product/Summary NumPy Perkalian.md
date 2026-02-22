# Perkalian Vektor di NumPy: Dot dan Cross Product

## Pengantar Perkalian Vektor

Dalam analisis data dan komputasi ilmiah menggunakan Python, NumPy adalah pustaka fundamental yang menyediakan dukungan untuk array dan matriks multi-dimensi, serta fungsi matematika tingkat tinggi untuk mengoperasikannya. Salah satu operasi penting adalah perkalian vektor, yang dapat dibagi menjadi dua jenis utama: **dot product** (produk skalar) dan **cross product** (produk vektor). Kedua operasi ini memiliki definisi, properti, dan aplikasi yang berbeda.

## Dot Product (Produk Skalar)

**Dot product**, juga dikenal sebagai produk skalar, adalah operasi aljabar yang mengambil dua urutan bilangan (biasanya vektor koordinat) dengan panjang yang sama dan mengembalikan satu bilangan tunggal (skalar).

### Definisi dan Properti

Untuk dua vektor $\mathbf{A} = [A_1, A_2, \dots, A_n]$ dan $\mathbf{B} = [B_1, B_2, \dots, B_n]$, dot product didefinisikan sebagai:
$$ \mathbf{A} \cdot \mathbf{B} = \sum_{i=1}^{n} A_i B_i = A_1 B_1 + A_2 B_2 + \dots + A_n B_n $$
Secara geometris, dot product juga dapat didefinisikan sebagai:
$$ \mathbf{A} \cdot \mathbf{B} = ||\mathbf{A}|| \cdot ||\mathbf{B}|| \cdot \cos(\theta) $$
di mana $||\mathbf{A}||$ adalah magnitudo (panjang) vektor $\mathbf{A}$, $||\mathbf{B}||$ adalah magnitudo vektor $\mathbf{B}$, dan $\theta$ adalah sudut antara kedua vektor.

Properti kunci dari dot product meliputi:
*   **Komutatif**: $\mathbf{A} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{A}$
*   **Distributif**: $\mathbf{A} \cdot (\mathbf{B} + \mathbf{C}) = \mathbf{A} \cdot \mathbf{B} + \mathbf{A} \cdot \mathbf{C}$
*   Jika dua vektor tegak lurus (ortogonal), maka dot product mereka adalah nol ($\theta = 90^\circ \implies \cos(\theta) = 0$).

### Implementasi di NumPy

NumPy menyediakan beberapa cara untuk menghitung dot product:

1.  **`numpy.dot()` fungsi**: Ini adalah fungsi umum yang dapat menangani dot product untuk vektor (1D array) maupun perkalian matriks.
    ```python
    import numpy as np

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    dot_product_result = np.dot(v1, v2)
    # Hasil: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32
    print(dot_product_result) # Output: 32
    ```
    `np.dot()` juga dapat digunakan untuk perkalian matriks.

2.  **Operator `@` (Python 3.5+)**: Operator `@` adalah sintaks yang lebih modern dan intuitif untuk perkalian matriks dan dot product vektor.
    ```python
    import numpy as np

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])

    dot_product_result_at = v1 @ v2
    print(dot_product_result_at) # Output: 32
    ```
    Operator `@` secara fungsional setara dengan `np.dot()` untuk vektor 1D.

### Aplikasi

Dot product digunakan dalam berbagai aplikasi, seperti:
*   Menghitung proyeksi satu vektor ke vektor lain.
*   Menentukan sudut antara dua vektor.
*   Menghitung kerja dalam fisika (gaya dikalikan perpindahan).
*   Dalam pembelajaran mesin, untuk menghitung kesamaan antara vektor fitur.

## Cross Product (Produk Vektor)

**Cross product**, juga dikenal sebagai produk vektor, adalah operasi biner pada dua vektor dalam ruang tiga dimensi. Hasil dari cross product adalah vektor lain yang tegak lurus terhadap kedua vektor input.

### Definisi dan Properti

Untuk dua vektor $\mathbf{A} = [A_x, A_y, A_z]$ dan $\mathbf{B} = [B_x, B_y, B_z]$ dalam ruang 3D, cross product $\mathbf{A} \times \mathbf{B}$ didefinisikan sebagai:
$$ \mathbf{A} \times \mathbf{B} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ A_x & A_y & A_z \\ B_x & B_y & B_z \end{vmatrix} = (A_y B_z - A_z B_y)\mathbf{i} - (A_x B_z - A_z B_x)\mathbf{j} + (A_x B_y - A_y B_x)\mathbf{k} $$
Atau dalam bentuk komponen:
$$ \mathbf{A} \times \mathbf{B} = [A_y B_z - A_z B_y, A_z B_x - A_x B_z, A_x B_y - A_y B_x] $$
Magnitudo dari vektor hasil cross product adalah:
$$ ||\mathbf{A} \times \mathbf{B}|| = ||\mathbf{A}|| \cdot ||\mathbf{B}|| \cdot \sin(\theta) $$
di mana $\theta$ adalah sudut antara $\mathbf{A}$ dan $\mathbf{B}$. Arah vektor hasil ditentukan oleh kaidah tangan kanan.

Properti kunci dari cross product meliputi:
*   **Anti-komutatif**: $\mathbf{A} \times \mathbf{B} = -(\mathbf{B} \times \mathbf{A})$
*   **Distributif**: $\mathbf{A} \times (\mathbf{B} + \mathbf{C}) = \mathbf{A} \times \mathbf{B} + \mathbf{A} \times \mathbf{C}$
*   Cross product hanya didefinisikan untuk vektor 3D. Untuk vektor 2D, NumPy dapat menghitung cross product dengan mengasumsikan komponen z adalah nol.
*   Jika dua vektor sejajar atau anti-sejajar, cross product mereka adalah vektor nol ($\theta = 0^\circ \text{ atau } 180^\circ \implies \sin(\theta) = 0$).

### Implementasi di NumPy

NumPy menyediakan fungsi `numpy.cross()` untuk menghitung cross product.

```python
import numpy as np

v1 = np.array([1, 0, 0]) # Vektor di sepanjang sumbu x
v2 = np.array([0, 1, 0]) # Vektor di sepanjang sumbu y

cross_product_result = np.cross(v1, v2)
# Hasil: [0, 0, 1] (Vektor di sepanjang sumbu z, sesuai kaidah tangan kanan)
print(cross_product_result) # Output: [0 0 1]

v3 = np.array([1, 2, 3])
v4 = np.array([4, 5, 6])

cross_product_result_2 = np.cross(v3, v4)
# Hasil: [(2*6 - 3*5), (3*4 - 1*6), (1*5 - 2*4)] = [12-15, 12-6, 5-8] = [-3, 6, -3]
print(cross_product_result_2) # Output: [-3  6 -3]
```
Untuk vektor 2D, `np.cross()` akan mengembalikan skalar yang merupakan komponen z dari cross product 3D yang dihasilkan (dengan asumsi komponen z dari vektor input adalah nol).

```python
v5 = np.array([1, 0])
v6 = np.array([0, 1])

cross_product_2d = np.cross(v5, v6)
print(cross_product_2d) # Output: 1 (mewakili [0, 0, 1] dalam 3D)
```

### Aplikasi

Cross product digunakan dalam berbagai bidang, termasuk:
*   Menghitung momen gaya (torque) dalam fisika.
*   Menemukan vektor normal ke bidang yang dibentuk oleh dua vektor.
*   Menghitung luas jajaran genjang yang dibentuk oleh dua vektor.
*   Dalam grafika komputer, untuk menentukan orientasi permukaan.

## Perbandingan Dot Product dan Cross Product

| Fitur              | Dot Product ($\mathbf{A} \cdot \mathbf{B}$)                               | Cross Product ($\mathbf{A} \times \mathbf{B}$)                                 |
| :----------------- | :------------------------------------------------------------------------ | :----------------------------------------------------------------------------- |
| **Tipe Hasil**     | Skalar (satu bilangan)                                                    | Vektor                                                                         |
| **Dimensi Input**  | Vektor dengan dimensi yang sama (umumnya $n$-dimensi)                     | Hanya vektor 3D (atau 2D dengan asumsi komponen z nol)                         |
| **Arah Hasil**     | Tidak ada arah, karena hasilnya skalar                                    | Tegak lurus terhadap kedua vektor input (sesuai kaidah tangan kanan)           |
| **Interpretasi Geometris** | Proyeksi satu vektor ke vektor lain, terkait dengan sudut antar vektor | Vektor normal ke bidang yang dibentuk oleh dua vektor, terkait dengan luas jajaran genjang |
| **NumPy Function** | `np.dot()`, `@` operator                                                  | `np.cross()`                                                                   |
| **Komutatif**      | Ya ($\mathbf{A} \cdot \mathbf{B} = \mathbf{B} \cdot \mathbf{A}$)          | Tidak ($\mathbf{A} \times \mathbf{B} = -(\mathbf{B} \times \mathbf{A})$)       |
| **Kapan Nol**      | Ketika vektor ortogonal ($\theta = 90^\circ$)                             | Ketika vektor sejajar atau anti-sejajar ($\theta = 0^\circ \text{ atau } 180^\circ$) |

Memahami perbedaan dan aplikasi dari dot product dan cross product sangat penting untuk melakukan operasi vektor yang benar dalam analisis data dan komputasi ilmiah menggunakan NumPy.