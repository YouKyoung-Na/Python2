# 과제 5
members = (('choi', 93), ('han', 50), ('jung', 92), ('kang', 68), ('kim', 80),
 ('lee', 90), ('moon', 65), ('na', 100), ('park', 75), ('song',75))

search = input("학생의 이름(성) 입력: ")
number = -1 # 점수 초기화
start = 0
end = len(members)-1

# Search
print(members[5][1])
# while True:
#   mid = (end - start) // 2
#   if members[mid][0] == search:
#     number = members[mid][1]
#     break
#   elif members[mid][0] > search:
#     end = mid - 1
    
#   else:
#     start = mid + 1 
    

print(f'{search} {number}')