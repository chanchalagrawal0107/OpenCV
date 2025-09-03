import cv2
image = cv2.imread("myphoto2.jpg")

if image is None:
    print("Image not found")

else:
    flipped_horizontal = cv2.flip(image, 1)
    flipped_vertical = cv2.flip(image, 0)
    flipped_both = cv2.flip(image, -1)
    
    cv2.imshow("Original", image)
    cv2.imshow("flippedhorizontal", flipped_horizontal)
    cv2.imshow("flippedvertical", flipped_vertical)
    cv2.imshow("flippedboth", flipped_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()