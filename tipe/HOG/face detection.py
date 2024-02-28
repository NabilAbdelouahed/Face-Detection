import face_recognition as fr
from PIL import Image, ImageDraw
import cv2 , os , numpy as np , time

path1 = "D:/AI influencer/image (5).png"
path2 = "D:/AI influencer/image.png"
listing = os.listdir(path1)

for file in listing:
    #load img
    image = fr.load_image_file(path1+file)
    #localise face
    loc = fr.face_locations(image)
    #draw a rectangle around the face
    image_pil = Image.fromarray(image)
    draw = ImageDraw.Draw(image_pil)

    for (x,y,z,t) in loc :
        draw.rectangle(((y,x),(t,z)), outline=(0,0,255))


    image_pil.save(path2+file)