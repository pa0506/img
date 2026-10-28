import cv2
import matplotlib.pyplot as plt

img = cv2.imread("porosh.png", 0)

_, binary = cv2.threshold(img, 0, 255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
chars = []

for c in contours:
    x, y, w, h = cv2.boundingRect(c)
    if w > 5 and h > 10:
        chars.append((x, y, w, h))

chars.sort(key=lambda a: a[0])

for x, y, w, h in chars:
    cv2.rectangle(output, (x, y), (x+w, y+h), (0, 255, 0), 2)

print("Total Characters:", len(chars))

plt.subplot(131)
plt.imshow(img, cmap="gray")
plt.title("Original")
plt.axis("off")

plt.subplot(132)
plt.imshow(binary, cmap="gray")
plt.title("Binary")
plt.axis("off")

plt.subplot(133)
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
plt.title("Character Segmentation")
plt.axis("off")

plt.show()