import cv2
import matplotlib.pyplot as plt

img = cv2.imread("coin.jpg", 0)
_, b = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15))
b = cv2.morphologyEx(b, cv2.MORPH_CLOSE, k)
c, _ = cv2.findContours(b, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

out = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
n = 0

for cnt in c:
    a = cv2.contourArea(cnt)
    if a > 5000:
        n += 1
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.drawContours(out, [cnt], -1, (0, 255, 0), 2)
        cv2.putText(out, str(int(a)), (x, y-5),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        print("Coin", n, "Area:", int(a))

print("Total Coins:", n)
plt.imshow(cv2.cvtColor(out, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()