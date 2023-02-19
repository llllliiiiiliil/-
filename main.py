import school

a = school.Student('kim',1)
mathTeacher = school.Teacher('kim','math')

ban1 = school.Class(mathTeacher,1)
ban1.introducing()
ban1.addstudent(a)
ban1.introducing()