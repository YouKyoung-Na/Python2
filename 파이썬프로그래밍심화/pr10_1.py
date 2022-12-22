#1.

#class 선언
class Circle:
    def __init__(self, r):
        self.R = r

    def area(self):
        print(f'원의 넓이는 {self.R*self.R*3.14}')

    def round(self):
        print(f'원의 둘레는 {self.R*2*3.14}')

#출력
c1 = Circle(10)
c1.area()
c1.round()