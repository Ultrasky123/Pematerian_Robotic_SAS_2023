import cv2

def main(capture):
    face_dataset = '/home/must/Materi ROBOTIC SAS/haarcascade_frontalface_default.xml'
    eye_dataset = '/home/must/Materi ROBOTIC SAS/haarcascade_eye.xml'
    upperbody_dataset = '/home/must/Materi ROBOTIC SAS/haarcascade_upperbody.xml'
    smile_dataset = '/home/must/Materi ROBOTIC SAS/haarcascade_smile.xml'

    face_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)
    upperbody_cascade = cv2.CascadeClassifier(upperbody_dataset)
    smile_cascade = cv2.CascadeClassifier(smile_dataset)

    while True:
        ret, frame = capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        upperbodies = upperbody_cascade.detectMultiScale(gray)
        print(upperbodies)

        for (x, y, w, h) in upperbodies:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), 3)
            upperbody_roi = gray[y:y+h, x:x+w]
            faces = face_cascade.detectMultiScale(upperbody_roi)

            for (x2, y2, w2, h2) in faces:
                cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (255,255,255), 3)
                face_roi = gray[y2:y2+h2, x2:x2+w2] 
                smile_rects, rejectLevels, levelWeights = smile_cascade.detectMultiScale3(face_roi, 2.5, 20, outputRejectLevels=True)
                
                if len(levelWeights) == 0:
                    cv2.putText(frame, "Not Smiling", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 3)
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
                    cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (0,0,255), 3)
                else:
                    # if `levelWeights` is below 2, we classify this as "Not Smiling"
                    if max(levelWeights) < 2:
                        cv2.putText(frame, "Not Smiling", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 3)
                        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
                        cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (0,0,255), 3)
                    # otherwise, there is a smiling in the face ROI
                    else:
                        cv2.putText(frame, "Smiling", (x2, y2), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 3)
                        cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
                        cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (0,255,0), 3)
                        
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    frame.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)
