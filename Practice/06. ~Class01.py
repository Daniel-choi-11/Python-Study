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
print(f"10 + 5 = {calc.add(10, 5)}")
