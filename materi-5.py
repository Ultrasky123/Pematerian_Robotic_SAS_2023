# object detection

import cv2

def main(capture):
    face_dataset = '/home/wijaya/assets/haarcascade_frontalface_default.xml'
    eye_dataset='/home/wijaya/assets/haarcascade_eye.xml'
    smile_dataset ='/home/wijaya/assets/smile_cascade.xml'
    upperbody_dataset = '/home/wijaya/assets/haarcascade_upperbody.xml'

    face_cascade =cv2.CascadeClassifier(face_dataset)
    # eye_cascade =cv2.CascadeClassifier(eye_dataset)
    smile_cascade =cv2.CascadeClassifier(smile_dataset)
    upperbody_cascade =cv2.CascadeClassifier(upperbody_dataset)

    while True:
        ret, frame = capture.read()

        # ubah warna dari BGR ke Grayscale
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # deteksi haar cascade
        upperbody = upperbody_cascade.detectMultiScale(gray)
        faces = face_cascade.detectMultiScale(gray)

        for (x3,y3,h3,w3) in upperbody :
        # untuk setiap wajah yang terdeteksi
            for (x,y,w,h) in faces :
                smile = smile_cascade.detectMultiScale(gray)
                for (a,b,c,d) in smile :
                    if len(smile) >= 30:
                        cv2.putText(frame,f"smile{len(smile)}",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
                        cv2.rectangle(frame,(x,y),(w+x,h+y), (0,255,0),2)
                    else:
                        cv2.putText(frame,f"no smile{len(smile)}",(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
                        cv2.rectangle(frame,(x,y),(w+x,h+y), (0,0,255),2)

        cv2.imshow('Frame',frame)

        # kondisi untuk end while loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # lepas cam & destroy windows
    frame.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)