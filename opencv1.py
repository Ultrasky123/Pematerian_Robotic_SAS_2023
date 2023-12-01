import cv2

def main(capture):
    while True:
        # print(capture.read())
        # Baca kamera
        ret, frame = capture.read()

        frame = cv2.flip(frame, 1)
        frame = cv2.resize(frame, (0,0), fx=1.5, fy=1.5)

        # Tampilkan frame
        cv2.imshow('Frame', frame)

        # Kondisi untuk end while loop
        if cv2.waitKey(1) == ord('q'):
            break

    frame.release()
    cv2.destroyAllWindows

if __name__ == '__main__':
    camera = cv2.VideoCapture(0)
    main(camera)

