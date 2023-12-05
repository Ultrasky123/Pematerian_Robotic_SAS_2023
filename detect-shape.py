# basis opencv
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

def callback(_):
    pass
    
cv2.namedWindow('HSV Trackbars')
cv2.createTrackbar('LH','HSV Trackbars',29,255, callback)
cv2.createTrackbar('LS','HSV Trackbars',34,255, callback)
cv2.createTrackbar('LV','HSV Trackbars',60,255, callback)
cv2.createTrackbar('UH','HSV Trackbars',255,255, callback)
cv2.createTrackbar('US','HSV Trackbars',255,255, callback)
cv2.createTrackbar('UV','HSV Trackbars',255,255, callback)


while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_hue = cv2.getTrackbarPos('LH','HSV Trackbars')
    lower_sat = cv2.getTrackbarPos('LS','HSV Trackbars')
    lower_val = cv2.getTrackbarPos('LV','HSV Trackbars')
    upper_hue = cv2.getTrackbarPos('UH','HSV Trackbars')
    upper_sat = cv2.getTrackbarPos('US','HSV Trackbars')
    upper_val = cv2.getTrackbarPos('UV','HSV Trackbars')

    lower = np.array([lower_hue,lower_sat,lower_val])
    upper = np.array([upper_hue,upper_sat,upper_val])
    mask = cv2.inRange(hsv,lower,upper)
    kernel = np.ones((5,5), np.uint8)
    mask = cv2.erode(mask,kernel)

    contours, _ = cv2.findContours(mask,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt,0.02 *cv2.arcLength(cnt,True),True)

        if area > 400:
            cv2.drawContours(frame, [approx], 0 ,(0,0,0),5)
            x,y,w,h = cv2.boundingRect(cnt)
            if len(approx) == 3:
                cv2.putText(frame,"Triangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
            elif len(approx) == 4:
                ratio = float(w)/h
                if ratio >= 0.9 and ratio <= 1.1 :
                    cv2.putText(frame,"Square",(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
                else:
                    cv2.putText(frame,"Rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
            elif 6 <= len(approx) < 15 :
                cv2.putText(frame,"Circle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),2)
        
        # print(len(approx))
        # tampilkan frame
    cv2.imshow("mask",mask)
    cv2.imshow('Frame',frame)

        # ko ndisi untuk end while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # lepas cam & destroy windows
frame.release()
cv2.destroyAllWindows()