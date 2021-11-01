import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('test.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

hImg, wImg, _ = img.shape

# 숫자를 검출하기 위해 digits 설정
cong = r'--oem 3 --psm 6 outputbase digits'

# config 설정
boxes = pytesseract.image_to_boxes(img, config=cong)
for b in boxes.splitlines():
    b = b.split(' ')
    print(b)

    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255), 1)
    cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)

cv2.imshow('Result', img)
cv2.waitKey(0)
