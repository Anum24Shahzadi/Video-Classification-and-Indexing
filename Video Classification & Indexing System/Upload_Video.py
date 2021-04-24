import cv2

cap = cv2.VideoCapture('Video.mp4')

if(cap.isOpened() == False):
    print("Error Open video file")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow('frame', frame)
        if cv2.waitKey(12500) == ord('q'):
            break

        else:
            break
cap.release()
cv2.destroyAllWindows()
