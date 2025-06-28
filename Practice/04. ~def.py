def calculator(a,b,c):
    if c == "add":
        return a + b
    elif c == "sub":
        return a-b
    elif c == "multuply":
        return a * b
    elif c == "divide":
        if b != 0:
            return a/b
        else:
            return "0으로 나눌 수 없습니다"
    else:
        return "지원하지 않는 기능입니다!"

a = int(input())
b = int(input())
c = input()
print(calculator(a,b,c))

