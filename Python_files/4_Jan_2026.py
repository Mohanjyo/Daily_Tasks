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
