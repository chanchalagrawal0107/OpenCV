import cv2
image = cv2.imread("blueprint-X_myphoto.jpg")
if image is None:
    print("Error finding image")
else:
    print("Image loaded successfully")

cv2.imshow("Chanchal", image)
cv2.waitKey(0)
cv2.destroyAllWindows()