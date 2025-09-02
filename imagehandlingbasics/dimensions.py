import cv2
image = cv2.imread("blueprint-X_myphoto.jpg")

if image is not None:
    h, w, c = image.shape
    print(f"Image loaded:\nHeight: {h}\nWidth: {w}\nChannels: {c}")
else:
    print("Couldn't load")