import cv2
import numpy as np
def callback(_):
    pass

def init_trackbars_green():
    cv2.namedWindow('HSV Trackbars Green')    

    cv2.createTrackbar('LH', 'HSV Trackbars Green', 27, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars Green', 26, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars Green', 92, 255, callback)
    cv2.createTrackbar('UH', 'HSV Trackbars Green', 90, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars Green', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars Green', 255, 255, callback)

def get_lower_hsv1():
    lower_h1 = cv2.getTrackbarPos('LH', 'HSV Trackbars Green')
    lower_s1 = cv2.getTrackbarPos('LS', 'HSV Trackbars Green')
    lower_v1 = cv2.getTrackbarPos('LV', 'HSV Trackbars Green')
    return (lower_h1, lower_s1, lower_v1)

def get_upper_hsv1():
    upper_h1 = cv2.getTrackbarPos('UH', 'HSV Trackbars Green')
    upper_s1 = cv2.getTrackbarPos('US', 'HSV Trackbars Green')
    upper_v1 = cv2.getTrackbarPos('UV', 'HSV Trackbars Green')
    return (upper_h1, upper_s1, upper_v1)

def init_trackbars_blue():
    cv2.namedWindow('HSV Trackbars Blue')    
 
    cv2.createTrackbar('LH', 'HSV Trackbars Blue', 93, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars Blue', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars Blue', 34, 255, callback)
    cv2.createTrackbar('UH', 'HSV Trackbars Blue', 155, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars Blue', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars Blue', 255, 255, callback)

def get_lower_hsv2():
    lower_h2 = cv2.getTrackbarPos('LH', 'HSV Trackbars Blue')
    lower_s2 = cv2.getTrackbarPos('LS', 'HSV Trackbars Blue')
    lower_v2 = cv2.getTrackbarPos('LV', 'HSV Trackbars Blue')
    return (lower_h2, lower_s2, lower_v2)

def get_upper_hsv2():
    upper_h2 = cv2.getTrackbarPos('UH', 'HSV Trackbars Blue')
    upper_s2 = cv2.getTrackbarPos('US', 'HSV Trackbars Blue')
    upper_v2 = cv2.getTrackbarPos('UV', 'HSV Trackbars Blue')
    return (upper_h2, upper_s2, upper_v2)


def init_trackbars_Red():
    cv2.namedWindow('HSV Trackbars Red')    
 
    cv2.createTrackbar('LH', 'HSV Trackbars Red', 143, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars Red', 87, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars Red', 0, 255, callback)
    cv2.createTrackbar('UH', 'HSV Trackbars Red', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars Red', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars Red', 255, 255, callback)

def get_lower_hsv3():
    lower_h3 = cv2.getTrackbarPos('LH', 'HSV Trackbars Red')
    lower_s3 = cv2.getTrackbarPos('LS', 'HSV Trackbars Red')
    lower_v3 = cv2.getTrackbarPos('LV', 'HSV Trackbars Red')
    return (lower_h3, lower_s3, lower_v3)

def get_upper_hsv3():
    upper_h3 = cv2.getTrackbarPos('UH', 'HSV Trackbars Red')
    upper_s3 = cv2.getTrackbarPos('US', 'HSV Trackbars Red')
    upper_v3 = cv2.getTrackbarPos('UV', 'HSV Trackbars Red')
    return (upper_h3, upper_s3, upper_v3)

def main(capture):
    while True:
        ret, frame = capture.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        lower_hsv1 = get_lower_hsv1()
        upper_hsv1 = get_upper_hsv1()
        lower_hsv2 = get_lower_hsv2()
        upper_hsv2 = get_upper_hsv2()
        lower_hsv3 = get_lower_hsv3()
        upper_hsv3 = get_upper_hsv3()

        mask1 = cv2.inRange(hsv, lower_hsv1, upper_hsv1)
        mask2 = cv2.inRange(hsv, lower_hsv2, upper_hsv2)
        mask3 = cv2.inRange(hsv, lower_hsv3, upper_hsv3)
        kernel = np.ones((5,5), np.uint8)
        mask1 = cv2.erode(mask1,kernel)
        mask2 = cv2.erode(mask2,kernel)
        mask3 = cv2.erode(mask3,kernel)

        contours1, _ = cv2.findContours(mask1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours2, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours3, _ = cv2.findContours(mask3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours1:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt,0.02 *cv2.arcLength(cnt,True),True)
            if area > 400:
                cv2.drawContours(frame, [approx], 0 ,(0,0,0),5)
                x,y,w,h = cv2.boundingRect(cnt)
                if len(approx) == 3:
                    cv2.putText(frame,"Green Triangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                elif len(approx) == 4:
                    ratio = float(w)/h
                    if ratio >= 0.9 and ratio <= 1.1 :
                        cv2.putText(frame,"Green Square",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                    else:
                        cv2.putText(frame,"Green Rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                elif 8 <= len(approx) < 15 :
                    cv2.putText(frame,"Green Circle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                cv2.rectangle(frame,(x,y),(w+x,h+y), (0,255,0),2)

        for cnt in contours2:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt,0.02 *cv2.arcLength(cnt,True),True)
            if area > 400:
                cv2.drawContours(frame, [approx], 0 ,(0,0,0),5)
                x,y,w,h = cv2.boundingRect(cnt)
                if len(approx) == 3:
                    cv2.putText(frame,"Blue Triangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                elif len(approx) == 4:
                    ratio = float(w)/h
                    if ratio >= 0.9 and ratio <= 1.1 :
                        cv2.putText(frame,"Blue Square",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                    else:
                        cv2.putText(frame,"Blue Rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                elif 8 <= len(approx) < 15 :
                    cv2.putText(frame,"Blue Circle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                cv2.rectangle(frame,(x,y),(w+x,h+y), (255,0,0),2)

        for cnt in contours3:
            area = cv2.contourArea(cnt)
            approx = cv2.approxPolyDP(cnt,0.02 *cv2.arcLength(cnt,True),True)
            if area > 400:
                cv2.drawContours(frame, [approx], 0 ,(0,0,0),5)
                x,y,w,h = cv2.boundingRect(cnt)
                if len(approx) == 3:
                    cv2.putText(frame,"Red Triangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                elif len(approx) == 4:
                    ratio = float(w)/h
                    if ratio >= 0.9 and ratio <= 1.1 :
                        cv2.putText(frame,"Red Square",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                    else:
                        cv2.putText(frame,"Red Rectangle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                elif 8 <= len(approx) < 15 :
                    cv2.putText(frame,"Red Circle",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),2)
                cv2.rectangle(frame,(x,y),(w+x,h+y), (0,0,255),2)

        # Tampilkan frame
        cv2.imshow("mask",mask1)
        cv2.imshow('Frame',frame)
        # Kondisi untuk end while loop
        if cv2.waitKey(1) == ord('q'):
            break
    
    frame.release()
    cv2.destroyAllWindows

# Entry Point
if __name__ == '__main__':
    init_trackbars_green()
    init_trackbars_blue()
    init_trackbars_Red()

    camera = cv2.VideoCapture(0)
    main(camera)