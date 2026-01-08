
#functions
def house(paint,brush):
    print(f"my painter is painting {paint} color using {brush} brushes to my House")
house("Blue",4)

#By using print statement in our block of code
def add():
    a = 5
    b = 3
    print(a+b)
add()

#By using return in our block of code
def add():
    a = 5
    b = 3
    return a+b
print(add())

#By using default parameters
def add(a=5,b=3):
    return a+b
print(add())

#By using with parameters
def add(a,b):
    print(a+b)
add(5,3)

words = ["apple", "banana", "cherry"]
first_letters = [w[0] for w in words]
print(first_letters)

#To print the second smallest and largest elements in a list
lis=[60,75,81,100,100]
maxi=0
smalli=0
for i in lis:
    if i >maxi:
        smalli = maxi
        maxi=i
    elif(i>smalli and i!=maxi):
        smalli=i

print(f"List of elements are : {lis}")
print(f"the second largest element is :{smalli}")
print(f"the  largest element is :{maxi}")