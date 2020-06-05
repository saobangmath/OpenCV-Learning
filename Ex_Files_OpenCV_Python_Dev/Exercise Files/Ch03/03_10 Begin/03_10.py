import numpy as np
import cv2
from random import randint as r

colors = [(0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 0), (255, 255, 255), (255, 0,255)]
i = 0
img = cv2.imread("fuzzy.png",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)

objects = np.zeros([img.shape[0], img.shape[1], 3], 'uint8')

thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 301, 1)
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.imshow("Thresh", thresh)

for c in contours:
    area = cv2.contourArea(c)
    perimeter = cv2.arcLength(c, True)
    print("Area: {}, perimeter: {}".format(area, perimeter))
    if area > 1000:
        cv2.drawContours(objects,[c], -1, colors[r(0, 5)], -1)


cv2.imshow("Original", img)
cv2.imshow("Contours", objects)
cv2.imwrite("contours.png", objects)

cv2.waitKey(0)
cv2.destroyAllWindows()
