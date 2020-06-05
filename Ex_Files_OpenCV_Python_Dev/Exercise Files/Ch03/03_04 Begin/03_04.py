import numpy as np
import cv2

img = cv2.imread('faces.jpeg',1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h = hsv[:,:,0]
s = hsv[:,:,1]
v = hsv[:,:,2]
# hue channel
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("Split HSV", hsv_split)
# saturation channel;
ret, min_sat = cv2.threshold(s, 40, 255, cv2.THRESH_BINARY)
cv2.imshow("Sat filter", min_sat)
# maximum hue channel;
ret, max_hue = cv2.threshold(h, 15, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Hue filter", max_hue)
# combination between saturation and hue channels;
final = cv2.bitwise_and(min_sat, max_hue)
cv2.imshow("Final", final)
# displaying original image for comparing purpose;
cv2.imshow("Original", img)

cv2.waitKey(0)
cv2.destroyAllWindows()