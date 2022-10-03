# 6번
ID = input('아이디 생성 ==> ')
pw = int(input('비밀번호 입력 ==> '))
print(f'아이디가 생성되었습니다. [{ID}]')

print()
print('******로그인******')
check_id = input('[ID] ')
check_pw = int(input('[PW] '))

if check_id == ID:
    if check_pw == pw:
        print('로그인 여부: True')
    else:
        print('로그인 여부: False')
else:
    print('로그인 여부: False')