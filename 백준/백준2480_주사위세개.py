nums = list(map(int,input().split()))
nums.sort()
new_list=set(nums)

if(len(new_list)==1):
    print(10000+(nums[0]*1000))

elif(len(new_list)==2):
    for i in new_list:
        if(nums.count(i)==2):
            print(1000+(i*100))
else:
    print(nums[2]*100)

#정석..쉬운문제도 어렵게 푸는 나란..
# a,b,c=map(int,input().split())
# if a==b==c:
#     print(10000+a*1000)
# elif a==b or b==c:
#     print(1000+b*100)
# elif a==c:
#     print(1000+a*100)
# else:
#     print(max(a,b,c)*100)