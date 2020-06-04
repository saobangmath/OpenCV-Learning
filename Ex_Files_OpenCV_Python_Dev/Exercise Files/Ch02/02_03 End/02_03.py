import numpy as np
import cv2
# black color image created with the np array filled with all zero in 1 channel;
black = np.zeros([150,200,1],'uint8')
cv2.imshow("Black",black)
print(black[0,0,:])
# all 1's matrix created
ones = np.ones([150,200,3],'uint8')
cv2.imshow("Ones",ones)
print(ones[0,0,:])
# white color image created by scaling the ones image matrix;
white = np.ones([150,200,3],'uint16')
white *= (2**16-1)
cv2.imshow("White",white)
print(white[0,0,:])
# blue color image created by replace each pixel with the channel of the blue pixel;
color = ones.copy()
color[:,:] = (255,0,0)
cv2.imshow("Blue",color)
print(color[0,0,:])
# wait key escape;
cv2.waitKey(0)
# destroy all window's;
cv2.destroyAllWindows()