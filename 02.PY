#List와 Tuple
#List와 Tuple은 데이터를 저장하고 관리하는데 가장 기본적인 자료구조다.

#1 list
#리스트는 여러 개의 값을 순서대로 저장할 수 있는 자료구조입니다. 리스트는 대괄호 []로 정의되며, 각 항목은 콤마로 구분됩니다. 리스트는 값을 추가, 삭제, 수정할 수 있습니다.

student = ["Minsoo","Daniel","Jung"]
print(student)

#index
#index는 0,1,2... 또는 -1,-2,-3...(이건 뒤에서부터)
print(student[2])

#항목추가하기/append()
student.append("Jang")
print(student)

#항목삽입하기/insert()
student.insert(1,"Hu")
print(student)

#항목제거하기/remove()
student.remove("Jang")
print(student)

#index으로 항목제거하기/pop()
student.pop(-2)
print(student)

#항목찾기/index()
index=student.index("Hu")
print(index)

#list slicing
#리스트의 특정 부분을 추출할때 슬라이싱을 사용합니다.
#[start_index:stop_index:step]
#start_index = 슬라이싱을 시작할 위치. 
#stop_index = 슬라이싱을 멈출 위치. stop을한 직전위치만 포함 
#step =  몇 칸씩 건너뛰며 추출할지
# start, stop, step의 구분점 : 
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # [1, 2, 3]
print(numbers[:3])   # [0, 1, 2]
print(numbers[::2])  # [0, 2, 4]

#2 tuple
#튜플은 리스트와 유사하지만 생성된후에는 값을 변경할수없다. 튜플은 ()로 정의되며 각항목은 ,로 구분. 바뀌지않는 데이터를 저장하는데 유용합니다.
z = ("Blue", "Red", "Green")
print(z)

#2-1 tuple의 index와 주요기능
#tuple의 각 항목은 list와 동일하게 index를 통해 접근할수있습니다
print(z[2])
print(z[-1])

#tuple에서 항목찾기(index()) 기능은 그대로 사용가능.

#항목개수세기/count()
#tuple에서 특정값이 몇번 나타내는지를 셀때 count함수를 사용합니다
f = [3,43,1,3,5,7,3,3]
print(f.count(3))
#tuple 사용예시: tuple은 변경이 필요하지않는 데이터를 저장할때 사용한다.

#Dictionary {}
#Dictionary는 키-값 (key-value) 쌍으로 저장하는 자료구조입니다. {}로 정의되며, 콜론으로 구분합니다 
j = {
    "name": "최정",
    "age": 13,
    "gender": "male"
}
print(j)

#값접근하기 []
name = j["name"]
print(name)

#값추가및 수정하기
j["grade"]= 8
s=j["grade"]
print(s)

j["age"]=11
print(j)

#값 제거하기 (del)
del j["age"]
print(j)

#모든 기와 값 돌아가며 출력하기 (item())
for key, value in j.items():
    print(f"{key}: {value}")

#모든 키가져오기 (keys())
a=j.keys()
print(a)

#집합 (set)
#집합은 중복되지않는 고유한 값들을 저장하는 자료구조입니다. {}로 정의되며, 순서가 보장되지않습니다
numbers2 = {1,2,3,4,5}
print(numbers2)

#항복추가하기 (add())
numbers2.add(6)
numbers2.add(3) #이미 존재하는 값은 추가되지않습니다
print(numbers2)

numbers2.remove(3)
print(numbers2)
