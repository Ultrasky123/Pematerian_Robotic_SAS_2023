import cv2

def callback(_):
    pass

def init_trackbars():
    cv2.namedWindow('HSV Trackbars')
    cv2.createTrackbar('LH', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('UH', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars', 255, 255, callback)

def get_lower_hsv():
    lower_hue = cv2.getTrackbarPos('LH', 'HSV Trackbars')
    lower_sat = cv2.getTrackbarPos('LS', 'HSV Trackbars')
    lower_val = cv2.getTrackbarPos('LV', 'HSV Trackbars')
    return (lower_hue, lower_sat, lower_val)

def get_upper_hsv():
    upper_hue = cv2.getTrackbarPos('UH', 'HSV Trackbars')
    upper_sat = cv2.getTrackbarPos('US', 'HSV Trackbars')
    upper_val = cv2.getTrackbarPos('UV', 'HSV Trackbars')
    return (upper_hue, upper_sat, upper_val)

def main(capture):
    while True:
        ret, frame = capture.read()

        lower_hsv = get_lower_hsv()
        upper_hsv = get_upper_hsv()

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        thresh = cv2.inRange(hsv, lower_hsv, upper_hsv)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            area = cv2.contourArea(contour)
            if area > 500:  # Filter contours by area to avoid noise
                perimeter = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)

                # Detect and label shapes based on the number of vertices
                if len(approx) == 3:
                    shape = "Triangle"
                elif len(approx) == 4:
                    shape = "Rectangle"
                else:
                    shape = "Circle"

                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
                cv2.putText(frame, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

        cv2.imshow('Thresh', thresh)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    init_trackbars()
    camera = cv2.VideoCapture(0)
    main(camera)
