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
# - 람다(lambda)는 '임시 알바생' 함수라고 생각하면 아주 편합니다.
#
# - '정직원' 함수 (def로 만든 함수)
#   - 이름도 있고(def add_def), 시키면 언제든 그 일을 할 수 있습니다.
#   - 하지만 아주 잠깐 쓰고 말 간단한 일(예: 1회성 이벤트)을 시키려고
#   - 정식으로 'def'를 써서 함수를 만드는 건 좀 귀찮고 번거롭죠.
#
# - '임시 알바생' 함수 (lambda)
#   - 이름이 없습니다. (익명 함수)
#   - 딱 한 줄짜리 간단한 일을 시킬 때, 그 자리에서 바로 만들어 쓰는 '일회용' 함수입니다.
#   - "이거 잠깐 계산만 하고 가!" 같은 느낌이죠.
#
# - 문법:
#   lambda 매개변수: 매개변수로 할 일 (이게 바로 반환값)

# (1) 람다 함수를 굳이 변수에 담아 본다면?
#     (비유: 임시 알바생에게 굳이 '김씨'라고 이름을 불러주는 격)
add_lambda = lambda x, y: x + y
print(f"\n람다 함수 add_lambda(3, 900) 결과: {add_lambda(3, 900)}")

#     이건 아래 '정직원' 함수와 100% 똑같은 일입니다.
def add_def(x, y):
    return x + y


# 8. lambda의 진짜 쓰임새 (언제 쓰면 좋은가?)
# -----------------------------------------------
# - 람다는 다른 함수(예: sorted, map)의 '부품'으로 끼워 넣을 때
#   가장 빛을 발합니다.
#
# - 예를 들어, 'sorted' 함수는 정렬 기준(key)을 알려줘야 합니다.
#   sorted(정렬할_리스트, key=정렬규칙_함수)
#
#   이 '정렬규칙_함수' 자리에 '임시 알바생(lambda)'을 쓸 수 있습니다.


words = ["apple", "banana", "pie", "apply", "peach"]

# - 문제: words 리스트를 (1)길이순, (2)사전순 으로 정렬하고 싶다.

# (방법 1: '정직원' 함수(def)를 쓰는 방법 - 람다 X)
# 1. 정렬 규칙을 정해주는 함수를 '정식으로' 만듭니다.
def sort_key_func(word):
    # 정렬 기준이 될 '꼬리표(튜플)'를 만들어 반환
    return (len(word), word)

# 2. 'sorted'의 key 자리에 '정직원' 함수의 이름을 알려줍니다.
sorted_list_1 = sorted(words, key=sort_key_func)
print(f"\ndef 함수 사용 정렬: {sorted_list_1}")


# (방법 2: '임시 알바생' 함수(lambda)를 쓰는 방법 - 추천!)
# 1. 'key=' 자리에 람다 함수를 '즉석에서' 만들어 끼워 넣습니다.
#    (def로 함수를 따로 만들 필요가 없어 코드가 깔끔해집니다)
sorted_list_2 = sorted(words, key=lambda w: (len(w), w))
print(f"람다 함수 사용 정렬: {sorted_list_2}")

# - 람다 코드 해설:
#   key=lambda w: (len(w), w)
#
#   이 코드는 'sorted' 함수에게 이렇게 말하는 것과 같습니다:
#   "내가 지금 'w'라는 이름으로 단어를 하나씩 줄게."
#   "너는 그 'w'를 받아서 (단어 길이, 단어 자체) 순서로 꼬리표(튜플)를 만들어."
#   "그리고 그 꼬리표 순서대로 정렬해 줘."
#
#   - 'apple'이 오면 -> (5, 'apple') 꼬리표 생성
#   - 'pie'가 오면   -> (3, 'pie') 꼬리표 생성
#
#   'sorted'는 (3, 'pie')가 (5, 'apple')보다 앞에 온다는 것을
#   이 꼬리표를 보고 알게 됩니다.
