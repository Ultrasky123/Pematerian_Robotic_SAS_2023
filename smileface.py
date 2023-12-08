import cv2

def main(capture):
    face_dataset = '/home/rico/sasrobotics/opencv_asset/haarcascade_frontalcatface.xml'
    smile_dataset = '/home/rico/sasrobotics/opencv_asset/haarcascade_smile.xml'
    upper_dataset = '/home/rico/sasrobotics/opencv_asset/haarcascade_upperbody.xml'

    face_cascade = cv2.CascadeClassifier(face_dataset)
    smile_cascade = cv2.CascadeClassifier(smile_dataset)
    upper_cascade = cv2.CascadeClassifier(upper_dataset)

    while True:
        ret, frame = capture.read()

        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        upper_bodies = upper_cascade.detectMultiScale(gray, scaleFactor=1.05)

        for (x, y, w, h) in upper_bodies:

            upper_roi = gray[y:y+h, x:x+w]
            
            faces = face_cascade.detectMultiScale(upper_roi, scaleFactor=1.05, minNeighbors=1, flags=0)

            for (x2, y2, w2, h2) in faces:
                cv2.rectangle(frame, (x + x2, y + y2), (x + x2 + w2, y + y2 + h2), (0, 0, 255), 2)
                cv2.putText(frame, 'face', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                face_roi = gray[y+y2:y+y2+h2, x+x2:x+x2+w2]

                smile = smile_cascade.detectMultiScale(face_roi, scaleFactor=1.05)

                for (x3, y3, w3, h3) in smile:
                    cv2.rectangle(frame, (x + x2, y + y2), (x + x2 + w2, y + y2 + h2), (0, 255, 0), 2)
                    cv2.putText(frame, 'smile', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)
