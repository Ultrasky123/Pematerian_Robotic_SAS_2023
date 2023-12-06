import cv2

def callback(_):
    pass

def init_trackbars():
    cv2.namedWindow('Blue HSV Trackbars')
    cv2.createTrackbar('Blue LH', 'Blue HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('Blue LS', 'Blue HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('Blue LV', 'Blue HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('Blue UH', 'Blue HSV Trackbars', 130, 255, callback)
    cv2.createTrackbar('Blue US', 'Blue HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('Blue UV', 'Blue HSV Trackbars', 255, 255, callback)

    cv2.namedWindow('Red HSV Trackbars')
    cv2.createTrackbar('Red LH', 'Red HSV Trackbars', 115, 255, callback)
    cv2.createTrackbar('Red LS', 'Red HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('Red LV', 'Red HSV Trackbars', 100, 255, callback)
    cv2.createTrackbar('Red UH', 'Red HSV Trackbars', 180, 255, callback)
    cv2.createTrackbar('Red US', 'Red HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('Red UV', 'Red HSV Trackbars', 255, 255, callback)

def get_blue_lower_hsv():
    lower_hue = cv2.getTrackbarPos('Blue LH', 'Blue HSV Trackbars')
    lower_sat = cv2.getTrackbarPos('Blue LS', 'Blue HSV Trackbars')
    lower_val = cv2.getTrackbarPos('Blue LV', 'Blue HSV Trackbars')
    return (lower_hue, lower_sat, lower_val)

def get_blue_upper_hsv():
    upper_hue = cv2.getTrackbarPos('Blue UH', 'Blue HSV Trackbars')
    upper_sat = cv2.getTrackbarPos('Blue US', 'Blue HSV Trackbars')
    upper_val = cv2.getTrackbarPos('Blue UV', 'Blue HSV Trackbars')
    return (upper_hue, upper_sat, upper_val)

def get_red_lower_hsv():
    lower_hue = cv2.getTrackbarPos('Red LH', 'Red HSV Trackbars')
    lower_sat = cv2.getTrackbarPos('Red LS', 'Red HSV Trackbars')
    lower_val = cv2.getTrackbarPos('Red LV', 'Red HSV Trackbars')
    return (lower_hue, lower_sat, lower_val)

def get_red_upper_hsv():
    upper_hue = cv2.getTrackbarPos('Red UH', 'Red HSV Trackbars')
    upper_sat = cv2.getTrackbarPos('Red US', 'Red HSV Trackbars')
    upper_val = cv2.getTrackbarPos('Red UV', 'Red HSV Trackbars')
    return (upper_hue, upper_sat, upper_val)

import cv2

def main(capture):
    while True:
        ret, frame = capture.read()

        blue_lower_hsv = get_blue_lower_hsv()
        blue_upper_hsv = get_blue_upper_hsv()
        red_lower_hsv = get_red_lower_hsv()
        red_upper_hsv = get_red_upper_hsv()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        blue_mask = cv2.inRange(hsv, blue_lower_hsv, blue_upper_hsv)
        red_mask = cv2.inRange(hsv, red_lower_hsv, red_upper_hsv)

        combined_mask = cv2.bitwise_or(blue_mask, red_mask)

        contours, _ = cv2.findContours(combined_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)
                
                if blue_lower_hsv[0] <= hsv[y + h // 2][x + w // 2][0] <= blue_upper_hsv[0]:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                    cv2.putText(frame, 'Blue', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
                    
                elif red_lower_hsv[0] <= hsv[y + h // 2][x + w // 2][0] <= red_upper_hsv[0]:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.putText(frame, 'Red', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    init_trackbars()
    camera = cv2.VideoCapture(0)
    main(camera)
