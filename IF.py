#조건문
#if문 
level=12
if level<10:
    print("레벨을 더올리고 다시 오십시오")
#if문은 "만약에"라는 뜻을 가지니, if문은 특정 카테고리한테만 코드블록을 실행하고싶은거가 있을시 쓰인다. 
#들여쓰기가 매우 중요하다.

#if-else 문
if level<10:
    print("레벨을 더올리고 다시 오십시오")
else:
    print("축하합니다! 레벨 10 이상입니다")

#if-elif-else 문
#elif문은 그렇지않다면 다른 조건을 확인하라는 의미입니다.

score=7
if score>=9:
    print("1등급")
elif score>=7:
    print("2등급")
else:
    print("Fail")

#중첩조건문 
age=18
student=False
if age >=19 :
    if student:
        print("성인이며 학생입니다.") 
    #19세 이상이며 학생일일때
    else:
        print("성인이며 학생이 아닙니다.")
else:
    print("성인이 아닙니다")
