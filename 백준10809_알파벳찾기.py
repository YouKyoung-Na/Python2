from string import ascii_lowercase
word = input()

for i in ascii_lowercase:
    print(word.find(str(i)))
