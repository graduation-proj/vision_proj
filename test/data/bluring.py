import numpy as np
import cv2

def bluring(img,i):
    blur33 = cv2.blur(img,(3,3))
    blur55 = cv2.blur(img,(5,5))

    blur33_path = 'blur33/images-%d.jpg'%i
    blur55_path = 'blur55/images-%d.jpg'%i
    cv2.imwrite(blur33_path,blur33)
    cv2.imwrite(blur55_path,blur55)


if __name__ == "__main__":
    for i in range(1,108):
        img_path = 'origin/images-%d.jpg'%i
        img = cv2.imread(img_path)
        
        bluring(img,i)

