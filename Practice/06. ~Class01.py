# 계산기
class calculator:
    def __init__(self):
        """계산기 초기화"""
        print("계산기가 준비되었습니다!")
    def addition(self,a,b):
        """더하기"""
        return a+b
    def subtraction(self,a,b):
        """빼기"""
        return a-b
    def multiplication(self,a,b):
        """곱하기"""
        return a*b
    def division(self,a,b):
        """나누기"""
        if b == 0:
            return "0으로 나눌 수 없습니다!"
        return a/b
    

calc = calculator()
print(f"10 + 5 = {calc.addition(10, 5)}")


#자기 소개
class introduction:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def introduce(self):
        print(f"안녕하세요! 저는 {self.name}입니다. 제 나이는 {self.age}이고, 학년은 {self.grade}입니다!")

person1= introduction("최정",14,8)
person1.introduce()

