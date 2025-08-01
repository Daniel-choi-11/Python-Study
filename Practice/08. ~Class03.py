import pytz
from datetime import datetime
for tz in pytz.all_timezones:
    print(tz)

Country = {
    "미국": "US/Eastern",
    "한국": "Asia/Seoul", 
    "영국": "Europe/London",
    "일본": "Asia/Tokyo",
    "프랑스": "Europe/Paris",
    "싱가포르": "Singapore",
    "러시아": "Europe/Moscow"
}
now_ny = datetime.now(pytz.timezone('America/New_York'))


def timezone(userinput):
    now_tz = datetime.now(pytz.timezone(userinput))
    if userinput not in Country:
        return f"{userinput}는 지원하지 않습니다."
    if userinput in Country:
        return f"{userinput}의 시간대는: {now_tz}"



def calculator(userinput1, userinput2):
    if userinput1 not in Country:
        return f"{userinput1}는 지원하지 않습니다."
    if userinput2 not in Country:
        return f"{userinput2}는 지원하지 않습니다."
    if userinput1, userinput2 in 


'''
시차 계산기
- 원하는 나라들간의 시차를 구하기 위해 나라 입력 가능
- 나라입력을 하면 시간대 출력 (ex. 나라이름= GMT+9)

코드 순서
- 각 나라들 시간대 저장
- input으로 나라를 넣으면 시간대 출력 기능 만들기

- input으로 원하는 2를 넣은다음, 나라들 간의 시차 계산기능 만들기
- 
'''

# 좋은 버전
def timezone(country):
    if country not in Country:
        return f"{country}는 지원하지 않아요."
    tz = pytz.timezone(Country[country])
    now = datetime.now(tz)
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"{country} 현재 시간: {time_str}"

user_input = input("나라 이름을 입력하세요: ")
print(timezone(user_input))
