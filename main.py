import cv2
import winsound
cam=cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame = cam.read()
    ret, frame1 = cam.read()
    diff = cv2.absdiff(frame, frame1)
    blur1 = cv2.GaussianBlur(diff, (5, 5), 0)
    grey=cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur= cv2.GaussianBlur(grey,(5,5),0)
    _, thresh = cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
    _, thresh1 = cv2.threshold(diff, 20, 255, cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh, None, iterations=3)
    contours,_= cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(frame, contours, -1, (0,255,0), 2)
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        x,y,w,h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0), 2)
        winsound.Beep(500, 200)
    if cv2.waitKey(10) == ord('e'):
        break
    #cv.imshow('Spy', diff)
    #cv.imshow('Spy', grey)
    #cv.imshow('Spy', blur1)
    # cv.imshow('Spy', blur1)
    # cv.imshow('Spy', thresh)
    #cv.imshow('Spy', thresh1)
    cv2.imshow('Spy', frame)
