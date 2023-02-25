class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Korean(Person):
    def hello(self):
        print(f"안녕하세요 저는 {self.name}입니다")
class Japanese(Person):
    def hello(self):
        print(f"こんにちは。私は{self.name}です。")

class British(Person):
    def hello(self):
        print(f"안녕하세요 저는 {self.name}입니다")

class French(Person):
    def hello(self):
        print(f"안녕하세요 저는 {self.name}입니다")