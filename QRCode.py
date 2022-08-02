import cv2
import numpy as np
from pyzbar.pyzbar import decode
# Helps to find info and location of bar code

img = cv2.imread("Reso/QR.jpg")
code = decode(img)
# print(code)
# print(code[0][2][0])
for barcode in decode(img):
    print(barcode.data)
    myData = barcode.data.decode('utf-8')
    print(myData)
    pts = np.array([barcode.polygon],int)
    pts.reshape((-1,1,2))
    cv2.polylines(img, [pts], True, (255,0,255), 5)  # can be performed using rectangle but polygon provides more accuracy
    pts2 = barcode.rect
    print(pts2[0]," ", pts2[1])
    cv2.putText(img, myData,(pts2[0]-20,pts2[1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)
# x,y,w,h = code[0][2][0], code[0][2][1], code[0][2][2], code[0][2][3]
# cv2.rectangle(img,(x,y), ((x+w),(y+h)), (0,0,255), 4, 1)
# length = len(code[0][3])
cv2.imshow('Image', img)
cv2.waitKey(0)
