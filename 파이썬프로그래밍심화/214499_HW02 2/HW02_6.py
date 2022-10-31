# HW 6. 과제 1. 
### 변수 선언
popcorn = 5000; fried = 3000; nacho = 4000; hotdog = 3500; coke = 2500
price = 0

### 메뉴 출력
print("***************************")
print("[1]팝콘 [2]감자튀김 [3]나쵸 [4]핫도그 [5]콜라")
print("주문을 끝내려면 [0]을 입력하세요.")
print("---------------------------")

### While문 내부에 if문을 넣어 처리하기(다양한 케이스)
while(True):
    menu = int(input('선택 메뉴: '))  #메뉴를 먼저 받음
    if(menu<0 or menu>5):  #메뉴가 범위를 벗어났을 때
        print("[주의!] 존재하지 않는 메뉴입니다. 다시 선택하세요.")
        print("")
        continue
    if(menu == 0):
        break

    elif(menu==1):  #메뉴가 팝콘일 때
        num = int(input('주문 수량: '))  #수량은 나중에 받음
        print("")
        price += popcorn *num
        continue

    elif(menu==2):  #메뉴카 감자튀김일 때 
        num = int(input('주문 수량: '))
        print("")
        price += fried *num
        continue

    elif(menu==3):  #메뉴가 나쵸일 때 
        num = int(input('주문 수량: '))
        print("")
        price += nacho *num
        continue

    elif(menu==4):  #메뉴가 핫도그일 때
        num = int(input('주문 수량: '))
        print("")
        price += hotdog *num
        continue

    elif(menu==5):  #메뉴가 콜라일 때
        num = int(input('주문 수량: '))
        print("")
        price += coke *num
        continue
    
print("---------------------------")
### 결과 출력
print(f'금액 합계는 {price} 원 입니다.')