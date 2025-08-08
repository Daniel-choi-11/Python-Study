# 파일 입출력
# 파일 입출력은 프로그램에서 데이터를 파일에 저장하거나, 파일로부터 데이터를 읽어오는 작업입니다
# 파일 입출력을 통해 데이터를 영구적으로 불러오거나 저장할수있어, 프로그램의 활용범위를 넓힐수있다.

# 파일 열기
# 파일을 열기위해 open() 함수를 이용한다
# r (읽기 모드): 파일을 읽기 위해 사용하며, 파일이 존재하지 않으면 오류가 발생합니다.
# w (쓰기 모드): 파일에 데이터를 쓰기위해 사용하며 기존 파일이 있으면, 덮어쓴다. 파일이 없으면 새로 생성한다.
# a (추가 모드): 파일의 끝에 데이터를 추가합니다. 파일이 없으면 새로 생성합니다.
# r+ (읽기,쓰기 모드)
# w+ (읽기, 쓰기 모드: 그러나 기존내용은 삭제됨)
# a+ (읽기, 추가 모드)

# file= open("Test1.txt", "w")


# 파일 쓰기

file2= open("write1.txt", "w")
file2.write("안녕하세요!")
file2.close()
# 파일을 open() 하면, close() 함수 사용하기


# 파일 읽기
# read(): 파일의 전체 내용을 하나의 문자열로 읽는다
# readline(): 파일에서 한줄씩 읽습니다
# readlines(): 파일의 모든줄을 list로 읽습니다

file= open("Test1.txt", "r")
read1= file.readline()
while read1:
    print(read1.strip())
    read1= file.readline()

file.close()


# with문
# 자원을 획득하고, 사용하고, 반납할때 주로 사용한다

# with문을 사용한 파일 쓰기
with open("write1.txt", "w") as file2:
    file2.write("안녕하세요!")

# with문을 사용한 파일 읽기
with open("Test1.txt", "r") as file:
    a=file.read()
print(a)
