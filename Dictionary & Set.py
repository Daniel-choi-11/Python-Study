# =============================================================================
# 📚 Dictionary와 Set - Python 자료구조
# =============================================================================

# -----------------------------------------------------------------------------
# 🗂️ Dictionary {} 
# Dictionary는 키-값 (key-value) 쌍으로 저장하는 자료구조입니다. 
# {}로 정의되며, 콜론으로 구분합니다
# -----------------------------------------------------------------------------

# Dictionary 생성
j = {
    "name": "최정",
    "age": 13,
    "gender": "male"
}
print(j)  # {'name': '최정', 'age': 13, 'gender': 'male'}

# 🔍 값 접근하기 []
# 키를 사용하여 해당하는 값에 접근
name = j["name"]
print(name)  # 최정

# ➕ 값 추가 및 수정하기
# 새로운 키-값 쌍 추가
j["grade"] = 8
s = j["grade"]
print(s)  # 8

# 기존 값 수정
j["age"] = 11
print(j)  # {'name': '최정', 'age': 11, 'gender': 'male', 'grade': 8}

# ❌ 값 제거하기 (del)
# del 키워드를 사용하여 특정 키-값 쌍 제거
del j["age"]
print(j)  # {'name': '최정', 'gender': 'male', 'grade': 8}

# 🔄 모든 키와 값 돌아가며 출력하기 (items())
# for문과 items() 메소드를 사용하여 모든 키-값 쌍 순회
for key, value in j.items():
    print(f"{key}: {value}")
# name: 최정
# gender: male  
# grade: 8

# 🔑 모든 키 가져오기 (keys())
# keys() 메소드로 딕셔너리의 모든 키를 가져옴
a = j.keys()
print(a)  # dict_keys(['name', 'gender', 'grade'])

# 📦 모든 값 가져오기 (values())
# values() 메소드로 딕셔너리의 모든 값을 가져옴
values = j.values()
print(values)  # dict_values(['최정', 'male', 8])

# 🛡️ 안전한 값 접근 (get())
# get() 메소드 - KeyError 방지, 기본값 설정 가능
height = j.get("height", "정보 없음")
print(height)  # 정보 없음

age = j.get("age", 0)
print(age)  # 0

# ✅ 키 존재 확인 (in)
# in 키워드로 키가 존재하는지 확인
if "name" in j:
    print(f"이름: {j['name']}")

if "age" not in j:
    print("나이 정보가 없습니다")

# 🔄 Dictionary 업데이트 (update())
# 다른 딕셔너리나 키-값 쌍으로 업데이트
additional_info = {"height": 160, "hobby": "축구"}
j.update(additional_info)
print(j)  # {'name': '최정', 'gender': 'male', 'grade': 8, 'height': 160, 'hobby': '축구'}

# 🗑️ 값 제거하고 반환 (pop())
# pop() 메소드로 키를 제거하고 해당 값을 반환
removed_value = j.pop("hobby", "취미 없음")
print(f"제거된 취미: {removed_value}")  # 제거된 취미: 축구

# -----------------------------------------------------------------------------
# 🎯 집합 (Set)
# 집합은 중복되지 않는 고유한 값들을 저장하는 자료구조입니다. 
# {}로 정의되며, 순서가 보장되지 않습니다
# -----------------------------------------------------------------------------

# Set 생성
numbers2 = {1, 2, 3, 4, 5}
print(numbers2)  # {1, 2, 3, 4, 5}

# 🚨 빈 Set 생성 주의사항
empty_set = set()  # 올바른 방법
empty_dict = {}    # 이건 빈 Dictionary!
print(type(empty_set))   # <class 'set'>
print(type(empty_dict))  # <class 'dict'>

# ➕ 항목 추가하기 (add())
# 새로운 값 추가
numbers2.add(6)
numbers2.add(3)  # 이미 존재하는 값은 추가되지 않습니다
print(numbers2)  # {1, 2, 3, 4, 5, 6}

# ❌ 항목 제거하기 (remove() vs discard())
# remove() - 없으면 KeyError 발생
numbers2.remove(3)
print(numbers2)  # {1, 2, 4, 5, 6}

# discard() - 없어도 에러 안 남 (안전한 제거)
numbers2.discard(10)  # 에러 없음
print(numbers2)  # {1, 2, 4, 5, 6}

# 🔄 여러 항목 추가하기 (update())
numbers2.update([7, 8, 9])
print(numbers2)  # {1, 2, 4, 5, 6, 7, 8, 9}

# 🧹 모든 항목 제거 (clear())
temp_set = {1, 2, 3}
temp_set.clear()
print(temp_set)  # set()

