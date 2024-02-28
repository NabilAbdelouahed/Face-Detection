import cv2, time
start = time.time()
# load a cascade for face detection
#xml : store and transport data
face_cascade=cv2.CascadeClassifier('folder/cascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('folder/cascades/haarcascade_eye.xml')
#load img
img=cv2.imread('photos/1.jpg')
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
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
cv2.namedWindow('face detected')
cv2.imshow('face detected',img)
cv2.imwrite('face detected.jpg',img)
end = time.time()
elapsed = end - start
print("Temps d'exécution : ",elapsed," s")
cv2.waitKey(0)
