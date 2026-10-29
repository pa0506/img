import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("1_image.jpg", 0)

# Smoothing filters
avg = cv2.blur(img, (3, 3))
gauss = cv2.GaussianBlur(img, (3, 3), 0)
median = cv2.medianBlur(img, 3)

# Sharpening filter
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])
sharp = cv2.filter2D(img, -1, kernel)

# Display images
plt.figure(figsize=(8, 5))

plt.subplot(231)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(232)
plt.imshow(avg, cmap="gray")
plt.title("Average Filter")
plt.axis("off")

plt.subplot(233)
plt.imshow(gauss, cmap="gray")
plt.title("Gaussian Filter")
plt.axis("off")

plt.subplot(234)
plt.imshow(median, cmap="gray")
plt.title("Median Filter")
plt.axis("off")

plt.subplot(235)
plt.imshow(sharp, cmap="gray")
plt.title("Sharpening")
plt.axis("off")

plt.tight_layout()
plt.show()