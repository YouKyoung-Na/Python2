# 1. 
### 모듈 임포트

### 튜플
names = ('choi', 'han', 'jung', 'kang', 'kim', 'lee', 'moon', 'na', 'park', 'son')
nums = (93, 50, 92, 68, 80, 90, 65, 100, 75, 75)

### 처리
a = max(nums)
b = (nums.index(a))

### 출력
print(f'시험 점수가 가장 높은 학생은 {names[b]}, 점수는 {a} 입니다.')