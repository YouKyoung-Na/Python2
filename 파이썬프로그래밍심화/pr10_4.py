#4. 
# 파일 불러오기
poem_read = open('파이썬프로그래밍심화/poem.txt', 'r')

poem_r = poem_read.read()

# 파일 내용 출력
print(poem_r)

# 찾을 내용과 바꿀 내용 입력
find = input('찾을 내용: ')
change = input('바꿀 내용: ')

# 바꾸는 작업 + 몇 번 바꿨는지 출력
print(f'{poem_r.count(find)}을 모두 바꿉니다.')
poem_write = open('파이썬프로그래밍심화/poem.txt', 'w')
poem_w = poem_write.write(poem_r.replace(find, change))

# 바뀐 파일 저장
poem_write.close()