#1부터 50까지 수 중에 3의 배수이면서 동시에 5의 배수인 수를 출력하기
for i in range(1,51):
    if i % 3==0 and i % 5==0:
        print(i)

# 비밀번호 맞출 때까지 반복 입력받기
correct_pw = 1234
pw = int(input("비밀번호를 입력하세요:"))
while pw != correct_pw:
    print("틀렸습니다.") 
    pw =int(input("다시 입력해주세요:"))
print("축하합니다!")
