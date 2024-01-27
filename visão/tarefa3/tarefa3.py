
# Python program to explain cv2.imshow() method 
  
# importing cv2 
import cv2
import numpy as np
  
# path 
path = 'img.jpg'
  
# Reading an image in default mode 
image = cv2.imread(path) 
  
lower_red = np.array([0, 0, 200], dtype = "uint8")
upper_red= np.array([0, 0, 255], dtype = "uint8")

mask = cv2.inRange(image, lower_red, upper_red)

detected_output = cv2.bitwise_and(image, image, mask = mask)
cv2.imshow("red color detection", detected_output)
cv2.waitKey(0)