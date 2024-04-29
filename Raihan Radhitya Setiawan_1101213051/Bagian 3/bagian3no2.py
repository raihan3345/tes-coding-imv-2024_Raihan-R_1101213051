import cv2
import matplotlib.pyplot as plt

img = cv2.imread('ayon.jpeg')
img_1 = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
img_gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite("ayon_grayscale.jpeg", img_gr)
(thresh, blackAndWhite) = cv2.threshold(img_gr, 127, 255, cv2.THRESH_BINARY)
cv2.imwrite("ayon_bnw.jpeg", blackAndWhite)

fig = plt.figure(figsize=(20,20))

ax1 = fig.add_subplot(1,3,1)
ax1.set_title("ORI")
ax1.imshow(img_1)
ax2 = fig.add_subplot(1,3,2)
ax2.set_title("GRAY")
ax2.imshow(img_gr)
ax3 = fig.add_subplot(1,3,3)
ax3.set_title("B & W")
ax3.imshow(blackAndWhite)

plt.show()