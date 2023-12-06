import cv2

def callback(_):
    pass

def init_trackbars():
    cv2.namedWindow('HSV Trackbars')
    cv2.createTrackbar('LH_Blue', 'HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('LS_Blue', 'HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('LV_Blue', 'HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('UH_Blue', 'HSV Trackbars', 130, 255, callback)
    cv2.createTrackbar('US_Blue', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('UV_Blue', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('LH_Red', 'HSV Trackbars', 115, 255, callback)
    cv2.createTrackbar('LS_Red', 'HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('LV_Red', 'HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('UH_Red', 'HSV Trackbars', 180, 255, callback)
    cv2.createTrackbar('US_Red', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('UV_Red', 'HSV Trackbars', 255, 255, callback)

def get_hsv_values(color):
    lower_hue = cv2.getTrackbarPos(f'LH_{color}', 'HSV Trackbars')
    lower_sat = cv2.getTrackbarPos(f'LS_{color}', 'HSV Trackbars')
    lower_val = cv2.getTrackbarPos(f'LV_{color}', 'HSV Trackbars')
    upper_hue = cv2.getTrackbarPos(f'UH_{color}', 'HSV Trackbars')
    upper_sat = cv2.getTrackbarPos(f'US_{color}', 'HSV Trackbars')
    upper_val = cv2.getTrackbarPos(f'UV_{color}', 'HSV Trackbars')
    return (lower_hue, lower_sat, lower_val), (upper_hue, upper_sat, upper_val)

def detect_shape(contour):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)

    if len(approx) == 3:
        return "Triangle"
    elif len(approx) == 4:
        return "Rectangle"
    else:
        return "Circle"

def main(capture):
    while True:
        ret, frame = capture.read()

        blue_lower_hsv, blue_upper_hsv = get_hsv_values('Blue')
        red_lower_hsv = (cv2.getTrackbarPos('LH_Red', 'HSV Trackbars'), cv2.getTrackbarPos('LS_Red', 'HSV Trackbars'), cv2.getTrackbarPos('LV_Red', 'HSV Trackbars'))
        red_upper_hsv = (cv2.getTrackbarPos('UH_Red', 'HSV Trackbars'), cv2.getTrackbarPos('US_Red', 'HSV Trackbars'), cv2.getTrackbarPos('UV_Red', 'HSV Trackbars'))

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        blue_mask = cv2.inRange(hsv, blue_lower_hsv, blue_upper_hsv)
        red_mask = cv2.inRange(hsv, red_lower_hsv, red_upper_hsv)

        contours_blue, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_red, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours_blue:
            area = cv2.contourArea(contour)
            if area > 500: 
                shape = detect_shape(contour)
                color = "Blue"
                
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, f"{color} {shape}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        for contour in contours_red:
            area = cv2.contourArea(contour)
            if area > 500:  
                shape = detect_shape(contour)
                color = "Red"
                
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(frame, f"{color} {shape}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

        cv2.imshow('Blue Mask', blue_mask)
        cv2.imshow('Red Mask', red_mask)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    init_trackbars()
    camera = cv2.VideoCapture(0)
    main(camera)
