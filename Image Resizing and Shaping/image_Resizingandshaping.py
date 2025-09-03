import cv2
image = cv2.imread("myphoto2.jpg")

if image is None:
    print("Image not found")

else:
    print("Image loaded")

    #width x height hota hai yaha
    resized = cv2.resize(image, (500, 500))

    cv2.imshow("Original image", image)
    cv2.imshow("Resized image", resized)


    #hamesha save karni hoti hai nhi toh wo overlap kar jati hai
    cv2.imwrite("Resized_output.jpg", resized)

    cv2.waitKey(0)
    cv2.destroyAllWindows()