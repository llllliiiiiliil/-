class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def greeting(self):
        print(f"안녕하세요 저는 {self.name}입니다 저의 학년은 {self.grade}학년 입니다")

class Teacher:
    def __init__(self,sub,name):
        self.sub = sub
        self.name = name

    def greeting(self):
        print(f"안녕하세요 저는 {self.name}입니다 제 담당 과목은 {self.sub}입니다")

class Class:
    def __init__(self,teacher,student, ban):
        self.teacher = teacher
        self.student = student
        self.ban = ban

    def introducing(self):
        print(f"{self.ban}반의 담당 선생님은{self.teacher}이고 학생은{self.student}이다 ")
