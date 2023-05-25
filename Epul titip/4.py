#import library yang dibutuhkan
import matplotlib.pyplot as plt
import cv2
#%matplotlib inline

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
import numpy as np

citra1 = cv2.imread("epul.jpeg", cv2.IMREAD_GRAYSCALE)    # Membaca citra
citra2 = cv2.imread("darma.jpeg", cv2.IMREAD_GRAYSCALE)      # Membaca citra

print('Shape citra 1 : ', citra1.shape)    # Menampilkan bentuk (shape) dari citra
print('Shape citra 1 : ', citra2.shape)

fig, axes = plt.subplots(1, 2, figsize=(10, 10))    # Membuat subplots dengan 1 baris dan 2 kolom
ax = axes.ravel()                                   # Mengubah array axes menjadi satu dimensi

ax[0].imshow(citra1, cmap='gray')    # Menampilkan citra 1 dengan colormap gray pada subplot
ax[0].set_title("Citra 1")            # Menetapkan judul pada subplot
ax[1].imshow(citra2, cmap='gray')
ax[1].set_title("Citra 2")

copyCitra1 = citra1.copy()    # Membuat salinan citra
copyCitra2 = citra2.copy()

m1, n1 = copyCitra1.shape    # Mendapatkan dimensi citra 1
output1 = np.empty([m1, n1])    # Membuat array kosong dengan dimensi yang sama dengan citra 1

m2, n2 = copyCitra2.shape    # Mendapatkan dimensi citra 2
output2 = np.empty([m2, n2])    # Membuat array kosong dengan dimensi yang sama dengan citra 2

print('Shape copy citra 1 : ', copyCitra1.shape)    # Menampilkan bentuk (shape) dari salinan citra 1
print('Shape output citra 1 : ', output1.shape)    # Menampilkan bentuk (shape) dari output citra 1

print('m1 : ', m1)
print('n1 : ', n1)

print()

print('Shape copy citra 2 : ', copyCitra2.shape)    # Menampilkan bentuk (shape) dari salinan citra 2
print('Shape output citra 3 : ', output2.shape)    # Menampilkan bentuk (shape) dari output citra 2

print('m2 : ', m2)
print('n2 : ', n2)

print()

for baris in range(0, m1 - 1):    # Melakukan iterasi untuk setiap baris dalam citra 1
    for kolom in range(0, n1 - 1):    # Melakukan iterasi untuk setiap kolom dalam citra 1
        a1 = baris
        b1 = kolom
        dataA = [copyCitra1[a1 - 1, b1 - 1], copyCitra1[a1 - 1, b1], copyCitra1[a1 - 1, b1 + 1], \
                 copyCitra1[a1, b1 - 1], copyCitra1[a1, b1], copyCitra1[a1, b1 + 1], \
                 copyCitra1[a1 + 1, b1 - 1], copyCitra1[a1 + 1, b1], copyCitra1[a1 + 1, b1 + 1]]

        # Urutkan dataA menggunakan metode bubble sort
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output1[a1, b1] = dataA[5]    # Ambil nilai median dari dataA

for baris in range(0, m2 - 1):    # Melakukan iterasi untuk setiap baris dalam citra 2
    for kolom in range(0, n2 - 1):    # Melakukan iterasi untuk setiap kolom dalam citra 2
        a1 = baris
        b1 = kolom
        dataA = [copyCitra2[a1 - 1, b1 - 1], copyCitra2[a1 - 1, b1], copyCitra2[a1 - 1, b1 + 1], \
                 copyCitra2[a1, b1 - 1], copyCitra2[a1, b1], copyCitra2[a1, b1 + 1], \
                 copyCitra2[a1 + 1, b1 - 1], copyCitra2[a1 + 1, b1], copyCitra2[a1 + 1, b1 + 1]]

        # Urutkan dataA menggunakan metode bubble sort
        for i in range(1, 8):
            for j in range(i, 9):
                if dataA[i] > dataA[j]:
                    tmpA = dataA[i]
                    dataA[i] = dataA[j]
                    dataA[j] = tmpA

        output2[a1, b1] = dataA[5]    # Ambil nilai median dari dataA

fig, axes = plt.subplots(2, 2, figsize=(10, 10))    # Membuat subplots dengan 2 baris dan 2 kolom
ax = axes.ravel()                                   # Mengubah array axes menjadi satu dimensi

ax[0].imshow(citra1, cmap='gray')    # Menampilkan citra 1 pada subplot
ax[0].set_title("Input Citra 1")    # Menetapkan judul pada subplot

ax[1].imshow(citra2, cmap='gray')
ax[1].set_title("Input Citra 1")

ax[2].imshow(output1, cmap='gray')
ax[2].set_title("Output Citra 1")

ax[3].imshow(output2, cmap='gray')
ax[3].set_title("Output Citra 2")

fig.tight_layout()
plt.show()    # Menampilkan plot
