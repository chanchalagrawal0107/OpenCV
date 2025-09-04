import cv2
image = cv2.imread("myphoto2.jpg")

if image is None:
    print("image is not working")

else:
    print("Image loaded successfully")

    #image, centre, radius, colour, thickness(-1 matlab poora color se fill ho jaega circle, aur agar kuch na likho toh wo bas ek outline dedega)
    cv2.circle(image, (150, 150), 50, (255, 0, 0), -1)

    cv2.imshow("Circled image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()