class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
        self.math = 0
        self.english = 0

    def studyMath(self):
        print("수학공부했습니다 수학 능력이 10 올랐어요")
        self.math += 10
    def greeting(self):
        print(f"안녕하세요 저는 {self.name}입니다 저의 학년은 {self.grade}학년 입니다 저의 수학 능력은 {self.math}입니다 저의 영어 능력은 {self.english}입니다")



class Teacher:
    def __init__(self,sub,name):
        self.sub = sub
        self.name = name

    def greeting(self):
        print(f"안녕하세요 저는 {self.name}입니다 제 담당 과목은 {self.sub}입니다")

class Class:
    def __init__(self,teacher, ban):
        self.teacher = teacher
        self.student = []
        self.ban = ban

    def addstudent(self,student):
        self.student.append(student)


    def introducing(self):
        nameList = []
        for i in self.student:
            nameList.append(i.name)
        print(f"{self.ban}반의 담당 선생님은{self.teacher.name}이고 학생은{nameList}이다 ")
