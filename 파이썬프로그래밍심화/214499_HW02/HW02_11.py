#hw11. 과제 6
### 변수 입력
first_num = input('0~99사이의 정수를 입력하세요: ')  #str형으로 받아옴(배열처리)
final_num = first_num  #final_number은 first number와 동일하게 생각
cnt = 0

### 처리
while(True):
    if len(first_num)  == 1:  #만약 숫자가 한자리면
        final_num = "0" + final_num  #앞에 0을 붙임
    tmp = str(int(final_num[0]) + int(final_num[1]))  #숫자를 합산한다음 다시 str형으로 받는다.
    final_num = final_num[-1] + tmp[-1]  #final_num 계속 업데이트, 이전의 마지막 자리수와 다음 마지막 자리수 합산한다. 
    cnt += 1  #반복할 때마다 1씩 증가

    if(final_num == first_num):  #원래의 수로 돌아왔을 경우
        break  #탈출

### 출력
print(f'숫자 {first_num}의 사이클은? ==> {cnt}')