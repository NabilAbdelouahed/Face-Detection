import cv2,numpy as np, os,PIL

randombytearray=bytearray(os.urandom(120000))

flatnumpyarray=np.array(randombytearray)

grayimage=flatnumpyarray.reshape(300,400)

# cv2.imwrite('randomgray.png',grayimage)

bgrimage=flatnumpyarray.reshape(100,400,3)

# cv2.imwrite('randomcolor.png',bgrimage)

cv2.imshow("image",bgrimage)

cv2.waitKey()



