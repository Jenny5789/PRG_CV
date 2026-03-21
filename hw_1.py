'''요구 사항
- 자신이 가장 좋아하는 사진을 읽어오되, 파일이 없을 경우 프로그램이 안전하게 종료되도록 예외 처리를 포함함
- 불러온 영상의 데이터 타입과 배열의 형태(가로, 세로, 채널수)를 출력함
- 원본 컬러 영상을 명암(Gray) 영상으로 변환하고,
- 변환된 영상의 크기를 가로세로 50% 비율로 축소함
- 변환된 영상의 특정 위치에 직사각형을 그리고 그 사진을 찍은 날자를 yyyy.mm.dd.라는 문구를 삽입함
- 최종 결과 영상을 화면에 표시
'''



import cv2 as cv
import sys

# 사진 읽어오기
file_name = 'jenny.jpg'
img = cv.imread(file_name)

# 파일 없을 경우 안전하게 종료되도록 예외 처리 포함
if img is None:
    print(f"오류: '{file_name}' 파일을 찾을 수 없습니다. 안전하게 종료하겠습니다.")
    sys.exit(1)


print("int.type:", img.dtype)
print("image (height, width, channels):", img.shape)

# 원본 컬러 영상을 명암으로 변환
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 변환된 영상의 크기를 가로세로 50% 비율로 축소
gray_small = cv.resize(gray, dsize=(0,0),fx=0.5,fy=0.5)

# 특정 위치에 직사각형을 그리고
cv.rectangle(gray_small,(60,80),(180,130),(255,255,255),2)

# 사진을 찍은 날짜 문구를 삽입
cv.putText(gray_small,'2025.07.26.',(80, 110),cv.FONT_HERSHEY_SIMPLEX,0.4,(255,255,255),1)

# 최종 결과 영상을 화면에 표시
cv.imwrite('jenny_gray.jpg', gray)
cv.imwrite('jenny_small.jpg',gray_small)

cv.imshow('Final_Result_color',img)
cv.imshow('Final_Result_gray', gray_small)

cv.waitKey(0)
cv.destroyAllWindows()
