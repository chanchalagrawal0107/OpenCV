import cv2
image = cv2.imread("myphoto2.jpg")

if image is None:
    print("Image not found")

else:
    print("Image loaded")
    cropped = image[100:200, 50:150]
    cv2.imshow("cropped", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()