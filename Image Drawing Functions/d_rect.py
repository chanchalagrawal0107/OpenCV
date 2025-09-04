import cv2
image = cv2.imread("myphoto2.jpg")

if image is None:
    print("image is not working")

else:
    print("Image loaded successfully")

    pt1 = (50, 100)
    pt2 = (300, 500)
    color = (0, 255, 0)
    thickness = 2

    cv2.rectangle(image, pt1, pt2, color, thickness)

    cv2.imshow("Rectangular image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()