# 반복문 
# 반복문은 코드를 여러번 사용하고싶을때 사용된다.

# 1. for문 
# 문자열, 리스트, 튜플, 등과 같은 항목의 순서대로 접근할때 사용됩니다.
food = ["김치", "사과", "배"] 
for food in food:
    print(food)

# 1-1. range() 함수
# for문에서 반복함수를 지정하고싶을때는 range함수를 사용할수있습니다
# i는 가상의 변수다 (허수)
for i in range(5):
    print("안녕하세요")

# 1-1-1. 
    # 기본 사용법: 괄호안에 숫자를 쓰면, 그 숫자만큼 반복한다
    # 시작점과 끝 지정: range(start, stop)을 사용하면, start부터 stop-1까지의 숫자를 생성한다
    # 증가폭 지정: range(start, stop, step)을 사용하면 증가폭을 지정2할수있다
    # 감소폭 지정: range(start, stop, step)을 사용하면 감소폭을 지정할수있다

for i in range(2,10,2):
    print(i)


# 2. while문
# while문은 조건이 참일때, 반복을 계속실행합니다. 조건이 거짓이되면, 반복이 종료됩니다.
count = 0
while count<5:
    print(count)
    count += 1

# 2-1. 무한반복
#while True:
#    print(1,2,3)

# 2-2. break와 continue
#break는 반복문을 즉시 종료
#continue는 현재반복을 건너뛰고 다음 반복을 실행
for i in range(5):
    if i==3:
        break
    print(i)

for i in range(5):
    if i==3:
        continue
    print(i)
