# 졸업 프로젝트  
```
진행 시기 : 2020.03 - 2020.11
참가 인원 : 김재홍, 김정욱  
지도 교수님 : 김태현 교수님  
```
## Image 손상 정도에 따른 Yolo model 성능 평가
---
### 목표
* 여러 image 손상 기법 사용해 image 손상시키기.
* 다양한 Image 손상 기법에 따른 Yolo model의 성능 분석.
---
### 예시결과
* blur33
<img src="/test/result/blur33/images-101.jpg" width="200" height="200">

* blur33
<img src="/test/result/blur33/images-101.jpg" width="200" height="200">

* blur55
<img src="/test/result/blur33/images-101.jpg" width="200" height="200">

* color trans1
<img src="/test/result/trans1/images-101.jpg" width="200" height="200">

* color trans2
<img src="/test/result/trans2/images-101.jpg" width="200" height="200">

* salt and papper 0.01
<img src="/test/result/0.01/images-101.jpg" width="200" height="200">

* salt and papper 0.005
<img src="/test/result/0.005/images-101.jpg" width="200" height="200">

---
### 결론
* Precision과 Recall으로만 봤을 경우 Salt and Pepper noise를 다루는 새로운 연구가 필요하다고 생각한다.
* 검출 threshold를 높인다면 더 높은 confidence score를 가지는 객체를 인식하므로 precision이 향상될 것이라 생각한다.
* Noise image에 대한 Precision 과 Recall이 감소하지만 Yolo model 굉장히 빠른 모델이기에 다양한 분야에 적용할 수 있을 것이라고 생각한다.
---
### [ppt](https://github.com/graduation-proj/vision_proj/blob/main/Image%20%EC%86%90%EC%83%81%20%EC%A0%95%EB%8F%84%EC%97%90%20%EB%94%B0%EB%A5%B8%20Yolo%20model%20%EC%84%B1%EB%8A%A5%20%ED%8F%89%EA%B0%80.pptx)
---
### 참고
* YOLO v1 | [논문](https://pjreddie.com/media/files/papers/yolo_1.pdf) |
* YOLO v2 | [논문](https://pjreddie.com/media/files/papers/YOLO9000.pdf) |
* YOLO v3 | [논문](https://pjreddie.com/media/files/papers/YOLOv3.pdf) |
* YOLO 사이트 | [주소](https://pjreddie.com/) |
