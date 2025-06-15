# 반복문 
# 반복문은 코드를 여러 번 사용하고 싶을 때 사용됩니다.

# 1. for문 
# 문자열, 리스트, 튜플 등과 같은 항목의 순서대로 접근할 때 사용됩니다.
food = ["김치", "사과", "배"] 
for item in food:
    print(item)
print(f"for문 결과: {food}")
# 출력: 김치
# 출력: 사과  
# 출력: 배

# 1-1. range() 함수
# for문에서 반복 횟수를 지정하고 싶을 때는 range 함수를 사용할 수 있습니다
# i는 가상의 변수입니다 (반복 변수)
for i in range(5):
    print("안녕하세요")
# 출력: 안녕하세요 (5번 반복)

# 1-1-1. range() 함수 사용법
# 기본 사용법: 괄호 안에 숫자를 쓰면, 그 숫자만큼 반복한다
# 시작점과 끝 지정: range(start, stop)을 사용하면, start부터 stop-1까지의 숫자를 생성한다
# 증가폭 지정: range(start, stop, step)을 사용하면 증가폭을 지정할 수 있다
# 감소폭 지정: range(start, stop, step)을 사용하면 감소폭을 지정할 수 있다

for i in range(2, 10, 2):
    print(i)
# 출력: 2, 4, 6, 8

# 2. while문
# while문은 조건이 참일 때, 반복을 계속 실행합니다. 조건이 거짓이 되면, 반복이 종료됩니다.
count = 0
while count < 5:
    print(count)
    count += 1
# 출력: 0, 1, 2, 3, 4

# 2-1. 무한반복
# while True:
#     print(1, 2, 3)
# 출력: 1 2 3 (무한 반복)

# 2-2. break와 continue
# break는 반복문을 즉시 종료
# continue는 현재 반복을 건너뛰고 다음 반복을 실행
print("break 예시:")
for i in range(5):
    if i == 3:
        break
    print(i)
# 출력: 0, 1, 2

print("continue 예시:")
for i in range(5):
    if i == 3:
        continue
    print(i)
# 출력: 0, 1, 2, 4
