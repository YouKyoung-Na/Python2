# 6번
### 아이디 생성 및 비밀번호 입력
ID = input('아이디 생성 ==> ')
pw = int(input('비밀번호 입력 ==> '))
print(f'아이디가 생성되었습니다. [{ID}]')  # 생성 알림 출력

print()  #공백

###로그인(일치여부 출력)
print('******로그인******')
check_id = input('[ID] ')
check_pw = int(input('[PW] '))

###로그인 일치 여부 코드
if check_id == ID:  #아이디 일치 여부
    if check_pw == pw:  #패스워드 일치 여부
        print('로그인 여부: True')
    else:
        print('로그인 여부: False')  #패스워드에서 틀릴 시
else:  #아이디에서 틀릴시
    print('로그인 여부: False')