import cv2
import matplotlib.pyplot as plt

img = cv2.imread("1_image.jpg", 0)

mask = cv2.Laplacian(img, cv2.CV_64F)
result = cv2.convertScaleAbs(mask)

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title("Original Image")

plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.title("Laplacian Image")

plt.show()
