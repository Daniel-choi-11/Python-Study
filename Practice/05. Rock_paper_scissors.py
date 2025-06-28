#input 없이
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

