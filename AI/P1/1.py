# import face_recognition
import cv2
import pandas as pd
import numpy as np

img = cv2.imread( 'original.jpg', 1)

print(img)

cv2.imshow('image', img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('cat_copy.jpg',img)
    cv2.destroyAllWindows()