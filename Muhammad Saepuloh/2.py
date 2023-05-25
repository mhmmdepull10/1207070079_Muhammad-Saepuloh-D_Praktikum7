#import library yang dibutuhkan
import cv2
import numpy as np
from skimage import data
import matplotlib.pyplot as plt
#%matplotlib inline

img = cv2.imread("epul.jpeg", cv2.IMREAD_GRAYSCALE)  # Membaca citra

row, column = img.shape  # Mendapatkan dimensi citra

img1 = np.zeros((row, column), dtype='uint8')  # Membuat array kosong dengan dimensi yang sama dengan citra

min_range = 10  # Menetapkan nilai batas bawah
max_range = 60  # Menetapkan nilai batas atas

# Looping untuk mengubah piksel menjadi 255 atau 0 berdasarkan batas rentang
for i in range(row):
    for j in range(column):
        if img[i, j] > min_range and img[i, j] < max_range:
            img1[i, j] = 255
        else:
            img1[i, j] = 0

fig, axes = plt.subplots(2, 2, figsize=(12, 12))  # Membuat subplot dengan 2 baris dan 2 kolom
ax = axes.ravel()  # Mengubah array subplot menjadi 1 dimensi

ax[0].imshow(img, cmap=plt.cm.gray)  # Menampilkan citra asli pada subplot
ax[0].set_title("Citra Input")  # Memberikan judul pada subplot
ax[1].hist(img.ravel(), bins=256)
ax[1].set_title('Histogram Input')

ax[2].imshow(img1, cmap=plt.cm.gray)
ax[2].set_title("Citra Output")
ax[3].hist(img1.ravel(), bins=256)
ax[3].set_title('Histogram Output')

fig.tight_layout()
plt.show()  # Menampilkan plot