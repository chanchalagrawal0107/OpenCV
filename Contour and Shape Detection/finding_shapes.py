#approx = cv2.approxPolyDP(contour, epsilon, True)   

import cv2

# Read the image
img = cv2.imread(r"C:\Users\agraw\.vscode\OpenCV\myphoto2.jpg")

# Safety check
if img is None:
    print("Error: Image not found or path is incorrect")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold (binary image)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY)

# Find contours on the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on a copy of original image
output = img.copy()
cv2.drawContours(output, contours, -1, (0, 255, 0), 2)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)

    corners = len(approx)

    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagon"
    elif corners > 5:
        shape_name = "Circle"
    else:
        shape_name = "unknown"

    cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
    x = approx.ravel()[0]               #ravel function multidimensional array ko 1D array mein convert karega
    y = approx.ravel()[1] - 10
    cv2.putText(img, shape_name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 0), 2)

# Show results
cv2.imshow("Threshold", thresh)
cv2.imshow("Contours", output)

cv2.waitKey(0)      # Wait for a key press
cv2.destroyAllWindows()
