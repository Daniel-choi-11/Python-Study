# =============================================================================
# 📚 List와 Tuple - Python 자료구조
# List와 Tuple은 데이터를 저장하고 관리하는데 가장 기본적인 자료구조입니다.
# =============================================================================

# -----------------------------------------------------------------------------
# 📝 1. List (리스트)
# 리스트는 여러 개의 값을 순서대로 저장할 수 있는 자료구조입니다. 
# 리스트는 대괄호 []로 정의되며, 각 항목은 콤마로 구분됩니다. 
# 리스트는 값을 추가, 삭제, 수정할 수 있습니다.
# -----------------------------------------------------------------------------

# 리스트 생성
student = ["Minsoo", "Daniel", "Jung"]
print(student)  # ['Minsoo', 'Daniel', 'Jung']

# 🔢 인덱스 (Index)
# index는 0, 1, 2... 또는 -1, -2, -3...(이건 뒤에서부터)
print(student[2])   # Jung (앞에서 3번째)
print(student[-1])  # Jung (뒤에서 첫 번째)
print(student[0])   # Minsoo (첫 번째)

# ➕ 항목 추가하기 / append()
# 리스트 끝에 새로운 항목 추가
student.append("Jang")
print(student)  # ['Minsoo', 'Daniel', 'Jung', 'Jang']

# 📌 항목 삽입하기 / insert()
# 지정한 위치에 새로운 항목 삽입
student.insert(1, "Hu")
print(student)  # ['Minsoo', 'Hu', 'Daniel', 'Jung', 'Jang']

# ❌ 항목 제거하기 / remove()
# 특정 값을 찾아서 제거 (첫 번째 발견된 값만)
student.remove("Jang")
print(student)  # ['Minsoo', 'Hu', 'Daniel', 'Jung']

# 🗑️ 인덱스로 항목 제거하기 / pop()
# 지정한 인덱스의 항목을 제거하고 반환
student.pop(-2)  # 뒤에서 두 번째 항목 제거
print(student)   # ['Minsoo', 'Hu', 'Jung']

# 🔍 항목 찾기 / index()
# 특정 값의 인덱스를 반환
index = student.index("Hu")
print(index)  # 1

# ✂️ List Slicing (리스트 슬라이싱)
# 리스트의 특정 부분을 추출할 때 슬라이싱을 사용합니다.
# [start_index:stop_index:step]
# start_index = 슬라이싱을 시작할 위치
# stop_index = 슬라이싱을 멈출 위치 (stop 직전 위치까지만 포함)
# step = 몇 칸씩 건너뛰며 추출할지

numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # [1, 2, 3] (인덱스 1부터 3까지)
print(numbers[:3])    # [0, 1, 2] (처음부터 인덱스 2까지)
print(numbers[3:])    # [3, 4, 5] (인덱스 3부터 끝까지)
print(numbers[::2])   # [0, 2, 4] (처음부터 끝까지 2칸씩)
print(numbers[::-1])  # [5, 4, 3, 2, 1, 0] (역순)

# 📊 기타 유용한 리스트 메소드
fruits = ["apple", "banana", "cherry", "banana"]

# 길이 확인
print(len(fruits))           # 4

# 특정 값 개수 세기
print(fruits.count("banana")) # 2

# 정렬
numbers_unsorted = [3, 1, 4, 1, 5]
numbers_unsorted.sort()      # 원본 리스트를 정렬
print(numbers_unsorted)      # [1, 1, 3, 4, 5]

# 리스트 확장
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)  # list1에 list2의 모든 요소 추가
print(list1)         # [1, 2, 3, 4, 5, 6]

# 리스트 연결
combined = [1, 2] + [3, 4]
print(combined)      # [1, 2, 3, 4]

# -----------------------------------------------------------------------------
# 🔒 2. Tuple (튜플)
# 튜플은 리스트와 유사하지만 생성된 후에는 값을 변경할 수 없습니다. 
# 튜플은 ()로 정의되며 각 항목은 ,로 구분합니다. 
# 바뀌지 않는 데이터를 저장하는 데 유용합니다.
# -----------------------------------------------------------------------------

