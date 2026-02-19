import numpy as np

# 1. Membuat Array dengan Tipe Data Spesifik (`dtype`)
print("Pembuatan Array Standar")
A = np.array([[1, 2, 3], [3, 4, 5]])
print(A)

print("\nMenentukan Tipe Data")
B = np.array([[1, 2, 3], [3, 4, 5]], dtype=int)
print("Integer:")
print(B)

print("\nFloat:")
C = np.array([[1, 2, 3], [3, 4, 5]], dtype=float)
print(C)

print("\nString:")
D = np.array([[1, 2, 3], [3, 4, 5]], dtype=str)
print(D)

print("\nBoolean:")
E = np.array([[1, 2, 3], [3, 4, 5]], dtype=bool)
print(E)


# 2. Membuat Array dari Fungsi (`np.fromfunction`)
print("\nPembuatan Array dari Fungsi")
print("Fungsi Kustom")
def kuadrat(baris, kolom):
    return kolom**2

# Contoh penggunaan fungsi kuadrat secara langsung
print(kuadrat(1, 5))

print("\nPenggunaan `np.fromfunction`")
B = np.fromfunction(kuadrat, (1, 10), dtype=int)
print(B)

print("\nArray 2D (Matrix)")
def jumlah(baris, kolom):
    return baris + kolom

C = np.fromfunction(jumlah, (4, 4), dtype=float)
print(C)


# 3. Membuat Array dari Iterable (`np.fromiter`)
print("\nPembuatan Array dari Iterable")
print("List Comprehension/Generator Expression")
iterable_data = (x**2 for x in range(5)) # Ini adalah generator expression, bukan list comprehension
print("Generator Expression:")
print(iterable_data)

print("\nPenggunaan `np.fromiter`")
D = np.fromiter(iterable_data, dtype=int)
print(D)

iterable_data_x2 = (x*2 for x in range(5))
D_x2 = np.fromiter(iterable_data_x2, dtype=int)
print(D_x2)


# 4. Membuat Array Multi-Tipe (Structured Array)
print("\nPembuatan Array Multi-Tipe (Structured Array)")
print("Data Input")
data = [('Alice', 25, 5.5),
        ('Bob', 30, 6.0),
        ('Charlie', 35, 5.8)]
print(data)

print("\nMendefinisikan `dtype` Kustom")
custom_dtype = np.dtype([
    ('name', 'U10'),
    ('age', 'i4'),
    ('height', 'f4')])

print("\nPembuatan Array")
structured_array = np.array(data, dtype=custom_dtype)
print(structured_array)

print("\nMengakses Elemen")
print("Nama:")
print(structured_array['name'])
print("Usia:")
print(structured_array['age'])
print("Tinggi:")
print(structured_array['height'])
print(structured_array[0])  # Mengakses elemen pertama