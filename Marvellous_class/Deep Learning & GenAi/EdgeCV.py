# ----------------------------------------------------------
# Edge Detection using OpenCV Canny Algorithm
#
# - Loads an image in grayscale
# - Applies Canny edge detection with thresholds 100 and 200
# - Displays original and edge-detected images
# ----------------------------------------------------------

import cv2

img = cv2.imread("sample.jpg", 0)  # grayscale
edges = cv2.Canny(img, 100, 200)

cv2.imshow("Original", img)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
