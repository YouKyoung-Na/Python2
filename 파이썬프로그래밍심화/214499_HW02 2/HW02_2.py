#hw2
###입력
height = int(input("키 입력(cm): "))
weight = int(input("몸무게 입력(kg): "))

### BMI 계산 및 출력
bmi = (weight / ((height/100)*(height/100)))  #float 형


### if-else를 이용해 건강상태 출력
if bmi >=25:  #bmi 25이상일 시 비만
    result = "비만"
elif bmi >= 23:  #25미만 23 이상일 시 과체중
    result = "과체중"
elif bmi >= 18.5:  #23미만 18.5 이상일 시 정상
    result = "정상"
else:  #18.5 미만일 시 저체중
    result = "저체중"

### 출력
print(f'당신의 BMI는 {bmi:.2f} 입니다. {result} 입니다.')