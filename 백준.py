a=[]

for i in range(9):
    a.append(int(input()))
total = sum(a)

for i in range(0, 8):
    for j in range(i+1, 9):
        if (total - (a[i]+a[j]))==100:
            a.remove(a[i])
            a.remove(a[j])
            break
            
    
a.sort()

for i in a:
    print(i)