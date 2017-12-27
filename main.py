import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    height, width, channels = frame.shape

    b, g, red_colors = cv2.split(frame)

    empty_image = np.ones([height, width, 3],  'uint8')


    cv2.imshow("Red Colors", empty_image)



    # Dilate video
    kernal = np.ones((5,5), 'uint8')
    dilate = cv2.dilate(frame, kernal, iterations=1)

    cv2.imshow('Diated', dilate)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
