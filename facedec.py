import cv2

"""
resized = cv2.resize(img,(int (img.shape[1]*2),int(img.shape[0]*2)))
print(type(img))
print(resized.shape)
cv2.imshow("he",resized)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

face_cascade = cv2.CascadeClassifier('/home/satya/Downloads/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('/home/satya/Downloads/opencv-master/data/haarcascades/haarcascade_eye.xml')
#img = cv2.imread("/home/satya/Downloads/jon.jpeg",1)
cap = cv2.VideoCapture(0)
while True:
    ret,img = cap.read()
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)

    for x ,y,w,h in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(120,150,0),3)
        roi_gray = gray_img[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray )
        for (ex,ey,eh,ew) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    #resized = cv2.resize(img,(int(img.shape[1]*7),int(img.shape[0]*7)))

    cv2.imshow("gray",img)

    k=cv2.waitKey(30) & 0xff
    if k == 27:
        break
    
cv2.destroyAllWindows()







