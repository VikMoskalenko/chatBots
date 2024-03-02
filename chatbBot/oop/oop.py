class Person:
    name = 'Ivan'
    age = 10
    
    def __init__(self,  name, age):
        self.name = name
        self.age = age
        
    def set(self, name, age):
        self.name = name
        self.age = age
        
class Student (Person):
    course = 1
    def set(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

igor = Student("Ihor", 19)
#igor._set('Igor', 19)
igor.set("Igor", 23, 5)

print("name", igor.name, ", age : ", igor.age, ", course : ", igor.course)
    
vlad = Person("Vlad", 33)
#vlad._set("Vlad", 25)
print(vlad.name + ' ' + str(vlad.age))

ivan = Person("Ivan", 23)
#ivan._set('Ivan', 33)
print(ivan.name + ' ' + str(ivan.age) )

