import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("1_image.jpg", 0)

mask = np.ones((3,3), np.float32) / 9
result = cv2.filter2D(img, -1, mask)

plt.subplot(121)
plt.imshow(img, cmap='gray')
plt.title("Original Image")

plt.subplot(122)
plt.imshow(result, cmap='gray')
plt.title("Convolution Image")

plt.show()
