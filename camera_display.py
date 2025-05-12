import cv2

cap = cv2.VideoCapture(0)
rot = 0
mir = 0

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    cv2.putText(frame, "Siti Zahra Muthmainnah", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 3)
    cv2.putText(frame, "Press any alphabet to close the camera", (10, 80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)
    cv2.putText(frame, "Press 1 to rotate 90 degree clockwise", (10, 110), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)
    cv2.putText(frame, "Press 2 to mirror", (10, 140), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 1)
    
    key = cv2.waitKey(1) & 0xFF

    if key == ord('1'):
        rot += 1
    if key == ord('2'):
        mir += 1
    if key >= ord('A') and key <= ord('z'):
        break    

    if rot%4 == 1:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif rot%4 == 2:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
    elif rot%4 == 3:
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    
    if mir%2 == 1:
        frame = cv2.flip(frame, 1)
    
    cv2.imshow('frame', frame)

    
cap.release()
cv2.destroyAllWindows()