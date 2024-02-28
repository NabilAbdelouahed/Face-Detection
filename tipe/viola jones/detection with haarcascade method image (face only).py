import cv2
# load a cascade for face detection
#xml : store and transport data
face_cascade=cv2.CascadeClassifier('folder/cascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('folder/cascades/haarcascade_eye.xml')
#lopad img
img=cv2.imread('photos/obama twin.jpg')
#convert img to grayscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#detect face
faces=face_cascade.detectMultiScale(gray,1.08,5)
for (x,y,w,h) in faces:
    #draw a rectangle around the face
    #x : left right coord (horizontal)
    #y : up down coord (vertical)
    #w : width of the rectangle
    #h : height of the rectangle
    img=cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
cv2.namedWindow('obama detected')
cv2.imshow('obama detected',img)
#cv2.imwrite('obama detected.jpg',img)
cv2.waitKey(0)
