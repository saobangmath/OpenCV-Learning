import numpy as np
import cv2

# Global variables
canvas = np.ones([500,500,3],'uint8')*255
# color define - notice in the interchange of blue and red in the openCV - not ordinary as expected!;
blue = (255, 0, 0)
green = (0, 255, 0)
red = (0, 0, 255)
# color of the drawing stuff;
color = red # default;
pressed = False
radius = 10
center = (0, 0)
# button_down: draw a circle;
# button_mouse move: do nothing
# bottom_up: change color from r ->g and reverse;
def click(event, x, y, flags, param):
    global canvas, color, pressed
    center = (x, y)
    if event == cv2.EVENT_LBUTTONDOWN:
        pressed = True
        cv2.circle(canvas, center, radius, color, 2)
        print("LButton Down")
    elif event == cv2.EVENT_MOUSEMOVE and pressed:
        cv2.circle(canvas, center, radius, color, 2)
        print("Mouse Move")
    elif event == cv2.EVENT_LBUTTONUP:
        print("LButton Up")
        pressed = False

# window initialization and callback assignment
cv2.namedWindow("canvas")
cv2.setMouseCallback("canvas", click)

# Forever draw loop
while True:
    cv2.imshow("canvas",canvas)
    # key capture every 1ms;
    ch = cv2.waitKey(1)
    # ending the infinite loop;
    if ch & 0xFF == ord('q'):
        break
    # color setting with pressing respective button;
    if ch & 0xFF == ord('b'):
        color = blue
    if ch & 0xFF == ord('g'):
        color = green
    if ch & 0xFF == ord('r'):
        color = red
	
cv2.imwrite("MyCanvas.jpg", canvas)
cv2.destroyAllWindows()