# -----------------------------------------------------------------------------
# 🔢 집합 연산 (합집합, 차집합, 교집합)
# -----------------------------------------------------------------------------

m = {1, 2, 3, 4, 5, 6}
n = {4, 5, 6, 7, 8, 9}

# 1. 합집합 (union())
# 합집합은 모든 집합들을 더한 집합이다.
print("합집합:")
print(m.union(n))         # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(m | n)              # 연산자 사용

# 2. 차집합 (difference())
# 첫 집합에는 있지만, 두 번째에는 없는 항목만 포함한 집합이다
print("차집합:")
print(m.difference(n))    # {1, 2, 3}
print(m - n)              # 연산자 사용

# 3. 교집합 (intersection())
# 두 집합이 만나는 곳만 포함한 집합이다.
print("교집합:")
print(m.intersection(n))  # {4, 5, 6}
print(m & n)              # 연산자 사용

# 4. 대칭차집합 (symmetric_difference())
# 두 집합 중 하나에만 있는 원소들
print("대칭차집합:")
print(m.symmetric_difference(n))  # {1, 2, 3, 7, 8, 9}
print(m ^ n)                      # 연산자 사용

# 5. 부분집합 (issubset())
# a와 b가 있을 때, a 값이 b의 값 안에 모두 포함되어 있다면 a는 b의 부분집합이라 부른다.
subset_test = {4, 5}
print(f"{subset_test}이 {m}의 부분집합인가? {subset_test.issubset(m)}")  # True
print(m.issubset(n))      # False (m이 n의 부분집합이 아님)

# 6. 상위집합 (issuperset())
# a와 b가 있을 때, b 값이 a의 값 안에 모두 포함되어 있다면 a는 b의 상위집합이라 부른다.
print(f"{m}이 {subset_test}의 상위집합인가? {m.issuperset(subset_test)}")  # True
print(m.issuperset(n))    # False (m이 n의 상위집합이 아님)

# 7. 서로소 집합 (isdisjoint())
# 교집합이 없는 집합들
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(f"{set1}과 {set2}는 서로소인가? {set1.isdisjoint(set2)}")  # True

# -----------------------------------------------------------------------------
# 💼 실무에서 자주 쓰이는 패턴
# -----------------------------------------------------------------------------

print("\n=== 실무 활용 예시 ===")

# 📊 Dictionary 활용 - Counter 패턴 (빈도수 세기)
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"문자 빈도수: {char_count}")

# 📝 Dictionary 활용 - 그룹화 패턴
students = [
    {"name": "철수", "grade": "A"},
    {"name": "영희", "grade": "B"},
    {"name": "민수", "grade": "A"},
    {"name": "지영", "grade": "C"}
]

grade_groups = {}
for student in students:
    grade = student["grade"]
    if grade not in grade_groups:
        grade_groups[grade] = []
    grade_groups[grade].append(student["name"])

print(f"성적별 그룹: {grade_groups}")

# 🔍 Set 활용 - 중복 제거
numbers_list = [1, 2, 2, 3, 3, 4, 5, 1, 2]
unique_numbers = list(set(numbers_list))
print(f"중복 제거된 숫자: {unique_numbers}")

# 🤝 Set 활용 - 공통 원소 찾기
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"공통 원소: {common}")

# 🔐 Set 활용 - 권한 검사
user_permissions = {"read", "write"}
required_permissions = {"read", "write"}
admin_permissions = {"read", "write", "admin"}

if required_permissions.issubset(user_permissions):
    print("일반 권한: 접근 허용")
else:
    print("일반 권한: 접근 거부")

if admin_permissions.issubset(user_permissions):
    print("관리자 권한: 접근 허용")
else:
    print("관리자 권한: 접근 거부")

# 📚 Dictionary 활용 - 학생 성적 관리 (확장된 예시)
grades = {
    "Hiwoo": {"수학": 85, "영어": 90, "과학": 80},
    "Jang": {"수학": 92, "영어": 88, "과학": 89},
    "Greg": {"수학": 100, "영어": 100, "과학": 100}
}

# 특정 학생의 성적 조회
print(f"Hiwoo의 수학 성적: {grades['Hiwoo']['수학']}")

# 모든 학생의 수학 성적 출력
print("\n=== 모든 학생의 수학 성적 ===")
for student, subjects in grades.items():
    print(f"{student}의 수학 성적: {subjects['수학']}")

# 평균 성적 계산
print("\n=== 학생별 평균 성적 ===")
for student, subjects in grades.items():
    average = sum(subjects.values()) / len(subjects)
    print(f"{student}의 평균: {average:.1f}")

