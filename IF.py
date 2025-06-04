# =============================================================================
# 🔀 Python 조건문 (Conditional Statements)
# =============================================================================

# -----------------------------------------------------------------------------
# 🎯 if문 기본 구조
# if문은 조건이 참일 때 특정 코드 블록을 실행하는 데 사용됩니다.
# 들여쓰기가 매우 중요합니다!
# -----------------------------------------------------------------------------

level = 12

# 기본 if문
if level < 10:
    print("레벨을 더올리고 다시 오십시오")
    print("현재 레벨이 너무 낮습니다")  # 같은 블록 내의 코드

print("이 줄은 조건과 관계없이 항상 실행됩니다")

# 📝 들여쓰기 예시
print("\n=== 들여쓰기의 중요성 ===")
x = 5
if x > 0:
    print("x는 양수입니다")          # 4칸 들여쓰기 (또는 Tab 1개)
    print("양수 처리 로직 실행")      # 같은 레벨 들여쓰기
print("조건문 밖의 코드")            # 들여쓰기 없음

# -----------------------------------------------------------------------------
# 🔄 if-else 문
# else는 if 조건이 거짓일 때 실행됩니다
# -----------------------------------------------------------------------------

level = 12
if level < 10:
    print("레벨을 더올리고 다시 오십시오")
else:
    print("축하합니다! 레벨 10 이상입니다")
    print(f"현재 레벨: {level}")

# 💡 다양한 조건 예시
print("\n=== 다양한 조건 예시 ===")

# 숫자 비교
number = 15
if number % 2 == 0:
    print(f"{number}는 짝수입니다")
else:
    print(f"{number}는 홀수입니다")

# 문자열 비교
password = "1234"
if password == "admin":
    print("관리자 로그인 성공")
else:
    print("일반 사용자 로그인")

# 리스트/문자열 길이 체크
name = "홍길동"
if len(name) >= 3:
    print("이름이 적절한 길이입니다")
else:
    print("이름이 너무 짧습니다")

# -----------------------------------------------------------------------------
# 🎚️ if-elif-else 문
# elif문은 "그렇지 않다면 다른 조건을 확인하라"는 의미입니다.
# 여러 조건을 순차적으로 검사할 때 사용합니다
# -----------------------------------------------------------------------------

score = 7
if score >= 9:
    print("1등급")
elif score >= 7:
    print("2등급")
elif score >= 5:
    print("3등급")
else:
    print("Fail")

# 📊 더 자세한 성적 시스템
print("\n=== 상세한 성적 평가 시스템 ===")
score = 85

if score >= 95:
    grade = "A+"
    message = "최우수"
elif score >= 90:
    grade = "A"
    message = "우수"
elif score >= 85:
    grade = "B+"
    message = "양호"
elif score >= 80:
    grade = "B"
    message = "보통"
elif score >= 70:
    grade = "C"
    message = "미흡"
elif score >= 60:
    grade = "D"
    message = "부족"
else:
    grade = "F"
    message = "재시험"

print(f"점수: {score}점")
print(f"등급: {grade}")
print(f"평가: {message}")

# 🎮 게임 레벨 시스템
print("\n=== 게임 레벨 시스템 ===")
player_level = 25

if player_level >= 50:
    tier = "마스터"
    bonus_exp = 100
elif player_level >= 30:
    tier = "다이아"
    bonus_exp = 75
elif player_level >= 20:
    tier = "골드"
    bonus_exp = 50
elif player_level >= 10:
    tier = "실버"
    bonus_exp = 25
else:
    tier = "브론즈"
    bonus_exp = 10

print(f"현재 레벨: {player_level}")
print(f"티어: {tier}")
print(f"보너스 경험치: {bonus_exp}")

# -----------------------------------------------------------------------------
# 🏗️ 중첩 조건문 (Nested Conditionals)
# 조건문 안에 또 다른 조건문을 넣는 구조입니다
# -----------------------------------------------------------------------------

age = 18
student = False

if age >= 19:
    if student:
        print("성인이며 학생입니다.")
        print("학생 할인 혜택을 받을 수 있습니다.")
    else:
        print("성인이며 학생이 아닙니다.")
        print("일반 요금이 적용됩니다.")
else:
    print("성인이 아닙니다")
    if age >= 13:
        print("청소년 요금이 적용됩니다.")
    else:
        print("어린이 요금이 적용됩니다.")

# 🎫 영화관 요금 시스템 (복잡한 중첩 예시)
print("\n=== 영화관 요금 시스템 ===")
age = 16
is_student = True
is_weekend = False
movie_type = "일반"  # "일반", "프리미엄", "IMAX"

base_price = 0

# 나이별 기본 요금 설정
if age >= 65:
    base_price = 7000  # 경로 우대
elif age >= 19:
    base_price = 12000  # 성인
elif age >= 13:
    base_price = 9000   # 청소년
else:
    base_price = 8000   # 어린이

# 학생 할인
if is_student and age >= 13:
    base_price -= 1000
    print("학생 할인 1000원 적용")

# 주말 할증
if is_weekend:
    base_price += 2000
    print("주말 할증 2000원 적용")

# 영화 타입별 추가 요금
if movie_type == "프리미엄":
    base_price += 3000
elif movie_type == "IMAX":
    base_price += 5000

print(f"나이: {age}세")
print(f"학생 여부: {'예' if is_student else '아니오'}")
print(f"주말 여부: {'예' if is_weekend else '아니오'}")
print(f"영화 타입: {movie_type}")
print(f"최종 요금: {base_price:,}원")
