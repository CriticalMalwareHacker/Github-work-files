class Person:
    def __init__(self,name,age,profession):#__init__ it is like a constructor
        
        self.name=name
        self.age=age
        self.profession=profession
    def show(self): #it is called a method not a function
        print("Name:",self.name," Age:",self.age," Profession:",self.profession)
    def work(self):
        print(self.name," working as a ",self.profession)
#object
Tanay=Person('Tanay',18,"Engineer")
Tanay.show()#calling the function from the class person
Tanay.work()

#object 2 user input
name1=input("Enter your name: ")
age1=input("Enter your age")
profession1=input("Enter your profession")
person2=Person(name1,age1,profession1)
person2.show()
person2.work()