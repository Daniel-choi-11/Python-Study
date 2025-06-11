grades = {
    "Huang": {"Test":71},
    "John": {"Test":65},
    "Jung": {"Test":100},
    "Darryl": {"Test":89}
}

# 학생 이름을 리스트로 저장
student=["Huang", "John", "Jung", "Darryl"]

# 합격자와 탈락자 명단을 
# 리스트로 저장
pass_list = []
fail_list = []

# 조건문으로 합격/탈락 분류
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
pass_tuple= tuple(pass_list)
fail_tuple= tuple(fail_list)

# 합격자 집합(set) 생성 (중복 제거 목적)
pass_set= set(pass_tuple)
# 결과 출력
print(pass_set)



print("합격자 튜플:", pass_tuple)
print("탈락자 튜플:", fail_tuple)
print("합격자 집합:", pass_set)
