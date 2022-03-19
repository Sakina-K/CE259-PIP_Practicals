#20CE046 SAKINA KUTERWADLI
#PRACTICAL 8
#AIM: Write a Program in Python to implement a Stack Data Structure 
#using Class and Objects, with push, pop, and traversal method.
##github repository link: https://github.com/Sakina-K/CE259-PIP_Practicals.git

class Stack:
    def __init__(self):
        self.stelement=[]
        top=None
        ### here we use a list to form a stack which have predefined functions like append and pop
    ##push
    def push(self,element):
        self.stelement.append(element)
        print('pushed')
        

    ##pop function
    def pop(self):
        print("Element popped:")
        return self.stelement.pop()
    
    def traversal(self):
        for i in self.stelement:
            print(i)




########creating an object of a class Stack
st1= Stack()
print("Push Operation")
st1.push(1)
st1.push(3)
st1.push(5)

print("Display")
st1.traversal()
####pop
print("POP operation")
print(st1.pop())
print(st1.pop())
print("Display")
st1.traversal()