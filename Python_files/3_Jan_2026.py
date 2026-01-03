marks = int(input("Enter Your marks:  "))
if marks <= 100 and marks >=90:
    print("Grade A")
elif marks >80 and marks<89:
    print("Grade B")
elif marks >70 and marks<80:
    print("Grade C")
else:
    print("Fail")
