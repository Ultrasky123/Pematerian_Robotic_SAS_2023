import cv2

def callback(_) :
    pass

def init_trackbars():
    #HSV 
    # Bikin Window
    cv2.namedWindow('HSV Trackbar')
    cv2.createTrackbar('LH', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbar', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbar', 0, 255, callback)

    cv2.createTrackbar('UH', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbar', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbar', 255, 255, callback)

def get_lower_hsv() :
    lower_hue= cv2.getTrackbarPos('LH', 'HSV Trackbar')
    lower_sat= cv2.getTrackbarPos('LS', 'HSV Trackbar')
    lower_val= cv2.getTrackbarPos('LV', 'HSV Trackbar')

    return (lower_hue, lower_sat, lower_val)

def get_upper_hsv() :
    upper_hue= cv2.getTrackbarPos('UH', 'HSV Trackbar')
    upper_sat= cv2.getTrackbarPos('US', 'HSV Trackbar')
    upper_val= cv2.getTrackbarPos('UV', 'HSV Trackbar')

    return (upper_hue, upper_sat, upper_val)



def main(capture) :

    while True :
        # print(capture.read())
        ret, frame = capture.read()

        lowerHSV = get_lower_hsv()
        upperHSV = get_upper_hsv()

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
            
    frame.release()
    cv2.destroyAllWindows()


if __name__ == '__main__' :
    init_trackbars()

    camera = cv2.VideoCapture(0)
    main(camera)