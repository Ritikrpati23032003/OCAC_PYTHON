# #Creating class:-
# class Student:
#     name='Ritik'

# # creating obj:-
# s1=Student()
# print(s1.name)                #Ritik

#1.Constructor (__init__):-

# default constructor:
# class Student:
#     def __init__(self):
#         print("Something")
# s1=Student()                  # Something

# Parameterized onstructor:
# class Student:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
# s1=Student('Riitk', 21, 80)
# s2=Student('chiku', 20, 30)
# print(s1.name, s1.age, s1.weight)
# print(s2.name, s2.age, s2.weight)

#2.Class and Instace atrribute:-

# class Student:
#     College_name="GIFT"                       #Class arttr
#     def __init__(self, name, age, weight):
#         self.name = name                      #instace attr
#         self.age = age
#         self.weight = weight
# s1=Student('Riitk', 21, 80)
# s2=Student('chiku', 20, 30)
# print(s1.name, s1.age, s1.weight)
# print(s2.name, s2.age, s2.weight)
# print(Student.College_name)

#3.Metods:-

# class Student:
#     def __init__(self,name,age): #constructor
#         self.name=name
#         self.age=age
#     def welcome(self):  #method
#         print('Welcome student',self.name)
#     def get_age(self):
#         return self.age
# s1=Student('Aman',32)
# s1.welcome()
# print(s1.get_age())

#Example:=

# class Student:
#     def __int__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi",self.name,"ur avg score is",sum/3)
# s1=Student('Ritik',[32,35,65])
# s1.get_avg()


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_avg(self):
#         total_marks = sum(self.marks)
#         average_score = total_marks / len(self.marks)
#         print(f"Hi {self.name}, your average score is {average_score}")

# # Create an instance of the Student class
# s1 = Student('Ritik', [32, 35, 65])


# # Call the get_avg method to calculate and print the average marks
# s1.get_avg()
# s1.name="Chiku"
# s1.get_avg()


#4.Static mehod:-

# class Student:
#     @staticmethod
#     def college():
#         print("Gift")

#5.Abstraction:-

# class car:
#     def __init__(self):
#         self.acc=False
#         self.acc=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("Car Strated...")
# car1=car()
# car1.start()  
      
#EXample:-create acc. having two attr debit and credit and print balance
# class Account:
#     def __init__(self,bal,acc):
#         self.balance=bal
#         self.acc=acc
#     # Debit
#     def debit(self,amount):
#         self.balance -= amount
#         print("Rs.",amount,"was debited")
#         print("Total balance is",self.get_balance())
#     #Credit
#     def credit(self,amount):
#         self.balance += amount
#         print("Rs.",amount,"was credited")
#         print("Total balance is",self.get_balance())
#     def get_balance(self):
#         return self.balance
# acc1=Account(300000,132348)
# print("balance is",acc1.balance,"acc no.is",acc1.acc)
# acc1.debit(20000)
# acc1.debit(50000)
# acc1.debit(20000)
# acc1.debit(50000)
# acc1.credit(80000)
# acc1.credit(5000)

#6.INHERITANCE:-

# #Single Inheritance
# #parent class
# class car:
#     @staticmethod
#     def Start():
#         print("Car has started")
#     @staticmethod
#     def stop():
#         print("car has stopped")
# #Child class
# class Toyotacar(car):
#     def __init__(self,name):
#         self.name=name
# car1=Toyotacar("Fortuner")
# print(car1.name)          #Fortuner
# car1.Start()              #car has started
# car1.stop()               # car has stopped


#Multilevel Inheritance
# class car:
#     @staticmethod
#     def Start():
#         print("Car has started")
#     @staticmethod
#     def stop():
#         print("car has stopped")
# class Toyotacar(car):
#     def __init__(self,brand):
#         self.brand=brand
# class Fortuner(Toyotacar):
#     def __init__(self,type):
#         self.type=type
# car1=Fortuner("Disel")
# print(car1.type)
# car2=Toyotacar("Fortuner")
# print(car2.brand)
# car1.Start() 
# car1.stop() 

