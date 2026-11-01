import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("2_rice.jpg", 0)
_, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
binary = cv2.morphologyEx(binary, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))

n, labels, stats, _ = cv2.connectedComponentsWithStats(binary, 8)
output = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
selected = np.zeros_like(img)

for i in range(1, n):
    area = stats[i, cv2.CC_STAT_AREA]
    w, h = stats[i, 2], stats[i, 3]

    if area > 20:
        obj = np.uint8(labels == i) * 255
        c, _ = cv2.findContours(obj, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if c:
            p = cv2.arcLength(c[0], True)
            print("Area:", area, "Major Axis:", max(w,h), "Perimeter:", p)

            x, y = stats[i, 0], stats[i, 1]
            cv2.rectangle(output, (x,y), (x+w,y+h), (0,255,0), 1)

            if 50 <= area <= 500:
                selected[labels == i] = 255

print("Total Rice:", n-1)

plt.figure(figsize=(12,4))
plt.subplot(131); 
plt.imshow(img, cmap="gray");
plt.title("Original")

plt.subplot(132); 
plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB)); 
plt.title("Detected Rice")

plt.subplot(133); 
plt.imshow(selected, cmap="gray");
plt.title("Specific Area Range")
plt.show()