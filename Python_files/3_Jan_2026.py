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


#list
my_list = [1, 2, 3, 69, "Mohan", "raju", "rama", 6]
my_list.insert(3,6)
print(my_list)
print(type(my_list))

#tuple
tp = (1,2,69)
print(type(tp))

#set
sets = {1,2,3,4,69}
print(type(sets))

#frozen set
fro_set = frozenset(sets)
print(type(fro_set))

#Dictionary
My_info = {
    "Name": "Kucharlapati Hari RamMohan Raju",
    "Register number": "23B21A4540",
    "Mobile Number": "9392549789",
    "Branch":"AID",
    "Date of Birth":"27-09-2005",
    "age":20
}
print(type(My_info))
print(My_info)
print("my age is :",My_info["age"])

