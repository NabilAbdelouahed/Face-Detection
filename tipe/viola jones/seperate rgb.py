import cv2, numpy as np

img = cv2.imread('photos/IMG_20190925_204740_608.jpg')

img_r , img_g , img_b = np.copy(img) , np.copy(img) , np.copy(img)

for i in range(len(img)):
    for j in range(len(img[i])):
        img_r[i][j][1] , img_r[i][j][2] = 0 , 0
        img_g[i][j][0], img_g[i][j][2] = 0, 0
        img_b[i][j][1], img_b[i][j][0] = 0, 0


cv2.imwrite('img_r.jpg',img_r)
cv2.imshow('img_r.jpg',img_r)

cv2.imwrite('img_b.jpg',img_b)
cv2.imshow('img_b.jpg',img_b)

cv2.imwrite('img_g.jpg',img_g)
cv2.imshow('img_g.jpg',img_g)
cv2.waitKey(0)