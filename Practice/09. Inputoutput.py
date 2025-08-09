with open("StudentGrade.txt", "w") as file:
    file.write("최정의 성적: 100점\n")
    file.write("지호의 성적: 80점\n")
    file.write("현호의 성적: 85점\n")
    file.write("시후의 성적: 90점")

with open("StudentGrade.txt", "r") as file:
    a=file.read()

print(a)


# 좋은 예시
'''
with open("grades.txt", "r") as file:
    for line in file:
        name, grade = line.strip().split(": ")
        print(f"{name}의 성적: {grade}")
'''
