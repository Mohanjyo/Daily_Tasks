# using if, elif and else statements to grade students based on their marks

marks = int(input("Enter Your marks:  "))
if marks <= 100 and marks >=90:
    print("Grade A")
elif marks >80 and marks<89:
    print("Grade B")
elif marks >70 and marks<80:
    print("Grade C")
elif marks >60 and marks<70:
    print("Grade D")
elif marks >50 and marks<60:
    print("Grade E")
elif marks <50:
    print("Grade F")  
else:
    print("Invalid Marks")
      
#Input & Output Functions

My_name = input("Enter your name:  ")
print("Hello "  + My_name +"!")
print()   
        
#Checking the type of the value
a = "Madam sir madam anthey"
print(type(a))

#int
b= 9392549789
print(type(b))

#float
c = 69.99
print(type(c))

#complex
d = 7+9j
print(type(d))

#Boolean
E = True
print(type(E))   