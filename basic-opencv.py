import cv2

def main(capture):
    while True:
        # print(capture.read())
        # Baca kamera
        ret, frame = capture.read()

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