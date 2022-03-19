#20CE046 SAKINA KUTERWADLI
#PRACTICAL 9
# Consider an example of declaring the examination result.
#  Design three classes: Student, Exam, and Result.
#  The Student class has data members such as those representing rollNumber, Name, etc.
#  Create the class Exam by inheriting Student class. 
#  The Exam class adds fields representing the marks scored in six subjects.
#  Derive Result from the Exam class, and it has its own fields such as total_marks.
#  Write an interactive program to model this relationship.
##github repository link: 
class Student:
    def _init_(self,name,roll):
        self.name=name
        self.roll=roll
    def stu_info(self):
        print('Name of student is',self.name)
        print('Roll number is is ',self.roll)

class Exam(Student):
    def _init_(self,name,id,a1,a2,a3,a4,a5,a6):#for marks of 6 subjects
        Student._init_(self,name,id)
        self.a1=a1
        self.a2=a2
        self.a3=a3
        self.a4=a4
        self.a5=a5
        self.a6=a6
    

class Result(Exam):
    def _init_(self,name,roll,a1,a2,a3,a4,a5,a6):
        Exam._init_(self,name,roll,a1,a2,a3,a4,a5,a6)
        self.Total_Marks=a1+a2+a3+a4+a5+a6
    def f_result(self):
        return self.Total_Marks


print("How many student's data you want to print:")
n=int(input())
for i in range(1,n+1):
    print('Enter  the Name of  the student:')
    name=str(input())
    print("Enter Roll No of the student: ")
    roll=str(input())
    print("Enter marks for 6 subjects: ")
    print("Enter marks 1")
    a1=int(input())
    print("Enter marks 2")
    a2=int(input())
    print("Enter marks 3")
    a3=int(input())
    print("Enter marks 4")
    a4=int(input())
    print("Enter marks 5")
    a5=int(input())
    print("Enter marks 6")
    a6=int(input())
    Result=Result(name,roll,a1,a2,a3,a4,a5,a6)
    Result.stu_info()
    Result.marks_info()
    print("Total Marks is:",Result.f_result())