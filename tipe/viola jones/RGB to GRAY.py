import cv2
#ouvrir l'image
img = cv2.imread('photos/obama twin.jpg')


R, G, B = img[:,:,0], img[:,:,1], img[:,:,2]

#coeffs : check rgb to gray coeff pdf file
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B

#save img
cv2.imwrite('img.jpg',imgGray)
image_sortie=cv2.imread('img.jpg')
cv2.imshow('img.jpg',image_sortie)
cv2.waitKey(0)