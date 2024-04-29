import matplotlib.pyplot as plt
import cv2

image = plt.imread("emma.jpg")
img_180=cv2.rotate(image,cv2.ROTATE_180)
cv2.imwrite("emma_flip_horizontal.jpg", img_180)
img_hor=cv2.flip(image,1)
cv2.imwrite("emma_flip_vertical.jpg", img_hor)
img_trans=cv2.transpose(image)
cv2.imwrite("emma_transpose.jpg", img_trans)

fig = plt.figure(figsize=(20,20))

ax1 = fig.add_subplot(1,4,1)
ax1.set_title("ORI")
ax1.imshow(image)
ax2 = fig.add_subplot(1,4,2)
ax2.set_title("Horizontal")
ax2.imshow(img_hor)
ax3 = fig.add_subplot(1,4,3)
ax3.set_title("Vertical")
ax3.imshow(img_180)
ax4 = fig.add_subplot(1,4,4)
ax4.set_title("Transpose")
ax4.imshow(img_trans)

plt.show()