#Multiple Inheritance:-
# class A:
#     vara="A started"
# class B:
#     varb="B started"
# class C(A,B):
#     varc="C started"
# c=C()
# print(c.vara)
# print(c.varb)
# print(c.varc)

#SUPER() METHOD:-

# class car:
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#     @staticmethod
#     def start():
#         print("Car started")
#     @staticmethod
#     def stop():
#         print("Car stopprd")
# class Toyotacar(car):
#     def __init__(self,name,type):
#         super().__init__(name,type)      #Use of super()
#         #super().__init__(type)
#         super().start()                    #O/P:-car started
# car1=Toyotacar("TATA","Electric")
# print(car1.name,car1.type)                  #O/P:-TATA,Electric
# #car.start()

#CLASS METHOD:-
# class person:
#     name="Ritik"
#     #def changename(self,name):
#         #self.name=name
#         #person.name=name
#         #self.__class__.name="Rahul"
#     @classmethod
#     def changename(cls,name):
#         cls.name=name
# p1=person()
# p1.changename("Rahul")
# print(p1.name)
# print(person.name)

#PROPERTY METHOD:-
# class student:
#     def __init__(self,phy,chem,mth):
#         self.phy=phy
#         self.chem=chem
#         self.mth=mth
#     #     self.percentage=str((self.phy+self.chem+self.mth)/3)+"%"
#     # def percentage(self):
#     #      self.percentage=str((self.phy+self.chem+self.mth)/3)+"%"
#     @property
#     def percentage(self):
#         return str((self.phy+self.chem+self.mth)/3)+"%"

# s1=student(63,65,63)
# print(s1.percentage)
# s1.phy=95
# print(s1.percentage)

#7.POLYMORPHISM:-
# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
#     def shownum(self):
#         print(self.real,"i+",self.img,"j")
    
#     # def add(self,c2):
#     #     newReal=self.real+c2.real
#     #     nweImg=self.img+c2.img
#     #     return complex(newReal,nweImg)

#     #OR Dunder function
#     def __add__(self,c2):
#         newReal=self.real+c2.real
#         nweImg=self.img+c2.img
#         return complex(newReal,nweImg)
#     def __sub__(self,c2):
#         newReal=self.real-c2.real
#         nweImg=self.img-c2.img
#         return complex(newReal,nweImg)

# c1=complex(5,2)
# c1.shownum()
# c2=complex(3,1)
# c2.shownum()
# #c3=c1.add(c2)
# c3=c1+c2
# c3.shownum()
# c3=c1-c2
# c3.shownum()

##Example:1-
# class circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return (22/7)*self.r**2
#     def perimeter(self):
#         return 2*(22/7)*self.r
# c1=circle(21) 
# print(c1.area())
# print(c1.perimeter())     
##Example:2-
# class Emp:
#     def __init__(self,role,dept,sal):
#         self.role=role
#         self.dept=dept
#         self.sal=sal   
#     def showdetails(self):
#         print("Role is",self.role)
#         print("Dept",self.dept)
#         print("Salatry",self.sal)
# class Engineer(Emp):
#     def __init__(self,name,age):
#         super().__init__("Accoutant","Finance","75000")
#         self.name=name
#         self.age=age
# s1=Engineer("Ritk",40)
# print("Name is",s1.name)
# print("Age is",s1.age)
# s1.showdetails()

# #Example 3:-
# class order:
#     def __init__(self,item,price):
#         self.item=item
#         self.price=price
#     def __gt__(self,odr2):
#         return self.price>odr2.price
# odr1=order("Chips",10)
# odr2=order("mixture",20)
# print(odr1>odr2)            #True/False



class ATM:
    def __init__(self,balance,acc):
        self.balance=balance
        self .acc=acc
    def debit(self,amount):
        self.balance-=amount
        print("debit",amount)
        print('after debit',self.balance)
    def credit(self,amount):
        self.balance+=amount
        print("credit",amount)
        print('after credit',self.balance)
    # def get_balance(self):
    #     print( self.balance)
acc1=ATM(1000,12345)
print(acc1.balance)
print(acc1.acc)
acc1.debit(500)
acc1.credit(1500)



