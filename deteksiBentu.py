import cv2

def getContour(imgCanny, imgContour):
    contours, heirarcy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        # print(area)
        if area > 1000:
            cv2.drawContours(imgContour, contour, -1, (0, 0, 0), 3)
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02*peri, True)
            #print(approx)
            sudutObject = len(approx)
        
            x, y, w, h = cv2.boundingRect(approx)

            if sudutObject == 3:
                tipeObject = 'Segitiga'
            elif sudutObject == 4:
                rasio = w/float(h)
                if rasio > 0.9 and rasio < 1.1:
                    tipeObject = 'Persegi'
                else :
                    tipeObject = 'Persegi Panjang'
            elif sudutObject == 8:
                tipeObject = 'Lingkaran'
            else:
                tipeObject = 'Benda lain'
            
            cv2.putText(imgContour, tipeObject, (x+10, y+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2, cv2.LINE_AA)

def main():
    img = cv2.imread('bentuk.png', -1)
    img = cv2.resize(img, (0,0), fx=0.45, fy= 0.45)
    imgContour = img.copy()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    
    getContour(imgCanny, imgContour)

    cv2.imshow('img contour', imgContour)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

