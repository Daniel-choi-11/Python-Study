import sys
# sys 모둘 
# 파이썬 인터프리터를 제어 할때 사용된다.

# sys.argv
# 반복문을 사용하여 명령행 인자를 불러올때 사용된다
# 명령행 인자를 사용할때

print("명령행 인자")
for arg in sys.argv:
    print(arg)

# sys.exit
# 인터프리터를 종료하는데 사용됩니다. 프로그램에서 오류가 발생하거나 예외가 발생했을 때, 즉시 종료하기 위해 사용될 수 있습니다.

'''
if ~:
    ~~
    sys.exit()
'''

# sys.path
# 모듈을 찾는 경로를 나타내는 list입니다.
# 함수를 사용하여 모듈을 추가할수있습니다.

# sys.stdin, sys.stdout, sys.stderr
# 표준 입력, 표준 출력, 표준 에러를 나타내는 파일 객체입니다
# 이 함수를 사용하여 입출력을 제어한다

# sys.platform 
# 현재 실행중인 platform을 나타낸다.

D=sys.platform
print(D)

# sys.version
# 파이썬의 버전을 나타낸다

# sys.getsizeof
# 객체의 크기를 바이트 단위롤 나타낸다.

#sys.stdin.readline()
# input이랑 같은 기능. 그러나 훨씬 빠르게 작동

# sys.getdefaultencoding
# 파이썬의 문자열 인코딩 단위
