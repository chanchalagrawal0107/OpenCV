import cv2
image = cv2.imread("myphoto2.jpg")
blurred = cv2.GaussianBlur(image, (7, 7), 3)

cv2.imshow("Original image", image)
cv2.imshow("Blurred image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

#blending- saari values ko ek sath karke uska avg nikalna aur fir uss avg value ko apni wali value ke sath replace karna taki image smooth bane, noise hate

# ek khud ka colour liya, baki apne saare neighbours ke liye, sabhi ka avg nikalke apne wale number se replace kar dena is BLENDING. isse sudden spikes remove ho jate hai, image smooth ho jati hai, jo bhi noise aur harsh spots wagera hote hai wo sab remove ho jate hai. image ek less sharp aur smooth nikalke aati hai.