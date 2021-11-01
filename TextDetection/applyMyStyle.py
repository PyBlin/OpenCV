import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('skin.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# 검출된 문자열을 변수에 저장
myText = pytesseract.image_to_string(img)

# 원하는 파일명과 확장자를 적은 후 'w(쓰기)' 모드
f = open('myStyle.hwp', 'w')

# 열린 파일에 저장했던 검출된 문자열을 쓰기
f.write(myText)

# 이거 반드시 써주기!! 안써주면 보이지 않는 곳에서 계속 열려있음... 아마도?
f.close()
