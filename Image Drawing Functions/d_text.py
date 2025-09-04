import cv2
image = cv2.imread("myphoto2.jpg")

if image is None:
    print("image is not working")

else:
    print("Image loaded successfully")

    cv2.putText(image, "Hello programmers", (50, 300), cv2.FONT_HERSHEY_COMPLEX, 1.2, (0, 255, 255), 2)

    cv2.imshow("Adding text over image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()