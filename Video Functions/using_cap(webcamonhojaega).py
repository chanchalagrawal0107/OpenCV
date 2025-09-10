import cv2

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()             #camera mein se ek frame ko read karna hai

    if not ret:
        print("couldn't read frame")
        break

    cv2.imshow("Webcam feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):       #1ms wait karo aur fir check karo ki user ne keyboard mein kuch press toh nhi kara na, agar 'q' press kara hai toh loop se bahar aajao
        print("Quitting..")
        break

cap.release()           #ab jab loop hi break ho jaega toh camera ko bhi band hi karna hoga. release() yahi karta hai
cv2.destroyAllWindows()

