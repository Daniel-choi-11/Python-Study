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

# return은 저장하는 역할
def without_return(a,b):
    return a*b
c= without_return(2,4)
print(c)

# return이 없으면 출력값은 none, 있으면 일반 값
