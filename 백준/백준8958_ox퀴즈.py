n=int(input())
for i in range(n):
    oxList = list(input())
    score = 0
    sum = 0
    for ox in oxList:
        if ox == 'O':
            score += 1
            sum += score
        else:
            score = 0
    print(sum)