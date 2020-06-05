import numpy as np
import cv2
# load a butterfly image
color = cv2.imread("butterfly.jpg", 1)
cv2.imshow("Butterfly", color)
cv2.moveWindow("Butterfly", 0, 0)
# height,width and number of channels of the image
height, width, channels = color.shape
# split 3 channels of the color image;
# blue, green, red;
b, g, r = cv2.split(color)
rgb_split = np.empty([height,width * 3, 3], 'uint8')

# rgb_split[:, 0:width] = cv2.merge([b, b, b])
# rgb_split[:, width:2*width] = cv2.merge([g, g, g])
# rgb_split[:,2*width:3*width] = cv2.merge([r, r, r])
# this is equivalent to divide the width in 3 sections and display each image channel in each section;
rgb_split = np.concatenate([b, g, r], axis = 1)

cv2.imshow("Channels", rgb_split)
cv2.moveWindow("Channels", 0, height)

hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
# splitting 3 channels of the hsv image;
h, s, v = cv2.split(hsv)

hsv_split = np.concatenate((h, s, v), axis=1)
cv2.imshow("SplitHSV", hsv_split)
cv2.moveWindow("SplitHSV", 0, height)
# delay to display the image
cv2.waitKey(0)
# destroy all windows;
cv2.destroyAllWindows()