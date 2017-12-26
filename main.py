import cv2
import numpy as np


# Load an color image in grayscale
img = cv2.imread('image.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
# import numpy as np
# import cv2
# cap.release()

# cap = cv2.VideoCapture(0)

# #green tuple
# color = (0,255,0)
# # circle line width 
# #note -1 = filled circle
# line_width = 3
# radius = 100
# # (x,y) starting point of circle
# point = (0,0)


# #mouse callback
# def click(event, x,y, flags, param):
# 	global point, pressed
# 	# if mouse press set point
# 	if event == cv2.EVENT_LBUTTONDOWN:
# 		print("Pressed", x,y)
# 		point = (x,y)

# #add mouse click callback on each frame 
# # of video
# # Note "frame" is refering to 
# #cv2.imshow("Frame", frame)
# #and must be spelled EXACTLY the same encluding capitals 
# cv2.namedWindow("Frame")
# cv2.setMouseCallback("Frame",click)
# # if capture failed to open, try again
# if not cap.isOpened():
#     cap.open(0)

# # only attempt to read if it is opened
# if cap.isOpened:

# 	while(True):
# 		# reads a fram into
# 		ret, frame = cap.read()

# 		frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
# 		cv2.circle(frame, point, radius, color, line_width)
# 		cv2.imshow("Frame", frame)

# 		# wait 1 milliseconds
# 		ch = cv2.waitKey(1)
# 		#check if key is <'q'>, 0xFF is for 64bit systems
# 		# ANDing 0xFF only gets key codes 
# 		if ch == ord('q'):
# 			break

# 	#important otherwise you will not have use of camera!
# 	cap.release()
# 	cv2.destroyAllWindows()
# else:
# 	print( "Failed to open capture device")