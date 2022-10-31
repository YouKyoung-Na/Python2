# hw7. 과제 2. 
## 입력, 두 양의 정수
n1 = int(input('첫 번째 양의 정수 : '))
n2 = int(input('두 번째 양의 정수: '))

# a>=b 조건
if(n1>n2):
    a = n1
    b = n2
elif(n1<n2):
    a = n2
    b = n1

# 최대공약수 loop
while(True):
    if(a==b):  #만일 a==b이면 a를 출력하고 종료
        print("최대공약수:", a)
        print("종료합니다.")
        break
    elif(a>b):  #a가 크면
        a -= b  #a = a-b
        continue  #다시 돌아감
    elif(b>a):  #b가 크면
        b-=a  #b = b-a
        continue  #다시 돌아감