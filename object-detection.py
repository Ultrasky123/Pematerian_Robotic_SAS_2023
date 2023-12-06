import cv2

def main(capture):
    face_dataset = '/home/aryayudistira/Materi Robotic SAS/assets/haarcascade_frontalcatface.xml'
    eye_dataset = '/home/aryayudistira/Materi Robotic SAS/assets/haarcascade_eye.xml'

    face_cascade = cv2.CascadeClassifier(face_dataset)
    eye_cascade = cv2.CascadeClassifier(eye_dataset)

    while True:
        # print(capture.read())
        # Baca kamera
        ret, frame = capture.read()

        #Ubah warna dari BGR ke Grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)

        # Deteksi haar cascade
        faces = face_cascade.detectMultiScale(gray)

        # Untuk setiap wajah yang terdeteksi
        for (x, y, w, h) in faces:
            # SImpan koordinat titik tengah wajah
            center = (x + w//2, y + h//2)

            # Tampilkan lingkaran
            frame = cv2.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 0), 2)

            # Tentukan wilayah wajah yang terdeteksi
            face_roi = gray[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(gray)

            #Untuk setiap mata yang terdeteksi
            for (x2, y2, w2, h2) in eyes:

                # Simpan Tentuukan koordinat titik tengah dari mata yang terdeteksi
                eye_center = (x + x2 + w2//2, y + y2 + h2//2)

                # Simpan nilai jari jari dari mata yang terdeteksi
                radius = int(round((w2 + h2) * 0.25))

                # Tampilkan lingkaran
                frame = cv2.circle(frame, eye_center, radius, (0, 255, 0), 2)

        # Tampilkan frame
        cv2.imshow('Frame', frame)

        # Kondisi untuk end while loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    frame.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # Get data kamera
    camera = cv2.VideoCapture(0)
    main(camera)