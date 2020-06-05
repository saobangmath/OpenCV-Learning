import numpy as np
import cv2
# Gaussian blur filter;
image = cv2.imread("thresh.jpg")
cv2.imshow("Original", image)
# pair (x, y): how much the scale of the blur on each direction (x-axis, y-axis);
# note that both x, y must be ODD
blur = cv2.GaussianBlur(image, (5, 1), 0)
cv2.imshow("Blur", blur)
# define kernel
kernel = np.ones((4, 4), "uint8")
# dilate: turn black (background) pixels -> white pixels
# erode: turn white pixels -> black (background) pixels;
dilate = cv2.dilate(image, kernel,iterations=1)
erode = cv2.erode(image, kernel, iterations=1)

cv2.imshow("Dilate", dilate)
cv2.imshow("Erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()
