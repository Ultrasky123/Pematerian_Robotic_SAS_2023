import cv2

def main(capture):
    while True:
        # print(capture.read())
        # Baca kamera
        ret, frame = capture.read()

        face = "/home/tisyads/SAS23/pertemuan3/asset/haarcascade_frontalcatface.xml"
        faceCascade = cv2.CascadeClassifier(faceCascade)

        smile = "/home/tisyads/SAS23/pertemuan3/asset/haarcascade_smile.xml"
        smileCascade = cv2.CascadeClassifier(smileCascade)

        eye = "/home/tisyads/SAS23/pertemuan3/asset/haarcascade_eye.xml"
        eyeCascade = cv2.CascadeClassifier(eyeCascade)

        faces = faceCascade.detectMultiScale(gray)
        scaleFactor= 1.1,
        minNeighbors=8,
        minSize=(55, 55)
    
        for (x,y,w,h) in faces:
            center = ((x + w//2, y + h//2))
            frame = cv2.ellipse(frame, center, (w//2 , h//2), 0,0,360, (255,0,0),2)

            face_roi = gray[y:y+h, x:x+w]
            eyes = eyes_cascade.detectionMultiscale(face_roi)
            
            for(x2,y2,w2,h2)in eyes:
                eye_center = (x + x2 + w2//2, y + y2 + h2//2)
                radius = int(round(w2+h2)*0.25)
                frame = cv2.circle(frame, eye_center, radius, (0,255,0),2)

        smile = smileCascade.detectMultiscale(gray,  scaleFactor= 1.16,
        minNeighbors=35,
        minSize=(25, 25))


        for(x2,y2,w2,h2)in smile:
            eye_center = (x + x2 + w2//2, y + y2 + h2//2)
            radius = int(round(w2+h2)*0.25)
            frame = cv2.circle(frame, eye_center, radius, (0,255,0),2)
            

        cv2.imshow('frame', frame)
        if cv2.waitkey(1) & 0xff == ord('q'):
            break

        frame.release()
        cv2.destroyAllWindows()

        if __name__ == '__main__':
            # Get data kamera
            camera = cv2.VideoCapture(0)
            main(camera)
            if vc.isOpened(): # try to get the first frame
                rval, frame = vc.read()
        else:
            rval = False

        print()

        while rval:
            cv2.imshow("preview", frame)
            rval, frame = vc.read()
            key = cv2.waitKey(40)

