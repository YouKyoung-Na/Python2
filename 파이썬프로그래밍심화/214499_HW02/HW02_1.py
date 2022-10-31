#hw1
### 입력
num = int(input("환전하려는 금액(원): "))
country = input("국가 선택(미국/영국/독일/중국/일본): ")


###if-else문에 사용할 변수 선언
if country=="미국":  #country 변수에 미국이 입력되었을때
    rate = 1394.00  #환율비율
    print(f'{num/rate:.2f} 달러')  #계산 및 출력, f-string 사용

elif country == "영국":  #country 변수에 영국이 입력되었을때
    rate = 1586.44
    print(f'{num/rate:.2f} 파운드')  #계산 및 출력

elif country == "독일":  #country 변수에 독일이 입력되었을때
    rate = 1393.33
    print(f'{num/rate:.2f} 유로')  #계산 및 출력

elif country == "중국":  #country 변수에 중국이 입력되었을때
    rate = 198.65
    print(f'{num/rate:.2f} 위안')  #계산 및 출력

elif country == "일본":  #country 변수에 일본이 입력되었을때
    rate = 971.87
    print(f'{num/rate:.2f} 엔')  #계산 및 출력


else:
    print("국가를 잘못 입력했습니다.")  #계산 및 출력
    print("0.00")