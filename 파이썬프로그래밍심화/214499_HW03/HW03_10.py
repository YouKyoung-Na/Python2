#10. 과제 5번
### 입력값 (알파벳순으로 정렬되어있음)
members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80),
    ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song',75))

search = input("학생의 이름(성) 입력: ")
number = -1 # 점수 초기화

start = 0
end = (len(members)-1)  #인덱스 끝값이기 때문에 len에 -1을 해준다.

for n, m in members: ### 이 부분을 이진 탐색에 맞게 수정해주세요.
    mid = (start + end) // 2   #중앙값
    if n == search: # 찾는 값이 있으면 점수를 number에 저장하고 반복 종료
        number = m  
        break
    elif n < search:  #만약 값을 못찾고 search가 오른쪽에 있다면..
        start = mid + 1  #start는 이전의 mid 값에서 한칸 오른쪽으로 
    else:  #search가 왼쪽에 있는 경우 
        end = mid -1  #end가 mid값의 한칸 왼쪽으로

if number > -1:   # 값이 업데이트가 됐다면..
    print(search, number)
else:  #값이 업데이트가 안됐다면...
    print("찾는 학생이 없습니다.")