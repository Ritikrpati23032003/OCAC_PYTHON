# Function to add two numbers
def add(a,b):
    return a+b
# Function to Substract two numbers
def substract(a,b):
    return a-b
# Function to Multiply two numbers
def multiply(a,b):
    return a*b
# Function to Divided two numbers
def division(a,b):
    if b==0:
        return "Can not divided by zero"
    else:
        return a/b
# Main function to run the calculator
def calculator():
    print("Select Operation")
    print("1.Add")
    print("2.Substract")
    print("3.Multiply")
    print("4.Division")
    choice=input("Enter choice 1/2/3/4\n")
    num1=float(input("Enter first number: "))
    num2=float(input("Enter Second number: "))
    match choice:
        case choice if choice=='1':
             print(num1,"+",num2,"=",add(num1,num2))
        case choice if choice=='2':
             print(num1,"-",num2,"=",substract(num1,num2))
        case choice if choice=='3':
             print(num1,"*",num2,"=",multiply(num1,num2))
        case choice if choice=='4':
             print(num1,"/",num2,"=",division(num1,num2))
        case _:
             print("Not vallid")
calculator()          # Run the calculator

