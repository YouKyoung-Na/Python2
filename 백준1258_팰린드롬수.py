from collections import Counter

n= int(input())
data = [int(a) for a in str(n)]
data_r = data.reverse()
data_cnt = Counter(data)


for i in data_cnt:
    if data_cnt[i]%2 != 0:  #홀수
        data.remove([len(data)/2])
        data_r.remove([len(data)/2])
        if(data[i]==data_r[i]):
            print('yes')
        else:
            print('no')

    else:
        if(data[i]==data_r[i]):
            print('yes')
        else:
            print('no')