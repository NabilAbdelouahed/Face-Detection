import cv2

# load a cascade for face and eyes detection
face_cascade=cv2.CascadeClassifier('folder/cascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('folder/cascades/haarcascade_eye.xml')
#activate the cam
camera=cv2.VideoCapture(0)
while (cv2.waitKey(1)==-1):
    success, frame =camera.read()
    if success :
        #convert each frame to grayscale
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #face detection
        faces=face_cascade.detectMultiScale(gray,1.3,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w, y+h),(255,0,0),2)
            roi_gray=gray[y:y+h , x:x+w]
            eyes=eye_cascade.detectMultiScale(roi_gray,1.03,5)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(frame,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,0),2)
    cv2.imshow('face detection',frame)