import cv2
import matplotlib.pyplot as plt

img = cv2.imread("1_image.jpg", 0)

plt.hist(img.ravel(), 256, [0,256])
plt.show()

low = cv2.GaussianBlur(img, (5,5), 0)
high = cv2.subtract(img, low)

plt.figure(figsize=(12, 4))

plt.subplot(1,3,1)
plt.imshow(img, cmap="gray")
plt.title("Original")

plt.subplot(1,3,2)
plt.imshow(low, cmap="gray")
plt.title("Low Pass")

plt.subplot(1,3,3)
plt.imshow(high, cmap="gray")
plt.title("High Pass")

plt.show()