
#SCOPE
#it refers to the region of the code where a variable is defined and accessible.

#global scope-works outside the function

x=10 #global scope
def greet():
    print("inside",x)
    
greet()
print("outside",x)
#inside 10
#outside 10


x=10 #global scope
def greet():
    #x+=20
    print("inside",x)    
greet()
x+=100
print("outside",x)
#inside 10
#outside 110

#local scope-inside the function
x=10
def greet():
    x=12 #local scope
    print("inside",x)
greet()
print("outside",x)
#inside 12
#outside 10


#global keyword
x=15
def greet2():
    global x #keyword
    x+=5
    print("inside",x)
greet2()
print("outside",x)
#inside 20
#outside 20


#RECURSION
#recursion is a programming technique where a function calls itself in order to solve a program 
num=int(input("enter a number:"))
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)



def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1) #recursive call
print(factorial(5))


