import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("1_image.jpg", 0)

_, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

power = np.uint8(255 * (img / 255.0) ** 0.5)

kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]])
high = cv2.filter2D(img, -1, kernel)

plt.subplot(221)
plt.imshow(th, cmap="gray")
plt.title("Threshold")

plt.subplot(222)
plt.imshow(power, cmap="gray")
plt.title("Power Enhancement")

plt.subplot(223)
plt.imshow(high, cmap="gray")
plt.title("High Pass")

plt.subplot(224)
plt.imshow(img, cmap="gray")
plt.title("Original")

plt.show()