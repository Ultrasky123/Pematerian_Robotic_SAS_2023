import cv2

def main(capture):
    face_dataset = '/home/must/Materi ROBOTIC SAS/haarcascade_frontalface_default.xml'
    eye_dataset = '/home/must/Materi ROBOTIC SAS/haarcascade_eye.xml'
    smile_dataset = '/home/must/Materi ROBOTIC SAS/haarcascade_smile.xml'

    face_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)
    smile_cascade = cv2.CascadeClassifier(smile_dataset)

    while True:
        ret, frame = capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # Deteksi haar cascade
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        
        # Setiap muka di faces / yang terdeteksi
        for (x, y, w, h) in faces:
            # fungsi tengah
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,0), 3)
            #center = ((x + w//2, y + h//2))
            #frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 0), 2)

            face_roi = gray[y:y+h, x:x+w]

            smile_rects, rejectLevels, levelWeights = smile_cascade.detectMultiScale3(face_roi, 2.5, 20, outputRejectLevels=True)
                
            if len(levelWeights) == 0:
                cv2.putText(frame, "Not Smiling", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 3)
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
                #cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (0,0,255), 3)
            else:
            # if `levelWeights` is below 2, we classify this as "Not Smiling"
                if max(levelWeights) < 0.5:
                    cv2.putText(frame, "Not Smiling", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255), 3)
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
                    #cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (0,0,255), 3)
                    # otherwise, there is a smiling in the face ROI
                else:
                    cv2.putText(frame, "Smiling", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,255,0), 3)
                    cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 3)
                    #cv2.rectangle(frame, (x2,y2), (x2+w2, y2+h2), (0,255,0), 3)

            eyes = eye_cascade.detectMultiScale(face_roi)

            # Setiap mata yang terdeteksi
            for (x2, y2, w2, h2) in eyes:
                # Mata tengah
                eye_center = ((x + x2 + w2//2, y + y2 + h2//2))
                # simpan nilai jari jari dari mata yang terdeteksi
                radius = (int(round((w2 + h2) * 0.25)))
                # Tampilkan lingkaran
                #frame = cv2.circle(frame, eye_center, radius, (0, 225, 0), 2)
                

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) == ord('q'):
            break

    frame.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)
