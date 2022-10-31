#5. 
### 딕셔너리 선언
langs  = {'c':1972, 'java':1995, 'python':1991, 'go': 2009, 'pascal':1969}

### 챗봇 프로그램 만들기!(while, if문 등을 활용해보세요!)
while(True):  #while 무한루프
    n = input('프로그래밍 언어 입력(0입력시 종료): ')
    if(n == 'C' or n =='c'):
        print(n, "언어는 ", langs['c'], "년에 태어났어요.")
    elif(n == 'JAVA' or n =='java'):
        print(n, "언어는 ", langs['java'], "년에 태어났어요.")
    elif(n == 'PYTHON' or n =='python'):
        print(n, "언어는 ", langs['python'], "년에 태어났어요.")
    elif(n == 'GO' or n =='go'):
        print(n, "언어는 ", langs['go'], "년에 태어났어요.")
    elif(n == 'PASCAL' or n =='pascal'):
        print(n, "언어는 ", langs['pascal'], "년에 태어났어요.")

    elif(n == '0'):
        print('챗봇 프로그램 종료됩니다.')
        break
    else:
        print("등록되지 않은 언어입니다.")