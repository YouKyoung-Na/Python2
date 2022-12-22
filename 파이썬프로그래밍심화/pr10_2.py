#2. 
#class 선언
class Student:
    def __init__(self, korean, english, math):
        self.kor = korean
        self.eng = english
        self.math = math

    def sum(self):
        print(self.kor+self.eng+self.math)

    def avg(self):
        print((self.kor+self.eng+self.math)/3)

#출력
student1 = Student(100,100,100)
student1.sum()
student1.avg()