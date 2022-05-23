n=int(input())
OrgList = list(map(int, input().split()))
m=max(OrgList)

NewList=[]
for score in OrgList:
    NewList.append(score/m*100)
result= sum(NewList)/n
print(result)