grades = {
    "Huang": {"Test":71},
    "John": {"Test":65},
    "Jung": {"Test":100},
    "Darryl": {"Test":89}
}

# 학생 이름을 리스트로 저장
student=["Huang", "John", "Jung", "Darryl"]

# 합격자와 탈락자 명단을 튜플로 저장
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
