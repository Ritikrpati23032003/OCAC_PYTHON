#FUNCTION
# def calculateGmean(a,b):
#     mean=(a*b)/(a+b)
#     print(mean)
# def calculateAdd(a,b):
#     add=a+b
#     print(add)
# def isGreater(a,b):
#     if(a>b):
#         print("First number is greater")
#     else:
#         print("Second nuber is greater")
# a=4
# b=5
# calculateGmean(a,b)
# calculateAdd(a,b)
# isGreater(a,b)
# c=10
# d=3
# calculateGmean(c,d)
# calculateAdd(c,d)
# isGreater(c,d)
# Calling function
# def name(fname,lname):
#     print("Hello",fname,lname)
# name("Ritik","Pati")
# FUNCTION ARGUMENTS
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        print(sum/len(numbers))
#average(5,6)
average(5,6,7,1)
