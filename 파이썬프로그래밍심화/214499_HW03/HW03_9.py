#9.  (과제 4번) 행성까지의 시간
###입력
#주어진 딕셔너리 
dic = {'수성': 91_700_000, '금성': 41_400_000, '화성':78_400_000, 
'목성':628_700_000, '토성': 1_277_400_000, '천왕성':2_750_400_000, '해왕성':4_347_400_000  }

#행성 이름 및 이동속도 입력받기
name = input('행성이름: ')
speed = int(input('이동속도(km/h): '))
key = dic[name]  #행성간의 거리는 key값으로 받아옴

time = key / speed  #행성간의 이동시간 계산 방법
print(f'이동 시간: 약 {time:2f}시간')

#년, 월, 일, 시간 계산 방법
year = int(time //8760)  #년
time -= (year*8760)
mon = int(time // 720)  #월
time -= (mon*720)
days = int(time //24)  #일
hour = int(time-(days *24))  #시간
print(f'시간 변환: 약{year}년 {mon}월 {days}일 {hour}시간')