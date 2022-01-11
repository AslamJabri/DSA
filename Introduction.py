_list = ["hello" , "World" , 2022 , "Python"]
print(_list[0]) # hello
print(len(_list)) # length of the list

print(_list[2])
_list[2] += 3
print(_list[2])

#Extending the list either by + or using extend

num_seq = range(0,10)
num_list = list(num_seq)
print(num_list)
_list.extend(num_list)
print(_list)

#Common List Opertions:
#Adding an Element into the list
num1 = []
num1.append(1)
num1.append(2)
print(num1)

#Insert and Element into list
num1.insert(1 , 4)
print(num1)

#Removing the Last Element
_list.pop()
print(_list)

# Removing the specific element
_list.remove(2025)
print(_list)

# List Slicing
print(_list[0:7])
print(_list[0::2])

# Index Search
print(_list.index("Python"))
#Can also be used with in and not in
print("hello" in _list)
print("Javascript" not in _list)

#Sorting the list
num2 = [10,54,34,97,33,56,78,77]
num2.sort()
print(num2)