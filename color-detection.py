import cv2

def callback():
    pass

def init_trackbars():
    print(True)
    #HVS 
    cv2.namedWindow('HSV Trackbars')
    cv2.createTrackbar('LH', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('UH', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars', 255, 255, callback)

def get_lower_hvs():
    lower_hue = cv2.getTrackbarPos('LH','HSV Trackbars')  
    lower_sat= cv2.getTrackbarPos('LH','HSV Trackbars')  
    lower_val = cv2.getTrackbarPos('LH','HSV Trackbars')   
    return (lower_hue, lower_sat, lower_val) 

def get_upper_hvs():
    upper_hue = cv2.getTrackbarPos('UH','HSV Trackbars')  
    upper_sat = cv2.getTrackbarPos('US','HSV Trackbars')  
    upper_val = cv2.getTrackbarPos('UV','HSV Trackbars')    
    return(upper_hue, upper_sat, upper_val)


def main(capture):
    while True:
        ret, frame =capture.read()

        lower_hvs = get_lower_hvs()
        upper_hsv = get_upper_hvs()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        thresh = cv2.inRange(hsv, lower_hvs, upper_hsv)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        
        if  contours:
            largest_contour = max(contours[0], key=cv2.contourArea)
           

            x,y,w,h = cv2.boundingRect(largest_contour)

            cv2.putText(frame, 'BLUE', (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
            cv2.rectangle(frame, (x,y), (w+x, h+y),(255, 0, 0), 2 )

        cv2.imshow('Thresh', thresh)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    frame.release()
    cv2.destroyAllWindows()

#Entry Point/ PORTAL
if __name__ =='__main__':
    print(True)
    init_trackbars()
    camera = cv2.VideoCapture(0)
    print(True)
    main(camera)

   
