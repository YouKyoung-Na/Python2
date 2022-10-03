#2
###입력
height = int(input("키 입력(cm): "))
weight = int(input("몸무게 입력(kg): "))

### BMI 계산 및 출력
bmi = (weight / ((height/100)*(height/100)))


### if-else를 이용해 건강상태 출력
if bmi >=25:
    result = "비만"
elif bmi >= 23:
    result = "과체중"
elif bmi >= 18.5:
    result = "정상"

else:
    result = "저체중"

print(f'당신의 BMI는 {bmi:.2f} 입니다. {result} 입니다.')