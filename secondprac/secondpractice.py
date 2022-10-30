import cv2
import numpy as np

image=cv2.imread("Fb94AQoWYAAC8MR.png")

cv2.imshow("Furkan",image)

print(image.size)
print(image.dtype)
print(image.shape)

cv2.waitKey(0)
cv2.destroyAllWindows()