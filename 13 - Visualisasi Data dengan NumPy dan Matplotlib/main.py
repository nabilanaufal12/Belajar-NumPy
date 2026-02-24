import numpy as np
import matplotlib.pyplot as plt

# Membuat Plot Persamaan Garis Lurus
x1 = np.arange(0, 11, 1)
y1 = 2 * x1 + 3
# plt.plot(x1, y1)
# plt.show()


# Membuat Plot Lingkaran
jari_jari = 5
sudut = np.linspace(0, 2 * np.pi, 100)
x2 = jari_jari * np.cos(sudut)
y2 = jari_jari * np.sin(sudut)
# plt.plot(x2, y2)
# plt.show()


# Mengelola Beberapa Plot (Figures)
# Plot pertama (misalnya, garis lurus)
plt.figure(1)
plt.plot(x1, y1) # Asumsikan x1, y1 sudah didefinisikan

# Plot kedua (misalnya, lingkaran)
plt.figure(2)
plt.plot(x2, y2) # Asumsikan x2, y2 sudah didefinisikan

plt.show()