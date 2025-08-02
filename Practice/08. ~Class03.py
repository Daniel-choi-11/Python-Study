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
# -------------------------------------------------------------------

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

'''
def timezone(userinput):
    now_tz = datetime.now(pytz.timezone(userinput))
    if userinput not in Country:
        return f"{userinput}는 지원하지 않습니다."
    elif userinput in Country:
        return f"{userinput}의 시간대는: {now_tz}"

userinput= input()

문제점 및 개선점
1. userinput과 Country 딕셔너리
userinput에는 나라 이름(예: "한국")을 넣어야 하고, 이걸 Country 딕셔너리에서 타임존 문자열로 변환해야 함.

2. pytz.timezone에 직접 나라 이름을 넣으면 안 됨.그리고  "Asia/Seoul" 같은 타임존 문자열이 들어가야 함.
지금 코드는 userinput(= "한국" 등)를 직접 넣어서 에러가 남.
'''

# -------------------------------------------------------------------
# 개선한 버전
def timezone(country):
    if country not in Country:
        return f"{country}는 지원하지 않아요."
    tz = pytz.timezone(Country[country])
    now = datetime.now(tz)
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    return f"{country} 현재 시간: {time_str}"

user_input = input("나라 이름을 입력하세요: ")
print(timezone(user_input))

# -------------------------------------------------------------------
# 시차 계산기

def calculator(country1, country2):
    if country1 not in Country:
        return f"{country1}는 지원하지 않습니다."
    if country2 not in Country:
        return f"{country2}는 지원하지 않습니다."
    tz1 = pytz.timezone(Country[country1])
    tz2 = pytz.timezone(Country[country2])
    now = datetime.now(timezone.utc)

    now_tz1 = now.astimezone(tz1)
    now_tz2 = now.astimezone(tz2)
    offset1 = now_tz1.utcoffset()
    offset2 = now_tz2.utcoffset()
    if offset1 is None or offset2 is None: 
        return "오류가 발생했습니다"
    diff_hours = int(abs((offset1 - offset2).total_seconds()) // 3600)
    return f"{country1}와 {country2}의 시차는: {diff_hours}시간"

country1= input("첫번째 나라를 입력하세요:").strip()
country2= input("처음에 입력하신 나라의 시차를 알고싶은 나라를 입력하세요:").strip()
print(calculator(country1,country2))


