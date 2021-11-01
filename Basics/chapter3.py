import cv2

img = cv2.imread("Resources/Lenna.png")
print(img.shape)

imgResized = cv2.resize(img, (200, 300))
print(imgResized.shape)

imgCropped = img[0:200, 200:500]

cv2.imshow("Image", img)
cv2.imshow("Resized Image", imgResized)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
