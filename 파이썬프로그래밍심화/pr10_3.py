#3. 
# 파일 불러오기
login_f = open('파이썬프로그래밍심화/login.txt', 'r')
login = login_f.read().split()
print(login)

# 아이디 및 비밀번호 입력
p_id = input('아이디 입력: ')


id_l  = []
pw_l = []

# 입력 데이터 전처리 및 아이디와 비밀번호 동일여부 확인(잘못 입력되었을 경우 확인 요청 문구 출력)
for i in range(len(login)):
    if(i%2==0):
        id_l.append(login[i])
    else:
        pw_l.append(login[i])

if(p_id in id_l):
    index = id_l.index(p_id)
    p_pw = input('비밀번호 입력: ')
    
    if(pw_l[index] == p_pw):
        print(f'접속이 완료되었습니다. 환영합니다. {p_id}')
    else:
        print(f'잘못 입력되었습니다. 비밀번호를 확인하세요.')
else:
    print(f'없는 회원입니다.')
