# 학생 점수 딕셔너리
grades = {
    "Huang": {"Test":71},
    "John": {"Test":65},
    "Jung": {"Test":100},
    "Darryl": {"Test":89}
}

# 학생 이름을 리스트로 저장
student = ["Huang", "John", "Jung", "Darryl"]

# 합격자와 탈락자를 저장할 리스트
pass_list = []
fail_list = []

# 조건문으로 각 학생 합격/탈락 판별
if grades[student[0]]["Test"] <= 70:
    print("시험 탈락")
    fail_list.append(student[0])
else:
    print("시험 합격")
    pass_list.append(student[0])

if grades[student[1]]["Test"] <= 70:
    print("시험 탈락")
    fail_list.append(student[1])
else:
    print("시험 합격")
    pass_list.append(student[1])

if grades[student[2]]["Test"] <= 70:
    print("시험 탈락")
    fail_list.append(student[2])
else:
    print("시험 합격")
    pass_list.append(student[2])

if grades[student[3]]["Test"] <= 70:
    print("시험 탈락")
    fail_list.append(student[3])
else:
    print("시험 합격")
    pass_list.append(student[3])

# 리스트를 튜플로 변환
pass_tuple = tuple(pass_list)
fail_tuple = tuple(fail_list)

# 집합(set)으로 중복 없는 합격자 명단 생성
pass_set = set(pass_tuple)

# 결과 출력
print("\n합격자 튜플:", pass_tuple)
print("탈락자 튜플:", fail_tuple)
print("합격자 집합:", pass_set)

# 질문? ('John',) 이렇게 '뒤에 , 들어가나요?
# => Python에서 튜플을 만들 때 요소가 하나만 있으면 자동으로 쉼표(,)가 추가됩니다. Python이 단일 요소 튜플과 일반 괄호를 구분하기 위한 문법 규칙입니다!
