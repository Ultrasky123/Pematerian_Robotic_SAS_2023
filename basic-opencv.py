import cv2

def main(capture):
    while True:
        #print(capture.read())
        #Baca Kamera
        ret, frame =capture.read()

        #Tampilkan Frame
        cv2.imshow('Frame', frame)

        #kondisi untuk end while loop 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #lepas cam & destory windows
    frame.release()
    cv2.destroyAllWindows()

if __name__ =='__main__':
    #Get data camera
    camera = cv2.VideoCapture(0)
    main(camera)