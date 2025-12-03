import cv2
import numpy as np

image = cv2.imread('my_image.jpg')

print(f"Shape: {image.shape}")
print(f"Data type: {image.dtype}")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, binary_mask = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)
print(f"Grayscale shape: {gray_image.shape}")
# Crop an image [y_start:y_end, x_start:x_end]
cropped_image = gray_image

edges = cv2.Canny(image, 100, 200)
cropped_image = edges[100:300, 200:400]
cv2.imshow('Cropped', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imread('new_image.png', image)



