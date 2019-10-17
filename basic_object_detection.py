import cv2
import numpy as np

cap = cv2.VideoCapture(0)
while(True):
    _,frame = cap.read()

    husat = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    mask = cv2.inRange(husat,lower_blue,upper_blue)

    im = cv2.bitwise_and(frame,frame,mask = mask)

    

    
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
