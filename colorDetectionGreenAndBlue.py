import cv2
def callback(_):
    pass

def init_trackbars_green():
    cv2.namedWindow('HSV Trackbars Green')    

    cv2.createTrackbar('LH', 'HSV Trackbars Green', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars Green', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars Green', 0, 255, callback)
    cv2.createTrackbar('UH', 'HSV Trackbars Green', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars Green', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars Green', 255, 255, callback)

def get_lower_hsv1():
    lower_hue1 = cv2.getTrackbarPos('LH', 'HSV Trackbars Green')
    lower_saturation1 = cv2.getTrackbarPos('LS', 'HSV Trackbars Green')
    lower_value1 = cv2.getTrackbarPos('LV', 'HSV Trackbars Green')
    return (lower_hue1, lower_saturation1, lower_value1)

def get_upper_hsv1():
    upper_hue1 = cv2.getTrackbarPos('UH', 'HSV Trackbars Green')
    upper_saturation1 = cv2.getTrackbarPos('US', 'HSV Trackbars Green')
    upper_value1 = cv2.getTrackbarPos('UV', 'HSV Trackbars Green')
    return (upper_hue1, upper_saturation1, upper_value1)

def init_trackbars_blue():
    cv2.namedWindow('HSV Trackbars Blue')    
 
    cv2.createTrackbar('LH', 'HSV Trackbars Blue', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars Blue', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars Blue', 0, 255, callback)
    cv2.createTrackbar('UH', 'HSV Trackbars Blue', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars Blue', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars Blue', 255, 255, callback)

def get_lower_hsv2():
    lower_hue2 = cv2.getTrackbarPos('LH', 'HSV Trackbars Blue')
    lower_saturation2 = cv2.getTrackbarPos('LS', 'HSV Trackbars Blue')
    lower_value2 = cv2.getTrackbarPos('LV', 'HSV Trackbars Blue')
    return (lower_hue2, lower_saturation2, lower_value2)

def get_upper_hsv2():
    upper_hue2 = cv2.getTrackbarPos('UH', 'HSV Trackbars Blue')
    upper_saturation2 = cv2.getTrackbarPos('US', 'HSV Trackbars Blue')
    upper_value2 = cv2.getTrackbarPos('UV', 'HSV Trackbars Blue')
    return (upper_hue2, upper_saturation2, upper_value2)

def main(capture):
    while True:
        ret, frame = capture.read()

        lower_hsv1 = get_lower_hsv1()
        upper_hsv1 = get_upper_hsv1()

        lower_hsv2 = get_lower_hsv2()
        upper_hsv2 = get_upper_hsv2()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      
        thresh_green = cv2.inRange(hsv, lower_hsv1, upper_hsv1)
        thresh_blue = cv2.inRange(hsv, lower_hsv2, upper_hsv2)

     
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh_green = cv2.morphologyEx(thresh_green, cv2.MORPH_OPEN, kernel)
        thresh_blue = cv2.morphologyEx(thresh_blue, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(thresh_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours2, _ = cv2.findContours(thresh_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest_contour = max(contours, key=cv2.contourArea)
     
            x, y, w, h = cv2.boundingRect(largest_contour)

            frame = cv2.putText(frame, 'Green', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)

        if contours2:
            largest_contour = max(contours2, key=cv2.contourArea)
     
            x, y, w, h = cv2.boundingRect(largest_contour)

            frame = cv2.putText(frame, 'BLUE', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

        # Detect Multi Object, Mendeteksi bangun datar, persegi persegi panjang, lingkaran, segitiga, war
        
        # Tampilkan frame
        cv2.imshow('Thresh Blue', thresh_blue)
        cv2.imshow('Thresh Green', thresh_green)
        cv2.imshow('Frame', frame)

        # Kondisi untuk end while loop
        if cv2.waitKey(1) == ord('q'):
            break
    
    frame.release()
    cv2.destroyAllWindows

# Entry Point
if __name__ == '__main__':
    init_trackbars_green()
    init_trackbars_blue()
    camera = cv2.VideoCapture(0)
    main(camera)
