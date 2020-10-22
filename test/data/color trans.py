import numpy as np
import cv2

def colorTrans(img,i):
    trans1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    trans2 = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)[:,:,0]
    
    trans1_path = 'trans1/images-%d.jpg'%i
    trans2_path = 'trans2/images-%d.jpg'%i
    cv2.imwrite(trans1_path,trans1)
    cv2.imwrite(trans2_path,trans2)


if __name__ == "__main__":
    for i in range(1,108):
        img_path = 'origin/images-%d.jpg'%i
        img = cv2.imread(img_path)
    
        colorTrans(img,i)

