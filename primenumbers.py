import math
# while True:
#     num=int(input("Choose a number: "))


def isprime(number):
    if number==1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    else:
        for i in range(3,int(math.sqrt(number))+1,2):
            if number % i == 0:
                return False
        return True
        
#     x=0
#     i=2
#     while x!=num:
#         if isprime(i)==True:
#             x+=1
#         if x==num:
#             print(i)
#         i+=1

length=int(input("Prime numbers up to __: "))
list=[]
listt=[]
trueorfalse=[]
for i in range(2,length+1):
    list.append(i)
    trueorfalse.append(True)
print("Finding primes... ")

def delete(n):
    for i in range(n-2+n,len(list),n):
        trueorfalse[i]=False
for i in range(len(list)):
    if trueorfalse[i]==True:
        delete(list[i])
for i in range(len(trueorfalse)):
    if trueorfalse[i]==True:
        listt.append(list[i])
        
print("Your prime numbers are: ",end="")
print(listt)

