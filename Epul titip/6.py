# Mengimport library
import matplotlib.pyplot as plt
#%matplotlib inline
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np
import cv2

citra1 = cv2.imread("epul.jpeg", cv2.IMREAD_GRAYSCALE)
# Membaca gambar

print(citra1.shape)
# Menampilkan dimensi citra dalam bentuk

plt.imshow(citra1, cmap='gray')
# Menampilkan citra grayscale

kernel = np.array([[-1, 0, -1],
                   [0, 4, 0],
                   [-1, 0, -1]])
# Membuat kernel dengan matriks tertentu yang akan digunakan dalam operasi konvolusi.

citraOutput = cv2.filter2D(citra1, -1, kernel)
# Melakukan operasi konvolusi pada citra citra1 menggunakan kernel yang telah dibuat sebelumnya

fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(citra1, cmap='gray')
ax[0].set_title("Citra Input")
ax[1].imshow(citraOutput, cmap='gray')
ax[1].set_title("Citra Output")

fig.tight_layout()
# Mengatur tata letak plot agar lebih rapi.

plt.show()
# Menampilkan plot ke layar.
