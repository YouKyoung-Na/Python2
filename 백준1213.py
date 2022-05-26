from collections import Counter

data = list(input())
data.sort()  #사전 순 정렬
data_cnt = Counter(data)

odd_cnt = 0  #홀수 개수
odd_char = ""  #홀수 가운데 문자
left = ""

for i in data_cnt:
    if data_cnt[i]%2 != 0:
        odd_cnt +=1
        odd_char += i
        data.remove(i)
        
    if odd_cnt > 1:
        break

if odd_cnt > 1 :
    print("I'm Sorry Hansoo")
else:
    
    for i in range(0, len(data),2):
        left += data[i]

    print(left + odd_char+left[::-1])  