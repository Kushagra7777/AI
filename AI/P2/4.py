# Shapes on video
import cv2

#Pixels of video
cap = cv2.VideoCapture(0);
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

# print(cap.isOpened())
# cap.set(3, 700)
# cap.set(4, 700)
# print(cap.get(3))
# print(cap.get(4))
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX
        text = 'Width: '+ str(cap.get(3)) + 'Height: '+ str(cap.get(4))
        # datet = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)

        # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        # out.write(frame)
    
        # gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
           break
    else:
        break

cap.release()
# out.release()
cv2.destroyAllWindows()