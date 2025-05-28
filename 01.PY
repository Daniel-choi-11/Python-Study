# 변수란?
# 값을 저장하는 공간, 이름을 붙여 사용함

name = "최정"   # 이름이라는 값을 저장
age = 13        # 나이라는 값을 저장

# 정수형(int)
# 소수점이 없는 숫자, 양수/음수/0 모두 가능
c = 1
n = -5
score = 100

# 실수형(float)
# 소수점이 있는 숫자, 정밀한 계산에 사용
d = 1.23
e = -3.24
f = 3.45

# 문자열(str)
# 문자 또는 글자를 저장, 큰따옴표(")나 작은따옴표('') 사용
x = "한글"
y = "87"
z = "Hello, World!"

# 불리언(bool)
# 참(True)과 거짓(False) 둘 중 하나의 값을 가짐
is_adult = True
is_student = False

# 형 변환 (Casting)
# 데이터 타입을 바꾸는 방법(int, float, str 등)
num = "20"
result = 10 + int(num)   # num을 정수로 변환 후 덧셈 (10 + 20 = 30)

# 기본 연산자
a = 15
b = 4

add = a + b    # 덧셈:           19
sub = a - b    # 뺄셈:           11
mul = a * b    # 곱셈:           60
div = a / b    # 나눗셈(실수):    3.75
flo = a // b   # 몫(정수):        3
mod = a % b    # 나머지:          3
exp = a ** b   # 제곱:            50625 (15의 4제곱)

# 비교 연산자
same = (a == b)     # == : a와 b가 같은가         (False)
diff = (a != b)     # != : a와 b가 다른가         (True)
bigger = (a > b)    # >  : a가 b보다 큰가         (True)
smaller = (a < b)   # <  : a가 b보다 작은가       (False)
big_eq = (a >= b)   # >= : a가 b보다 크거나 같은가 (True)
small_eq = (a <= b) # <= : a가 b보다 작거나 같은가 (False)

# 논리 연산자
cond1 = (a > 10) and (b < 10)   # 둘 다 True여야 결과가 True (True)
cond2 = (a > 20) or (b < 10)    # 둘 중 하나만 True여도 True (True)
cond3 = not(a == b)             # 결과를 반대로 (True)

# 연산자 우선순위
result1 = 2 + 3 * 4     # 3*4 먼저 계산 → 2+12 = 14
result2 = (2 + 3) * 4   # 괄호가 우선 → 5*4 = 20
result3 = 2 ** 3 * 2    # **가 *보다 먼저 → 8*2 = 16

# 들여쓰기(Indentation)
age = 13
if age >= 18:
    print("성인입니다.")
else:
    print("청소년입니다.")
