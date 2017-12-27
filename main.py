import cv2
import numpy as np


# Load an color image in grayscale
img = cv2.imread('image.jpg',0)
cv2.imshow('image',img)

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
        mouseX,mouseY = x,y


cap = cv2.VideoCapture(0)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	cv2.imshow('Camera', frame)
 
	# Rotation
	# M - capital letters are convention for matrix operations
	#(0,0) - origin of rotation, -30 - minus 30 degrees of rotation, 1 - not sure
	# M = cv2.getRotationMatrix2D((0,0), -30, 1)
	# rotated = cv2.warpAffine(img, M, (img.shape[1], img.shape[0]))
	# cv2.imshow("Rotated", rotated)


	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
