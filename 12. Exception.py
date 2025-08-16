# 예외처리
# 오류가 발생해도, 프로그램이 정상적으로 작동하게할수있는 방법

# 예외 (exception)
# 프로그램을 실행할때 발생하는 오류상황

# try-except 구문
'''
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        return f"예외가 발생했습니다: {e}"

print(divide("10", "0"))
'''

# try-except 구문은 오류가 생길때, 특정 오류를 지정해서 예외처리를 할수있다.
# 예) ZeroDivisionError

# 모든 예외 처리하기 Exception: Exception은 모든 오류를 예외처리할수있다.
# 무슨 오류인지 알려주기위해서는 Exception as e를 쓴다.
# 오류의 원인을 파악하기 어려움으로, 신중하게 사용해야한다.

# else와 finally 구문
# else: 예외가 발생하지 않았을때 실행되는 코드 블록이다.
# finally: 예외 발생 여부와 상관없이 항상 실행되는 코드 블록이다. 주로 자원을 정리할때 사용된다.

def division(a,b):
    try:
        abc= a/b
    except ZeroDivisionError:
        return "0으로 나눌수없습니다"
    else:
        return f"결과:{abc}"
    finally:
        print("계산이 완료되었습니다")

print(division(10,2))

# 사용자 정의 예외
# 필요에 따라 사용자가 직접 예외를 정의하여 사용할수있다.
# exception class를 상속받아 사용합니다

class NegativeNumberError(Exception):
    pass 

def square_root(x):
    if x < 0:
        raise NegativeNumberError("음수는 제곱근을 계산할 수 없습니다.")
    return x ** 0.5

try:
    print(square_root(-9))
except NegativeNumberError as e:
    print(e)

