import cv2



def main(capture) :

    face_dataset = '/home/aswangga/Materi Robotic/haarcascade_frontalface_default.xml'
    eye_dataset = '/home/aswangga/Materi Robotic/haarcascade_eye.xml'

    fase_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)

    while True :
        # print(capture.read())
        ret, frame = capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)


## Deteksi Haar cascade
        faces = fase_cascade.detectMultiScale(gray)
        # Untuk setiap wajah yang terdeteksi
        for (x, y, w, h) in faces :
            # Simpan koordinat titik tengah wajah
            center = ((x + w //2, y + h //2))

            # Tampilkan lingkaran
            frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0,360, (255, 0, 0), 2)

            # Tentukan wilayah awajah yang terdeteksi
            face_roi = gray[y:y+h, x:x+w]

            print(face_roi)


            eyes = eye_cascade.detectMultiScale(face_roi)

            # Untuk Setiap Mata Yang terdeteksi

            for (x2, y2, w2, h2) in eyes :
                # Tentukan koordinat tengah mata
                eye_center = (x+x2+w2//2, y + y2 + h2//2)
                # Simpan nilai jari2 dari mata yang terdeteksi
                radius = int(round((w2+h2) * 0.25))

                # Tampilkan lingkaran

                frame = cv2.circle(frame, eye_center, radius, (0, 255, 0), 2)

        print(faces)

        cv2.imshow('Frame', frame)
        cv2.imshow('GRAY', gray)

        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
            
    frame.release()
    cv2.destroyAllWindows()


if __name__ == '__main__' :


    camera = cv2.VideoCapture(0)
    main(camera)