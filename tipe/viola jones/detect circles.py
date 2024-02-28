import cv2,numpy as np
planets=cv2.imread("photos/planet.jpg")
gray_img=cv2.cvtColor(planets,cv2.COLOR_BGR2GRAY)
gray_img=cv2.medianBlur(gray_img,5)
circles=cv2.HoughCircles(gray_img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
circles=np.uint16(np.around(circles))
for i in circles[0, :]:
    #draw the outer circle
    cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),2)
    #draw the center of the circle
    cv2.circle(planets,(i[0],i[1]),2,(0,255,0),3)
cv2.imwrite("planet2.jpg",planets)
cv2.imshow("HoughCircles",planets)
cv2.waitKey()
cv2.destroyAllWindows()