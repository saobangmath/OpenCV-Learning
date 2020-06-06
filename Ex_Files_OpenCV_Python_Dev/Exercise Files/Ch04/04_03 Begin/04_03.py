import numpy as np
import cv2

template = cv2.imread('template.jpg',0)
frame = cv2.imread("players.jpg",0)
clone = frame.copy()

cv2.imshow("Frame", frame)
cv2.imshow("Template", template)
# match a frame with a predefined template;
result = cv2.matchTemplate(frame, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# print maximum, minimum value and corresponding points of matching w.r.t the template;
print(max_val,max_loc)
print(min_val,min_loc)
# cv2.circle(image, (x,y), radius, color, line thickness);
# drawing a circle to the section with most matching to the template;
cv2.circle(result, max_loc, 15, 255, 2)
# showing the most matching section displayed;
cv2.imshow("Matching", result)
# waiting for any key clicked and destroy all windows after that;
cv2.waitKey(0)
cv2.destroyAllWindows()