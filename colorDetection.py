import cv2
def callback(_):
    pass

def init_trackbars():
    # Hue Saturation Value
    # Bikin Windows
    cv2.namedWindow('HSV Trackbars')    
    # Buat Trackbar
    cv2.createTrackbar('LH', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('LS', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('LV', 'HSV Trackbars', 0, 255, callback)
    cv2.createTrackbar('UH', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('US', 'HSV Trackbars', 255, 255, callback)
    cv2.createTrackbar('UV', 'HSV Trackbars', 255, 255, callback)

def get_lower_hsv():
    lower_hue = cv2.getTrackbarPos('LH', 'HSV Trackbars')
    lower_saturation = cv2.getTrackbarPos('LS', 'HSV Trackbars')
    lower_value = cv2.getTrackbarPos('LV', 'HSV Trackbars')
    return (lower_hue, lower_saturation, lower_value)

def get_upper_hsv():
    upper_hue = cv2.getTrackbarPos('UH', 'HSV Trackbars')
    upper_saturation = cv2.getTrackbarPos('US', 'HSV Trackbars')
    upper_value = cv2.getTrackbarPos('UV', 'HSV Trackbars')
    return (upper_hue, upper_saturation, upper_value)


def main(capture):
    while True:
        # print(capture.read())
        # Baca kamera
        ret, frame = capture.read()

        #frame = cv2.flip(frame, 1)
        #frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)

        lower_hsv = get_lower_hsv()
        upper_hsv = get_upper_hsv()

        print(lower_hsv)
        print(upper_hsv)

        # Convert warna dari BGR ke HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Get threshold /batas dengan cara filter warna dari lower & upper
        thresh = cv2.inRange(hsv, lower_hsv, upper_hsv)

        # Mengurangi noise hasil dari filter warna
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # Generate Kontur Object
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        # Ketika ada kontur / ada object => generate bounding box
        if contours:
            # Get kontur dengan ukuran terbesar
            largest_contour = max(contours, key=cv2.contourArea)
     
            # x dan y adalah koordinat, w & h adalah ukuran
            x, y, w, h = cv2.boundingRect(largest_contour)

            # Tampilkan rectange atau persegi
            frame = cv2.putText(frame, 'BLUE', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)

        # Detect Multi Object, Mendeteksi bangun datar, persegi persegi panjang, lingkaran, segitiga, war
        
        # Tampilkan frame
        cv2.imshow('Thresh', thresh)
        cv2.imshow('Frame', frame)

        # Kondisi untuk end while loop
        if cv2.waitKey(1) == ord('q'):
            break
    
    frame.release()
    cv2.destroyAllWindows

# Entry Point
if __name__ == '__main__':
    init_trackbars()
    camera = cv2.VideoCapture(0)
    main(camera)
