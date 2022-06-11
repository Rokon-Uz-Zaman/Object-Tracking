#author : A.B.M. Rokon-uz-zaman (  Roman )
#lib : openCV python  contrib , imutils 

import cv2
import imutils

cap=cv2.VideoCapture('test.mp4')

while True:
    ret,frame=cap.read()
    frame=imutils.resize(frame,width=720)
    cv2.imshow('press S to select',frame)

    if cv2.waitKey(1) & 0xff == ord('s'):

        bb=cv2.selectROI(frame,False)
        cv2.destroyAllWindows()
        break
	
#create tracker obj
tracker=cv2.TrackerCSRT_create()
tracker.init(frame,bb)

while True:
	ret,frame=cap.read()
	frame = imutils.resize(frame,width=720)
	trackCheck,bb = tracker.update(frame)
	if trackCheck:
		topLeft= (int(bb[0]) ,int(bb[1]))
		bottomRight=(int(bb[0]+bb[2]) ,int(bb[1]+bb[3]))
		cv2.rectangle(frame,topLeft,bottomRight,(0,255,0),5)
	cv2.imshow('Traking the selected object',frame)
	#key  =  cv2.waitKey(1) & 0xff
	if cv2.waitKey(1) & 0xff== ord('q'):
		break

cv2.destroyAllWindows()


