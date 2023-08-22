class Student:
    def __init__(self, name, kor, math):
        self.name = name
        self.kor = kor
        self.math = math
        
    def average(self):
        print((self.kor + self.math)/2)

student_li = []
student_li.append(Student('choisugil', 88, 70))
student_li.append(Student('sdf', 34, 52))
student_li.append(Student('grgd', 50, 32))

class G_student(Student):
    def __init__(self, name, kor, math):
        super().__init__(name, kor, math)


temp_student = G_student('asdf', 54, 45)

# for student in student_li:
#     print(student.name)
#     student.average()
#     print()
temp_student.average()
print(temp_student.name)
    