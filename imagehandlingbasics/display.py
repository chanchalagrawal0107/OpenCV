import cv2
image = cv2.imread("blueprint-X_myphoto.jpg")
if image is not None:
    cv2.imshow("Image showing", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("cannot load")