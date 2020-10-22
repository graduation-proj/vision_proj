import numpy as np
import cv2
from random import random
import copy
def salt_and_pepper(image, p):
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - p
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random()
            if rdn < p:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output
for i in range(1,101):
    img_path = "C:/Users/USER/Desktop/origin/origin/images-%d.jpg"%i
    img = cv2.imread(img_path,cv2.IMREAD_UNCHANGED)
    origin = copy.deepcopy(img)
    img = salt_and_pepper(img,0.01)
    cv2.imwrite('C:/Users/USER/Desktop/origin/salt/images-%d.jpg'%i, img)
