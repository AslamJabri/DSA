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


#List Comprehension
""" List Comprehension is a technique that uses a for loop and a condition to create a new list from an existing one. """
# A result is always a new list, so its a good practice to assign list comprehension to a new variable.

# Structure
'''A list comprehension statement is always enclosed in square brackets,[].
    [expression for loop if condition]      

  1.  The expression is an operation used to create elements in the new list.

  2.The for loop will iterate an existing list. The iterator will be used in the expression.

  3. New elements will only be added to the new list when the if condition is fulfilled. This component is optional.
'''
 #if we use a simple iteration 
numb = [1,2,3,4,5,6,7,8,9]
numb_doub = []
for i in numb:
    numb_doub.append(i * 2)

print(numb)
print(numb_doub)


#now lets convert to list comprehension

number = [1,3,5,7,9]
number_doub = [n * 2 for n in number]
print(number)
print(number_doub)


#Adding a Condition
numm = [10,20,30,40,50]
numm_doub = [i * 2 for i in numm if i % 4 == 0]#only divisible by 4 will be multiplied

print(numm)
print(numm_doub)

#using multiple lists
n1 = [1,2,3,4,15]
n2 = [7,8,19,5,6]
sum_n=[(i,j) for i in n1 for j in n2 if i+j > 15]
print(sum_n)