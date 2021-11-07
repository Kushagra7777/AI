import cv2
import numpy as np
import face_recognition
import os 

path = 'Test_images'
images  = []
classNames = []
mylist = os.listdir(path)
print(mylist)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

print(classNames)


def findEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)


    return encodelist


encodelistKnown = findEncodings(images)
print('Encoding Complete')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    
    faceCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,faceCurFrame)
    
    for encodeFace,faceLoc in zip(encodesCurFrame,faceCurFrame):
        matches = face_recognition.compare_faces(encodelistKnown,encodeFace)






# faceLoc = face_recognition.face_locations(imgElon)[0]
# encodeElon = face_recognition.face_encodings(imgElon)[0]
# # cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255),2)
# str_pt = (faceLoc[3],faceLoc[0])
# end_pt = (faceLoc[1],faceLoc[2])
# cv2.rectangle(imgElon,str_pt,end_pt,(255,0,255),2)


# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# # cv2.rectangle(imgElon, (faceLoc[3],faceLoc[0],faceLoc[1],faceLoc[2]),(255,0,255),2)
# str_pt = (faceLocTest[3],faceLocTest[0])
# end_pt = (faceLocTest[1],faceLocTest[2])
# cv2.rectangle(imgTest,str_pt,end_pt,(255,0,255),2)


# results = face_recognition.compare_faces([encodeElon],encodeTest)
# faceDis = face_recognition.face_distance([encodeElon],encodeTest)