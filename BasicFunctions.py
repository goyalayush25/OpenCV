import cv2
import numpy as np

kernel = np.ones((5, 5), np.uint8)
print(kernel)
path = "Reso/ScanTest.jpeg"
img = cv2.imread(path)
# To convert image to gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Add blur to image - if we increase k-size more blur image will be
imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 0)
# For Edge Detection - if we decrease threshold limit lot more edges visible
imgCanny = cv2.Canny(imgGray, 100, 200)
# Dilation - Thickness of Canny Image Lines increases in respective directions - on increasing iterations thickness further increases
imgDilate = cv2.dilate(imgCanny, kernel, iterations=1)
# Eroded
imgEroded = cv2.erode(imgCanny, kernel)
cv2.imshow('Original', img)
cv2.imshow('Photo', imgGray)
cv2.imshow('Blur', imgBlur)
cv2.imshow('Image Canny', imgCanny)
cv2.imshow('Dilate', imgDilate)
cv2.imshow('Eroded', imgEroded)
cv2.waitKey(0)