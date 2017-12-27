import cv2
import numpy as np

cap = cv2.VideoCapture(0)
alpha = 0.5
beta = 0.5

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    height, width, channels = frame.shape

    b, g, red_colors = cv2.split(frame)

    empty_image = np.zeros([height, width, 1],  'uint8')


    reds = cv2.merge([ empty_image[:,:], empty_image[:,:],red_colors[:,:] ])
    cv2.imshow("Red Colors", frame)
    cv2.moveWindow("Red Colors",0,height)
    cv2.imshow("Blended Red + colors",cv2.addWeighted(frame,alpha, reds,beta,0.0 ))



    # Dilate video
    kernal = np.ones((5,5), 'uint8')
    dilate = cv2.dilate(frame, kernal, iterations=1)

    cv2.imshow('Diated', dilate)
    cv2.moveWindow("Diated",width,0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
