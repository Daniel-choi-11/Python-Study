# input 없이
import random
def rock_paper_scissors(user_choice):
    choices = ["가위", "바위", "보"]
    computer_choice = random.choice(choices)
    if user_choice ==computer_choice:
        return "비겼습니다"
    elif (user_choice == "가위" and computer_choice == "보") or \
        (user_choice == "바위" and computer_choice == "가위")or \
        (user_choice == "보" and computer_choice == "바위"):
        return "승리"
    else:
        return "패배"

user= input()


print(rock_paper_scissors("____"))

=================

# 개선판

import random

def rock_paper_scissors():
    choices = ["가위", "바위", "보"]
    
    print("무엇을 내실건가요?")
    user_choice = input("당신의 선택:")
    
    if user_choice not in choices:
        return "잘못 입력된 값입니다."
        
    computer_choice = random.choice(choices)
    
    print(f"당신의 선택 : {user_choice}")
    print(f"컴퓨터의 선택 : {computer_choice}")
    

    # 결과판정
    
    if user_choice == computer_choice:
        return "비겼습니다"
    elif (user_choice == "가위" and computer_choice == "보") or \
        (user_choice == "바위" and computer_choice == "가위")or \
        (user_choice == "보" and computer_choice == "바위"):
        return "승리"
    else:
        return "패배"
    
result = rock_paper_scissors()
print(result)