# 과목별 전체 평균
print("\n=== 과목별 전체 평균 ===")
subjects = ["수학", "영어", "과학"]
for subject in subjects:
    total = sum(grades[student][subject] for student in grades)
    average = total / len(grades)
    print(f"{subject} 평균: {average:.1f}")

# -----------------------------------------------------------------------------
# 🔄 Dictionary와 Set 변환
# -----------------------------------------------------------------------------

print("\n=== 자료구조 변환 ===")

# Dictionary의 키들을 Set으로
dict_example = {"a": 1, "b": 2, "c": 3}
keys_set = set(dict_example.keys())
print(f"Dictionary 키들의 Set: {keys_set}")

# Dictionary의 값들을 Set으로 (중복 제거됨)
dict_with_duplicates = {"a": 1, "b": 2, "c": 1, "d": 3}
values_set = set(dict_with_duplicates.values())
print(f"Dictionary 값들의 Set: {values_set}")

# Set을 Dictionary로 (인덱스와 함께)
sample_set = {"사과", "바나나", "오렌지"}
set_to_dict = {i: item for i, item in enumerate(sample_set)}
print(f"Set을 Dictionary로: {set_to_dict}")

# -----------------------------------------------------------------------------
# 📋 Dictionary와 Set의 차이점 및 성능
# -----------------------------------------------------------------------------

print("\n=== Dictionary vs Set 비교 ===")

# Dictionary는 key와 value로 이루어져 있다. Set은 고유한 값들의 모음 구조이다.
# Dictionary는 구조화된 데이터를 사용하고, Set은 중복제거와 집합 연산을 사용한다.

# 성능 테스트 (간단한 예시)
import time

# 큰 데이터셋으로 검색 속도 비교
large_list = list(range(100000))
large_set = set(large_list)
large_dict = {i: f"value_{i}" for i in large_list}

# List에서 검색 (느림)
start = time.time()
99999 in large_list
list_time = time.time() - start

# Set에서 검색 (빠름)
start = time.time()
99999 in large_set
set_time = time.time() - start

# Dictionary에서 키 검색 (빠름)
start = time.time()
99999 in large_dict
dict_time = time.time() - start

print(f"List 검색 시간: {list_time:.6f}초")
print(f"Set 검색 시간: {set_time:.6f}초")
print(f"Dictionary 검색 시간: {dict_time:.6f}초")

# -----------------------------------------------------------------------------
# 💡 고급 활용 팁
# -----------------------------------------------------------------------------

print("\n=== 고급 활용 팁 ===")

# Dictionary Comprehension
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(f"제곱수 Dictionary: {squares_dict}")

# Set Comprehension
even_squares = {x**2 for x in numbers if x % 2 == 0}
print(f"짝수의 제곱수 Set: {even_squares}")

# 중첩 Dictionary 안전하게 접근하기
nested_dict = {
    "user1": {
        "profile": {
            "name": "홍길동",
            "age": 25
        }
    }
}

# 안전한 접근 방법
name = nested_dict.get("user1", {}).get("profile", {}).get("name", "이름 없음")
print(f"사용자 이름: {name}")

# defaultdict 패턴 (collections 모듈 없이)
def get_default_dict():
    class DefaultDict(dict):
        def __init__(self, default_factory):
            self.default_factory = default_factory
            super().__init__()
        
        def __getitem__(self, key):
            if key not in self:
                self[key] = self.default_factory()
            return super().__getitem__(key)
    
    return DefaultDict

# 사용 예시
dd = get_default_dict()(list)
dd['fruits'].append('apple')
dd['fruits'].append('banana')
print(f"DefaultDict 예시: {dict(dd)}")

# -----------------------------------------------------------------------------
# 🎯 요약 정리
# -----------------------------------------------------------------------------

print("\n=== 📋 최종 요약 ===")

print("""
Dictionary: 
- 키-값 쌍으로 데이터 저장
- 구조화된 데이터 관리에 적합
- 빠른 검색과 데이터 매핑에 사용
- 주요 메소드: get(), keys(), values(), items(), update(), pop()

Set:
- 고유한 값들만 저장 (중복 불가)
- 집합 연산 (합집합, 교집합, 차집합 등)에 적합
- 중복 제거와 멤버십 테스트에 사용
- 주요 메소드: add(), remove(), discard(), union(), intersection(), difference()

성능:
- Dictionary와 Set 모두 해시 테이블 기반으로 O(1) 평균 검색 시간
- List보다 멤버십 테스트가 훨씬 빠름

활용 팁:
- Dictionary: 데이터 매핑, 카운팅, 그룹화
- Set: 중복 제거, 집합 연산, 빠른 멤버십 테스트
""")
