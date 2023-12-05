# basis opencv
import cv2
import numpy as np

def callback(_):
    pass

def init_trackbars():
    # HSV(HUE,SATURATION,VALUE)
    cv2.namedWindow('HSV Trackbars')
    cv2.createTrackbar('LH','HSV Trackbars',0,255, callback)
    cv2.createTrackbar('LS','HSV Trackbars',0,255, callback)
    cv2.createTrackbar('LV','HSV Trackbars',0,255, callback)
    cv2.createTrackbar('UH','HSV Trackbars',255,255, callback)
    cv2.createTrackbar('US','HSV Trackbars',255,255, callback)
    cv2.createTrackbar('UV','HSV Trackbars',255,255, callback)

def get_lower_hsv():
    lower_hue = cv2.getTrackbarPos('LH','HSV Trackbars')
    lower_sat = cv2.getTrackbarPos('LS','HSV Trackbars')
    lower_val = cv2.getTrackbarPos('LV','HSV Trackbars')
    return(lower_hue,lower_sat,lower_val)

def get_upper_hsv():
    upper_hue = cv2.getTrackbarPos('UH','HSV Trackbars')
    upper_sat = cv2.getTrackbarPos('US','HSV Trackbars')
    upper_val = cv2.getTrackbarPos('UV','HSV Trackbars')
    return(upper_hue,upper_sat,upper_val)

lower_blue = np.array([93,0,34])
upper_blue = np.array([155,255,255])
lower_green = np.array([27,26,92])
upper_green = np.array([90,255,255])
lower_red = np.array([121,129,0])
upper_red = np.array([255,255,255])

def main(capture):
    while True:
        # print(capture.read())
        # baca kamera
        ret, frame = capture.read()
        
        # simpan nilai HSV
        lower_hsv = get_lower_hsv()
        upper_hsv = get_upper_hsv()
        # print(lower_hsv)
        # print(upper_hsv)

        # Konvert warna dari BGR ke HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        thresh = cv2.inRange(hsv,lower_hsv, upper_hsv)

        # mengurangi noise hasil dari filter warna
        kernel = np.ones((5,5), np.uint8)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # generate kontur objek
        image =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(image,lower_green,upper_green)
        mask2 = cv2.inRange(image,lower_blue,upper_blue)
        mask3 = cv2.inRange(image,lower_red,upper_red)
        mask1 = cv2.erode(mask1,kernel)
        mask2 = cv2.erode(mask2,kernel)
        mask3 = cv2.erode(mask3,kernel)
        contours, _ = cv2.findContours(mask1,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours1, _ = cv2.findContours(mask2,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours2, _ = cv2.findContours(mask3,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # ketika ada warna hijau
        if len(contours)!= 0:
            for contour in contours:
                if cv2.contourArea(contour)>500:
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(frame,(x,y),(w+x,h+y), (0,255,0),2)
                    cv2.putText(frame,'GREEN',(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),2)
        # ketika ada warna biru
        if len(contours1)!= 0:
            for contour in contours1:
                if cv2.contourArea(contour)>500:
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(frame,(x,y),(w+x,h+y), (255,0,0),2)
                    cv2.putText(frame,'BLUE',(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,0),2)
        # ketika ada warna merah
        if len(contours2)!= 0:
            for contour in contours2:
                if cv2.contourArea(contour)>500:
                    x,y,w,h = cv2.boundingRect(contour)
                    cv2.rectangle(frame,(x,y),(w+x,h+y), (0,0,255),2)
                    cv2.putText(frame,'RED',(x,y),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)


        # tampilkan frame
        cv2.imshow('mask',mask1+mask2+mask3)
        cv2.imshow('Frame',frame)

        # kondisi untuk end while loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # lepas cam & destroy windows
    frame.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    init_trackbars()
    camera = cv2.VideoCapture(0)
    main(camera)