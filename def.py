# 함수 
# 입력값을 가지고 어떤 일을 수행한 후 그 결과물을 내어 놓는 것이 바로 함수
# 비유: 과일(입력)이 있으면 믹서기(함수)를 사용하기. 함수가 같다는 과정하에, 결과는 입력에 따라 다르다.

# 함수를 사용하는 이유는 무엇일까?
# 반복적인 부분을 대체하기위해 사용한다

def 함수_이름(매개변수):
    수행할_문장1...

#매개변수란 함수의 입력값또는 input이라 생각하면 편하다.

def add(a, b): 
    return a + b
a=3
b=4
c=add(a, b)
print(c)

print(add(10, 4))

=======================

def add_without_return(a, b):
    result = a + b # a 변수와 b 변수에 있는 값을 result 라는 변수에 저장해줘
    print(result) # result 변수에 있는 값을 출력해줘

total = add_without_return(3, 5) # return 값이 없기 때문에 total 이라는 변수에 아무 값도 저장이 안됨
print(total) # None 출력

================================

# 두 수의 합을 반환하는 함수 예제
def add(a, b):
    result = a + b # a 변수와 b 변수에 있는 값을 result 라는 변수에 저장해줘
    print(result) # result 변수에 있는 값을 출력해줘
    return result # result 변수에 있는 값을 반환해줘

total = add(3, 5) # return 값이 있던 덕분에 total 이라는 변수에 결과 값이 저장 됨
print(total) # 8 출력
