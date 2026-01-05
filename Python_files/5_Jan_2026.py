
#Arithmetic
a,b=10,3; print(f"Addition:{a+b}"); print(f"Subtraction:{a-b}"); print("Multiplication:", a*b); print("Division:", a/b); print("Modulus:", a%b); print("Exponential:", a**b); print("Float division :",a//b)
print()

#assignment operator
a=10; a+=5;print(f"The values of a and b are:{a}&{b}"); print("Addition Assignment (a+=5): The value of a is now", a); a-=5; print("Subtraction Assignment (a-=5): The value of a is now", a); a*=5; print("Multiplication Assignment (a*=5): The value of a is now", a); a/=5; print("Division Assignment (a/=5): The value of a is now", a); a%=5; print("Modulus Assignment (a%=5): The value of a is now", a); a//=5; print("Floor Division Assignment (a//=5): The value of a is now", a); a**=5; print("Exponentiation Assignment (a**=5): The value of a is now", a)
print()

#Comparision operator
a,b=1,2;print(f"The values of a and b are:{a}&{b}"); print("Equal To (a == b):", a==b); print("Not Equal To (a != b):", a!=b); print("Greater Than (a > b):", a>b); print("Less Than (a < b):", a<b); print("Greater Than or Equal To (a >= b):", a>=b); print("Less Than or Equal To (a <= b):", a<=b)
print()

#Logical operators
#logical And
print("Logical AND:")
#case 1
a = 10
b = 20
if a < b and b > 15:
    print("Case 1: Both conditions are True\n")
else:
    print("Case 1: False")
#case 2
a = 5
b = 2
if a > 2 and b > 5:
    print("Case 2: True")
else:
    print("Case 2: False\n")
#case 3
x = 3
y = 10
if x > 5 and y == 10:
    print("Case 3: True")
else:
    print("Case 3: False\n")
#case 4
p = 8
q = 2
if p < 5 and q > 10:
    print("Case 4: True")
else:
    print("Case 4: False\n")


print("Logical OR:")
#Logocal OR
#case 1
a = 10
b = 20
if a < b or b > 15:
    print("Case 1: Both conditions are True\n")
else:
    print("Case 1: False")

#case 2
x = 5
y = 2
if x > 2 or y > 10:
    print("Case 2: One condition is True\n")
else:
    print("Case 2: False")

#case 3
p = 3
q = 15
if p > 10 or q > 10:
    print("Case 3: One condition is True\n")
else:
    print("Case 3: False")

#case 4
m = 4
n = 2
if m > 10 or n > 10:
    print("Case 4: True")
else:
    print("Case 4:Both conditions are False\n")


#Logical Not
print("Logical NOT")

print(not (5<2))
print(not ((5>2) and (10>5)))
print(not ((5<2) and (10<5)))
print(not( (5<10) and (5>10)))
print()

#Identity operator
#checks the memory location
a=[1,2]
b=[1,2]
a=b
print(a is b)
print(a is not b)

a=(1,2)
b=(1,2)
print(a is b)
print(a is not b)


#Membership operator


for i in range(1,31):
    if i % 3 == 0:
        print(i)

users = ["Mohan", "Keerthi", "Raju", "Pavani"]
for i in users:
    print(f"Hello ,{i}")

stu_marks= list(map(int, input().split()))
count_1 =0
count_2=0
pass_stu=[]
fail_stu=[]
for num in stu_marks:
    if num>=70:
        count_1+=1
    elif num< 70:
        count_2+=1
pass_stu.append(count_1)
fail_stu.append(count_2)
print("the no of students passed was :",*pass_stu)
print("the no of students failed was :",*fail_stu)
