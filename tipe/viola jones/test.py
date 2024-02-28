import cv2, time, os
start = time.time()
# load a cascade for face detection
#xml : store and transport data
face_cascade=cv2.CascadeClassifier('folder/cascades/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier('folder/cascades/haarcascade_eye.xml')

path1 = "photos/test images/noface/"
path2 = "photos/results/noface/"
listing = os.listdir(path1)

for file in listing:
    try:
        img=cv2.imread(path1+file)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.08,5)
        for (x,y,w,h) in faces:
            img=cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0),2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imwrite(path2+file ,img)
    except:
        print("""error : """,file)
end = time.time()
elapsed = end - start
print("Temps d'exécution : ",elapsed," s")

