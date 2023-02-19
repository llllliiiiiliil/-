import school


a = school.Student('kim',1)
mathTeacher = school.Teacher('kim','math')

ban1 = school.Class(mathTeacher,1)
ban1.addstudent(a)
ban1.introducing()

b = school.Student('park',1)
ban1.addstudent(b)
ban1.introducing()
c = school.Student('jun',3)
ban1.addstudent(c)
ban1.introducing()
ban1.mathavg()
a.studyMath()
a.studyMath()
ban1.mathavg()
