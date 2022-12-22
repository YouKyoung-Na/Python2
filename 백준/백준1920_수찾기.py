n = int(input())
n_list = []

result =[]

for i in range(n):
    ns = int(input().split())
    n_list.append(ns)

m = int(input())
m_list = []

for i in range(m):
    ms = int(input())
    m_list.append(ms)

for i in m_list:
    for j in n_list:
        if i == n_list[j]:
            result.append(1)
        else:
            result.append(0)

for i in result:
    print(i)