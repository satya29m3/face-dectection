import cv2 
import numpy as np


cap= cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   # cv2.imshow('gray',gray)

    #cv2.line(frame,(0,0),(150,150),(255,0,0),15)
    #cv2.rectangle(frame,(15,25),(200,150),(0,255,0),5)
    #cv2.circle(frame,(150,250),(55),(0,255,0),5)

    #frame[100:500,100:500] = (255,255,255)
    ret ,mask = cv2.threshold(gray,220,255,cv2.THRESH_BINARY)
    #gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #gaus = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)

    cv2.imshow('mask',mask)
    
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.realease()
cv2.destroyAllWindows()