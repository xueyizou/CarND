import numpy as np
import cv2

cap = cv2.VideoCapture('yellow.mp4')
#cap = cv2.VideoCapture('white.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame',frame)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()