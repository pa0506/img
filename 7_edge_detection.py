import cv2
import matplotlib.pyplot as plt

img = cv2.imread("1_image.jpg", 0)

sobel = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)
lap = cv2.Laplacian(img, cv2.CV_64F)
canny = cv2.Canny(img, 100, 200)

plt.subplot(221)
plt.imshow(img, cmap="gray")
plt.title("Original")

plt.subplot(222)
plt.imshow(cv2.convertScaleAbs(sobel), cmap="gray")
plt.title("Sobel")

plt.subplot(223)
plt.imshow(cv2.convertScaleAbs(lap), cmap="gray")
plt.title("Laplacian")

plt.subplot(224)
plt.imshow(canny, cmap="gray")
plt.title("Canny")

plt.show()