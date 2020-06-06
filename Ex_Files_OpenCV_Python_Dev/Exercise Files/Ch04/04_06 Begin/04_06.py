import numpy as np
import cv2

img = cv2.imread("faces.jpeg",1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
color = (255, 255, 0)

path ="haarcascade_eye.xml"

eye_cascade = cv2.CascadeClassifier(path)
eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=2)

print(len(eyes))

for (x, y, w, h) in eyes:
    xc = (x + x + w) / 2
    yc = (y + y + h) / 2
    radius = w / 2
    cv2.circle(img, (int(xc), int(yc)), int(radius), color = color, thickness = 3)

cv2.imshow("Result", img)
cv2.imwrite("result.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()