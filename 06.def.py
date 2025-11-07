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

# 7. lambda (람다) 함수
# -----------------------------------------------
# - 정의: '일회용' 임시 함수. (이름이 없는 익명 함수)
# - 용도: def로 정식 함수를 만들긴 귀찮고, '한 줄짜리' 간단한 기능이 필요할 때.
# - 문법: lambda 매개변수1, 매개변수2: 결과표현식

# (1) 람다 함수를 변수에 담아 쓰기 (권장되진 않지만, def와 비교하기 좋음)
add_lambda = lambda x, y: x + y
print(f"\n람다 함수 add_lambda(3, 900) 결과: {add_lambda(3, 900)}")

# 위 람다는 아래 def 함수와 100% 동일
def add_def(x, y):
    return x + y


# 8. lambda의 실제 활용 (sorted와 함께 쓰기)
# -----------------------------------------------
# - 람다는 다른 함수(예: sorted, map, filter)의 'key' 인수로 전달할 때
#   가장 강력하고 유용함.

words = ["apple", "banana", "pie", "apply", "peach"]

# - 문제: words 리스트를 (1)길이순, (2)사전순 으로 정렬하고 싶다.

# (방법 1: def를 사용하는 정석적인 방법)
def sort_key_func(word):
    # 정렬의 기준이 될 '꼬리표(튜플)'를 반환
    return (len(word), word)

sorted_list_1 = sorted(words, key=sort_key_func)
print(f"\ndef 함수 사용 정렬: {sorted_list_1}")

# (방법 2: lambda를 사용하는 깔끔한 방법)
# - key= 자리에 일회용 람다 함수를 바로 정의해서 넣음.
# - 위 sort_key_func와 똑같은 역할을 함.
sorted_list_2 = sorted(words, key=lambda w: (len(w), w))
print(f"람다 함수 사용 정렬: {sorted_list_2}")

# - 람다 작동 원리:
#   1. sorted가 "apple"을 꺼내서 람다에 줌 -> w = "apple"
#   2. 람다가 (len("apple"), "apple") -> (5, "apple") 튜플을 반환
#   3. sorted가 "pie"를 꺼내서 람다에 줌 -> w = "pie"
#   4. 람다가 (len("pie"), "pie") -> (3, "pie") 튜플을 반환
#   5. sorted는 이 튜플들 (꼬리표)을 기준으로 최종 정렬함.
