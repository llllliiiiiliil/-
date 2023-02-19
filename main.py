import school

a = school.Student('kim',1)
b = school.Student("lee",2)
c = school.Student("park",3)

a.greeting()


mathTeacher = school.Teacher('math','수학선생님')
enTeacher = school.Teacher('english','영어선생님')

mathTeacher.greeting()
enTeacher.greeting()

ban1 = school.Class(1,"선생님1","학생1")
