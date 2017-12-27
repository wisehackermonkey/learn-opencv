import cv2
import numpy as np


# Load an color image in grayscale
img = cv2.imread('image.jpg',0)
cv2.imshow('image',img)



cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # blur = cv2.GaussianBlur(frame, (55,55), 0)

    # Display the resulting frame
    cv2.imshow('Blur',blur)

    # Dilate video
    kernal = np.ones((5,5), 'uint8')
    dilate = cv2.dilate(frame, kernal, iterations=1)

    cv2.imshow('Diated', dilate)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
