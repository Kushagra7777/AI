import cv2
from face_recognition.api import face_locations
import numpy as np
import face_recognition



imgElon = face_recognition.load_image_file('Test_images/Elon1.jpg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('Test_images/Elon2.jpg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceLoc = face_recognition.face_locations(imgElon)[0]
encodeElon = face_recognition.face_encodings(imgElon)[0]
# cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255),2)
str_pt = (faceLoc[3],faceLoc[0])
end_pt = (faceLoc[1],faceLoc[2])
cv2.rectangle(imgElon,str_pt,end_pt,(255,0,255),2)


faceLocTest = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255),2)
str_pt = (faceLocTest[3],faceLocTest[0])
end_pt = (faceLocTest[1],faceLocTest[2])
cv2.rectangle(imgTest,str_pt,end_pt,(255,0,255),2)


results = face_recognition.compare_faces([encodeElon],encodeTest)
faceDis = face_recognition.face_distance([encodeElon],encodeTest)
print(results,faceDis)
cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}', (50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)


cv2.imshow('Elon1', imgElon)
cv2.imshow('Elon2', imgTest)

cv2.waitKey(0)