while(True):
    n= input()
    if n == '0': break

    elif n == n[::-1]: #짝수
        print('yes')
    else:
        print('no')