import numpy as np
import cv2

color =  cv2.imread("butterfly.jpg", 1)
gray = cv2.cvtColor(color, cv2.COLOR_RGB2GRAY)

cv2.imwrite("gray.jpg", gray)

# more efficient and faster compare to using color.split()
b = color[:,:,0]
g = color[:,:,1]
r = color[:,:,2]
# the forth parameter acts as our transparent layer (green color in this case)
# hence, for the color which is green the color will be shown as high alpha layer,
# Everything else will be transparent (non-green or low-green);
rgba =  cv2.merge((b, g, r, g))
cv2.imwrite("rgba.png", rgba)