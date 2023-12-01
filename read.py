#import cv2 as cv

# Membaca photo 
#img = cv.imread('Photos/Cat.jpeg')

#cv.imshow('Cat', img)

#cv.waitKey(0)

import cv2 as cv

# Membaca Video
capture = cv.VideoCapture('Photos/Ambatukam.mp4')

while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.realese()
cv.destroyAllWindows()


cv.waitKey(0)