# 튜플 생성
z = ("Blue", "Red", "Green")
print(z)  # ('Blue', 'Red', 'Green')

# 다양한 튜플 생성 방법
colors = ("Blue", "Red", "Green")        # 괄호 사용
coordinates = 10, 20                     # 괄호 생략 가능
single_item = ("Hello",)                 # 단일 항목은 콤마 필요
empty_tuple = ()                         # 빈 튜플

print(coordinates)  # (10, 20)
print(single_item)  # ('Hello',)

# 🔢 Tuple의 인덱스와 주요 기능
# tuple의 각 항목은 list와 동일하게 index를 통해 접근할 수 있습니다
print(z[2])   # Green (세 번째 항목)
print(z[-1])  # Green (마지막 항목)
print(z[0])   # Blue (첫 번째 항목)

# 🔍 tuple에서 항목 찾기 (index()) 기능은 그대로 사용 가능
index_of_red = z.index("Red")
print(index_of_red)  # 1

# 📊 항목 개수 세기 / count()
# tuple에서 특정 값이 몇 번 나타나는지를 셀 때 count 함수를 사용합니다
f = (3, 43, 1, 3, 5, 7, 3, 3)
print(f.count(3))  # 4 (숫자 3이 4번 나타남)

# 튜플의 길이
print(len(z))  # 3

# ✂️ 튜플 슬라이싱
# 튜플도 리스트와 동일하게 슬라이싱 가능
numbers_tuple = (0, 1, 2, 3, 4, 5)
print(numbers_tuple[1:4])   # (1, 2, 3)
print(numbers_tuple[:3])    # (0, 1, 2)
print(numbers_tuple[::2])   # (0, 2, 4)

# 🔄 튜플 언패킹 (Tuple Unpacking)
point = (3, 5)
x, y = point  # 튜플의 값을 각각의 변수에 할당
print(f"x: {x}, y: {y}")  # x: 3, y: 5

# 여러 값 동시 할당
a, b, c = ("apple", "banana", "cherry")
print(a, b, c)  # apple banana cherry

# 📋 List vs Tuple 비교
print("\n" + "="*50)
print("List vs Tuple 비교")
print("="*50)

# List (변경 가능)
my_list = [1, 2, 3]
my_list[0] = 10  # 값 변경 가능
print(f"변경된 리스트: {my_list}")  # [10, 2, 3]

# Tuple (변경 불가능)
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # 오류 발생! 주석 처리
print(f"튜플: {my_tuple}")  # (1, 2, 3)

# 🎯 Tuple 사용 예시
# 튜플은 변경이 필요하지 않는 데이터를 저장할 때 사용합니다

# 좌표 저장
coordinates = (37.5665, 126.9780)  # 서울 좌표
print(f"위도: {coordinates[0]}, 경도: {coordinates[1]}")

# 데이터베이스 레코드
person = ("김철수", 30, "서울", "개발자")
name, age, city, job = person  # 언패킹
print(f"이름: {name}, 나이: {age}, 도시: {city}, 직업: {job}")

# 함수에서 여러 값 반환
def get_name_age():
    return "이영희", 25

person_name, person_age = get_name_age()
print(f"함수에서 반환: {person_name}, {person_age}")

# RGB 색상 코드
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

colors_dict = {
    "빨강": red,
    "초록": green,
    "파랑": blue
}

print(f"빨간색 RGB: {colors_dict['빨강']}")

# 📝 정리
print("\n" + "="*50)
print("📝 List와 Tuple 정리")
print("="*50)
print("List: 변경 가능, 대괄호 [], 동적 데이터")
print("Tuple: 변경 불가능, 소괄호 (), 고정 데이터")
print("둘 다 인덱싱, 슬라이싱, 반복문 사용 가능")

