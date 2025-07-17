def add(num1,num2):
    return num1+num2

def subtract(num1,num2):
    return num1-num2

def multiply(num1,num2):
    return num1*num2

def divide(num1,num2):
    return num1/num2

def power(num1,num2):
    return num1**num2

x=input("What operation? (+, -, *, /,^) ")
if x=="+":
    num1=int(input("What is the first number? "))
    num2=int(input("What do you want to add to " + str(num1) + "? "))
    print(add(num1,num2))
if x=="-":
    num1=int(input("What is the first number? "))
    num2=int(input("What do you want to subtract " + str(num1) + " by? "))
    print(subtract(num1,num2))
if x=="*":
    num1=int(input("What is the first number? "))
    num2=int(input("What do you want to multiply " + str(num1) + " by? "))
    print(multiply(num1,num2))
if x=="/":
    num1=int(input("What is the first number? "))
    num2=int(input("What do you want to divide " + str(num1) + " by? "))
    print(divide(num1,num2))
if x=="^":
    num1=int(input("What is the first number? "))
    num2=int(input(str(num1)+" to the power of _? "))
    print(power(num1,num2))
    