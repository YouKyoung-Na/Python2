n = int(input())
words =[]

for word in range(n):
    word = input()
    if word not in words:
        words.append(word)

words.sort()
words.sort(key=len)

for i in words:
    print(i)