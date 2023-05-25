# import library yang diperlukan
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("epul.jpeg") # Membaca gambar
epul = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Mengubah format citra

plt.imshow(epul)
plt.title("Gambar Awal")
plt.axis("off")
plt.show()
# Menampilkan gambar awal (citra RGB)

kernel = np.ones((5,5),np.float32)/25
print(kernel)
# Membuat filter dengan matriks berukuran 5x5

epul_filter = cv2.filter2D(img,-1,kernel)
# Melakukan operasi filtering pada citra asli

plt.imshow(epul_filter)
plt.title("Gambar Setelah Filtering")
plt.axis("off")
plt.show()
# Menampilkan citra setelah proses filtering

data = np.random.normal(size=1000)

plt.rcParams["figure.figsize"] = (15,15)
# Mengatur ukuran plot menjadi 15x15

plt.subplot(221)
plt.hist(data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')

plt.subplot(222), plt.imshow(epul)
plt.title('Original')
plt.xticks([]), plt.yticks([])

plt.subplot(223), plt.imshow(epul_filter)
plt.title('Averaging')
plt.xticks([]), plt.yticks([])

plt.subplot(224)
hist_data = epul_filter.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Setelah Filtering')

plt.suptitle('Gambar dan Histogram')
plt.show()

epul_blur = cv2.blur(img,(5,5))
plt.imshow(epul_blur)
# Melakukan operasi blurring pada citra asli (img)

kernel = np.matrix([
          [1, 1, 1],
          [1, 2, 1],
          [1, 1, 1]
          ])/25
print(kernel)
# Membuat kernel dengan menggunakan np.matrix dengan matriks berukuran 3x3

epul_filter = cv2.filter2D(img,-1,kernel)

plt.imshow(epul_filter)
plt.show()
# Melakukan operasi filtering pada citra asli

# Highpass Filter

img = cv2.imread("epul.jpeg", 0)  # Membaca citra
laplacian = cv2.Laplacian(img, cv2.CV_64F)  # Menerapkan algoritma high-pass filtering

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
# Menerapkan algoritma high-pass filtering

plt.rcParams["figure.figsize"] = (20, 20)  # Mengatur ukuran plot menjadi 20x20

plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

plt.figure(figsize=(10, 5))
plt.subplot(121)
hist_data = img.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram (Original)')

plt.subplot(122)
hist_data = laplacian.flatten()
plt.hist(hist_data, bins=30)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram (Laplacian)')

plt.show()


img = cv2.imread("epul.jpeg", 0) # Membaca citra

# memanggil fungsi Canny Edges dengan argument
edges = cv2.Canny(img, 100, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()
# Menampilkan citra asli dan citra hasil deteksi tepi

img = cv2.imread("epul.jpeg",0) # Membaca citra

ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
# Melakukan thresholding pada citra grayscale

titles = ['Gambar asli','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# Menyimpan judul dan citra hasil thresholding

for i in range(6):
    plt.subplot(3,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
# Menampilkan citra-citra hasil thresholding

img = cv2.medianBlur(img,5) # Menggunakan median blur pada citra grayscale

# Lakukan Thresholding
# Binary Threshold
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Melakukan thresholding binary menggunakan fungsi threshold

# Adaptive Threshold dengan Mean
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# Melakukan thresholding adaptif dengan metode mean menggunakan fungsi adaptiveThreshold dari OpenCV. Menggunakan ukuran blok 11x11 dan konstanta C sebesar 2.

# Adaptive Threshold dengan Gaussian
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
# Melakukan thresholding adaptif dengan metode Gaussian menggunakan fungsi adaptiveThreshold dari OpenCV. Menggunakan ukuran blok 11x11 dan konstanta C sebesar 2.

# Plotting
titles = ['Original Image', 'Global Thresholding (v = 127)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, th1, th2, th3]
# Membuat list judul 'titles'

# menampilkan hasil
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
# Melakukan iterasi untuk menampilkan gambar

plt.tight_layout()
plt.show()
# Menampilkan plot.

# Membuat histogram
plt.subplot(2, 2, 1)
plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram Gambar asli')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')

# Membuat histogram
for i in range(1, 4):
    plt.subplot(2, 2, i + 1)
    plt.hist(images[i].ravel(), 256, [0, 256])
    plt.title('Histogram ' + titles[i])
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
# Menampilkan citra-citra hasil thresholding