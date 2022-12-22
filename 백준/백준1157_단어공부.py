import statistics  #통계 모듈

a = input()
a = a.upper()

if (len(statistics.multimode(a))>=2):
    print('?')
else:
    print(statistics.mode(a))