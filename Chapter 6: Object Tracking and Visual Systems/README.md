# **🚸 어린이 보호구역 인식 시스템 🚸**

### 📋 PyQt5를 활용하여 shift 매칭(특징점 매칭)을 이용, 실제 영상 1, 2, 3에서 표지판 위치를 표현하고 소스/결과 화면을 캡처하였습니다.

- SIFT 특징점 추출 및 FLANN 매칭

- RANSAC Homography로 표지판 실제 위치 계산

- 실시간 영상에서 3종 표지판 자동 인식

- 매칭 결과 시각화 및 위치 표시

사용순서 : 표지판 등록 → 도로 영상 불러오기 → 인식 시작

🎯 주요 기능
  - ✅ 표지판 등록: 어린이 보호구역, 속도30제한, 어린이보호 3종 이미지 등록

 - ✅ 도로 영상 재생: MP4 등 영상 파일 로드 및 프레임별 재생

 - ✅ 실시간 인식: 10프레임마다 SIFT 매칭 수행

 - ✅ 위치 표시: 인식된 표지판 위치를 초록색 사각형으로 표시

 - ✅ 매칭 결과: 특징점 연결선과 매칭 이미지 출력

📸 결과 화면: 

<img width="1008" height="604" alt="image" src="https://github.com/user-attachments/assets/6120fadd-1fde-4ee0-9d02-acaddf5be544" />
- 시작 화면

  
<img width="1008" height="606" alt="image" src="https://github.com/user-attachments/assets/7b150566-13dc-4831-89f1-b43c8c68eadf" />
- 영상 1 결과 - 어린이 보호구역

  
<img width="1008" height="605" alt="image" src="https://github.com/user-attachments/assets/58a020c2-6f26-4a3e-ae27-0f09ff4681dd" />
- 영상 2 결과 - 속도 30 제한

<img width="1006" height="602" alt="image" src="https://github.com/user-attachments/assets/0533e21b-7231-4145-b597-93ef41fa3c45" />
- 영상 3 결과 - 횡단보도



🎓 Perplexity AI를 활용하여 구현
