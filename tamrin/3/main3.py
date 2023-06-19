import cv2
import matplotlib.pyplot as plt
from boundingRect import kiya_boundingRect

image = cv2.imread("input\dice.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, image_thresh = cv2.threshold(image,75,255,cv2.THRESH_BINARY)

r, c = image_thresh.shape
w = 0
b = 0
for i in range(r):
    for j in range(c):
        if 250 < image_thresh[i,j] > 255:
            w += 1
        else:
            b += 1

if b > w:
    image_thresh = 255 - image_thresh

contours, _ = cv2.findContours(image_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

number = 0
for contour in contours:
    if cv2.contourArea(contour) < 90:
        continue
    x,y,w,h = kiya_boundingRect(contour)
    cv2.rectangle(image,(x,y),(x+w, y+w), (127,127,127), 2)
    number += 1 

print(number)
plt.imshow(image, cmap='gray')
plt.show()
cv2.imwrite("output/2_result.png", image)