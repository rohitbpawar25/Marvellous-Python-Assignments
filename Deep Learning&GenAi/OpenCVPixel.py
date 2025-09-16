# ----------------------------------------------------------
# Load an image, convert to grayscale, and display pixel intensities
#
# - Reads a color image using OpenCV
# - Converts it to grayscale
# - Plots the grayscale image and a colorbar of pixel values side-by-side using matplotlib
# ----------------------------------------------------------

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("sample.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10,5))
plt.subplot(1,2,1); plt.imshow(gray, cmap="gray"); plt.title("Grayscale Image"); plt.axis("off")
plt.subplot(1,2,2); plt.imshow(gray, cmap="gray"); plt.colorbar(label="Pixel Value"); plt.title("Pixel Values")
plt.show()
