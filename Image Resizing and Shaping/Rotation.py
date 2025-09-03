import cv2
image = cv2.imread("myphoto2.jpg")

if image is None:
    print("Image not found")

else:
    print("Image loaded")
    (h, w) = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 2.0)            #1.0 matlab same size, 0.5 matlab half the size, and 2.0 means double the image size
    rotated = cv2.warpAffine(image, M, (w, h))
    
    cv2.imshow("Original", image)
    cv2.imshow("Rotated", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()