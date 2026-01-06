
for i in range(1,6):
    print("*" * i)

for i in range(1,6):
    for j in range(i):
        print("*",end ="")
    print()

for i in range(6,0,-1):
    print("*" * i)

#cubes of the list elements
l_cubes = [1,3,5,7,9]
i = 0
while i < len(l_cubes):
    print(l_cubes[i]**3)
    i+=1

#printing the odd numbers in a list
my_list =[1,2,3,4,5,11,6,9]
i = 0
while i <len(my_list):
    if my_list[i]%2!=0:
        print(my_list[i])
    i+=1

#print double of all numbers in a list
my_list =[1,2,3,4,5,6]
i = 0
while i < len(my_list):
    print(my_list[i]*2)
    i+=1

n=6
for i in range(1,n+1):
    print(" " *(n-i) + "*" *(2*i-1))
n=6
for i in range(n,0,-1):
    print(" " *(n-i) + "*" *(2*i-1))


i = 1
while i<4:
    j = 1
    while j<4:
        print(i,j)
        j+=1
    i+=1