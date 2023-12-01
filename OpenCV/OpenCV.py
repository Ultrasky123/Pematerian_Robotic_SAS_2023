import cv2

def main(capture):
    while True:
        ret, frame = capture.read()

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    frame.realease()
    cv2.destroyAllwindows()

if __name__=='__main__':
    camera = cv2.VideoCapture(0)
    main(camera)