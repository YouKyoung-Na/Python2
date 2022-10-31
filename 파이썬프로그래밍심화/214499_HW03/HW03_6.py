#6. 버킷리스트 작성
### 입력
ls = []

### 출력
while(True):  #무한루프
    n = int(input('버킷리스트 기능 선택(1.추가 2.삭제 0.종료): '))
    if(n == 1):  #입력값이 1이면 append 이용해서 추가
        a = input('추가할 내용: ')
        ls.append(a)  
        print('**************************')
        for i in ls:  #리스트 출력
            print(i)
        print('**************************')
        continue

    elif(n==2):  #입력값이 2이면 remove 이용해서 삭제
        b = input('삭제할 내용: ')
        ls.remove(b)
        print('**************************')
        for i in ls:  #리스트 출력
            print(i)
        print('**************************')
        continue

    elif(n==0):  #입력값이 0이면 종료
        print('프로그램을 종료합니다.') 
        break;
    else:  #입력값이 0,1,2가 아니면 아래와 같이 출력
        print('기능 선택 오류. 다시 선택하세요')

