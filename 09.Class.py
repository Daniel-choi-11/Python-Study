# class
# class란, 객체 지향 프로그래밍의 핵심개념으로, 파이썬에서 코드 재사용성과 구조화를 도와주는 도구이다.
# class를 사용하면, 데이터와 관련된 기능을 한곳에 모아관리할수있다.

# class와 객체란? (객체 (Object) 혹은 인스턴스 (Instance))
# class는 설계도의 역할을하고, 객체 혹은 인스턴스는 그 설계도에서 만들어진 개별항목
# 객체의 특징: 서로 영향을 주지않는다 


class jung:
    pass 

# class를 만드는 방법 
# 1. class 어떻게 만들지 구상하기
# 객체를 중심으로 어떤식으로 동작하게 할지 정하기.
# 2. class 만들기
# 구상을 한데로 class를 만들기.



# 간단한 클래스 정의
class Dog:
    # 클래스의 생성자 함수
    def __init__(self, name, age):
#__init__은 클래스의 생성자로, 객체가 생성될때 자동으로 호출된다. 이를 통해 객체의 초기 속성을 설정할수있다.
# self는 자기자신을 참조하기위해있다. (맨앞에서 나와야한다)
        self.name = name  # 속성 정의
        self.age = age

    # 함수 정의
    def bark(self):
        print(f"{self.name}가 멍멍 짖습니다.")

# 객체 생성
dog1 = Dog("바둑이", 3)
dog2 = Dog("초코", 5)

# 함수 호출
dog1.bark()  # 바둑이가 멍멍 짖습니다.
dog2.bark()  # 초코가 멍멍 짖습니다.


# class의 속성과 함수
# 속성 (Attribute): 속성은 객체의 상태나 데이터를 저장하는 변수이다.
# class의 생성자(__init__)에서 정의하며 self.속성명 형태로 선언합니다.
# 함수 (Method): 함수는 객체가 수행할수있는 동작을 정의하는 함수입니다.클래스 내에서 정의되며, 첫번째 매개변수로 self를 사용하여 해당개체의 속성에 접근하거나 다른함수로 호출할수있습니다.


# 상속 (inheritance)
# 상속이란 어떤고유한 기능을 새로운 클래스한테 물려주는 개념이다
# A가 가지고있는 기능을 새로운 클래스한테 물려준다

# 부모 클래스(기본 클래스)로부터 상속받은 자식 클래스(파생 클래스)는 부모 클래스의 모든 속성과 함수를 물려받으며,
# 필요에 따라 새로운 속성이나 함수를 추가하거나 기존 함수를 재정의할 수 있다.

# 코드의 중복을 줄일수있다.
# 기존 클래스의 기능을 확장할수있다



# 부모 클래스
class animal:
    def __init__(self,name):
        self.name=name
        
    def speak(self):
        print(f"{self.name}가 소리를 냅니다")


# 자식 클래스
class cat(animal):
    def speak(self):
        print(f"{self.name}가 야옹 소리를 냅니다")

g=cat("나비")

g.speak()

# cat class(자식)는 animal class(부모)를 상속받아, speak함수를 재정의(overriding)하였습니다


# class 변수와 instance 변수

# class 변수란, class 전체에서 공유되는 변수이다.
# instance 변수란, 각 객체에서 유지되는 변수이다.

class circle:
    pi=3.14 #class 변수
    def __init__(self,radius):
        self.radius=radius #instance 변수
    def area(self):
        return circle.pi * (self.radius ** 2)

