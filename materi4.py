# basis opencv
import cv2

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
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # generate kontur objek
        contours, _ = cv2.findContours(thresh,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # ketika ada kontur / ada objek => generat bounding box
        if contours:
            # get kontur dengan ukuran terbesar
            largest_contour =max(contours, key=cv2.contourArea)
            #  x & y = koordinat / w & h = ukuran
            x,y,w,h = cv2.boundingRect(largest_contour)
            # tampilkan kotak
            cv2.rectangle(frame,(x,y),(w+x,h+y), (0,0,255),2)

        # tampilkan frame
        cv2.imshow('Thresh',thresh)
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