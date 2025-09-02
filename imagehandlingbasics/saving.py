import cv2
image = cv2.imread("blueprint-X_myphoto.jpg")
if image is not None:
    success = cv2.imwrite("output_python.png", image)
    if success:
        print("image saved")
    else:
        print("Failed to save")
else:
    print("cannot load")