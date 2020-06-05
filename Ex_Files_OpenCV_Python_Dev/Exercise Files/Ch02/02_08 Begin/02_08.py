import numpy as np
import cv2

cap = cv2.VideoCapture(0)
# while loop for the main program
while (True):
    ret, frame = cap.read()
    frame = cv2.resize(frame, (0,0),fx = 0.5, fy = 0.5)
    cv2.imshow("Frame", frame)
    cv2.imwrite("My image.png", frame)
    ch = cv2.waitKey(1)
    # terminate the camera when the q character is clicked;
    if ch & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()