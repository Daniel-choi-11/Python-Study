# 함수 
# 입력값을 가지고 어떤 일을 수행한 후 그 결과물을 내어 놓는 것이 바로 함수
# 비유: 과일(입력)이 있으면 믹서기(함수)를 사용하기. 함수가 같다는 과정하에, 결과는 입력에 따라 다르다.

# 함수를 사용하는 이유는 무엇일까?
# 반복적인 부분을 대체하기위해 사용한다

def 함수_이름(매개변수):
    수행할_문장1...

#매개변수란 함수의 입력 값 또는 input이라 생각하면 편하다.

def add(a, b): 
    return a + b
a=3
b=4
c=add(a, b)
print(c)

print(add(10, 4))

# return은 저장하는 역할 (값을 반환하는 역할)
def without_return(a,b):
    return a*b
c= without_return(2,4)
print(c)

# return이 없으면 변수에 아무 값도 반환되지 않아서 출력값은 none이 출력된다.

def greeting(name,greet="안녕하세요"):
    print(f"{greet}, {name}님!")
greeting("최정","환영합니다")
# 기본값을 지정하면 함수 호출시 매개변수를 생략할수있습니다

# 가변매개변수
# *args: 숫자를 여러개받으면 튜플로 저장
def a(*args):
    for number in args:
        print(number)
a(3,4,6,7,10,4555)

# **kwargs: 키워드임자를 dictionary로 전달받는다
def io(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
io(name="최정",age=14,gender="male")

# lambda함수: 익명 함수
add=lambda x,y:x+y
print(add(3,900))
