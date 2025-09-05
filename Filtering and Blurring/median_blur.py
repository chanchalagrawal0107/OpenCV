# Median Blur - sabse pehele group of pixels ko dhundega, uske baad unko brightness ke according sort kar dega aur fir jo unki middle/median value niklegi usko nikal dega
# how is it different from gaussian_blur? - gaussian blur nikalta hai neighbours ka avg nikalke, median mein middle value of neighbours ka mid nikalke nikalte hai(Random black and white dots ko remove karne ke liye use hota hai)

#blurred = cv2.medianBlur(image, kernel_size)

import cv2
image = cv2.imread(r"C:\Users\agraw\.vscode\OpenCV\blueprint-X_myphoto.jpg")

blurred = cv2.medianBlur(image, 11)
cv2.imshow("Original", image)
cv2.imshow("clean image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()