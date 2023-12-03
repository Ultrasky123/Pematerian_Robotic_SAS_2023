import cv2
import numpy as np
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

def main():
    img = cv2.imread('bentuk.png', -1)
    img = cv2.resize(img, (0,0), fx=0.3, fy= 0.3)
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    while True:
        imgContour = img.copy()
        lower_hsv1 = get_lower_hsv1()
        upper_hsv1 = get_upper_hsv1()

        lower_hsv2 = get_lower_hsv2()
        upper_hsv2 = get_upper_hsv2()

        print(lower_hsv1)
        print(upper_hsv1)
        print(lower_hsv2)
        print(upper_hsv2)


        thresh_green = cv2.inRange(imgGray, lower_hsv1, upper_hsv1)
        thresh_blue = cv2.inRange(imgGray, lower_hsv2, upper_hsv2)

        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
        thresh_green = cv2.morphologyEx(thresh_green, cv2.MORPH_OPEN, kernel)
        thresh_blue = cv2.morphologyEx(thresh_blue, cv2.MORPH_OPEN, kernel)

        imgCanny1 = cv2.Canny(thresh_green, 50, 50)
        imgCanny2 = cv2.Canny(thresh_blue, 50, 50)

        contours, _ = cv2.findContours(imgCanny1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours2, _ = cv2.findContours(imgCanny2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour1 in contours:
            area = cv2.contourArea(contour1)
            # print(area)
            if area > 1000:
                #cv2.drawContours(imgContour, contour1, -1, (0, 0, 0), 3)
                peri = cv2.arcLength(contour1, True)
                approx = cv2.approxPolyDP(contour1, 0.02*peri, True)
                #print(approx)
                sudutObject = len(approx)
            
                x, y, w, h = cv2.boundingRect(approx)

                if sudutObject == 3:
                    tipeObject = 'Segitiga Hijau'
                elif sudutObject == 4:
                    rasio = w/float(h)
                    if rasio > 0.9 and rasio < 1.1:
                        tipeObject = 'Persegi Hijau'
                    else :
                        tipeObject = 'Persegi Panjang Hijau'
                elif sudutObject == 8:
                    tipeObject = 'Lingkaran Hijau'
                else:
                    tipeObject = 'Benda lain'
                
                cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0,255,0), 3)
                cv2.putText(imgContour, tipeObject, (x+10, y+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 1, cv2.LINE_AA)

        for contour2 in contours2:
            area = cv2.contourArea(contour2)
            # print(area)
            if area > 1000:
                #cv2.drawContours(imgContour, contour2, -1, (0, 0, 0), 3)
                peri = cv2.arcLength(contour2, True)
                approx = cv2.approxPolyDP(contour2, 0.02*peri, True)
                #print(approx)
                sudutObject = len(approx)
            
                x, y, w, h = cv2.boundingRect(approx)

                if sudutObject == 3:
                    tipeObject = 'Segitiga Biru' 
                elif sudutObject == 4:
                    rasio = w/float(h)
                    if rasio > 0.9 and rasio < 1.1:
                        tipeObject = 'Persegi Biru'
                    else :
                        tipeObject = 'Persegi Panjang Biru'
                elif sudutObject == 8:
                    tipeObject = 'Lingkaran Biru'
                else:
                    tipeObject = 'Benda lain'
                
                cv2.rectangle(imgContour, (x,y), (x+w, y+h), (255,0,0), 3)
                cv2.putText(imgContour, tipeObject, (x+10, y+30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,0,0), 1, cv2.LINE_AA)

        cv2.imshow('Image contour', imgContour)
        cv2.imshow('Thresh Green', thresh_green)
        cv2.imshow('Thresh Blue', thresh_blue)
        #cv2.imshow('Image Canny Blue', imgCanny2)
        #cv2.imshow('Image Canny Green', imgCanny1)
        

        if cv2.waitKey(1) == ord('q'):
            break
        

if __name__ == '__main__':
    init_trackbars_green()
    init_trackbars_blue()
    main()