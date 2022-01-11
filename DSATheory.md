## DSA definition:
    A data structure is a way of storing data and organizing data according to a certain format or structure.
    There are so many lists online about all sorts of topics. Another example is the use of tables to display schedules. A novel stores and organizes text in paragraphs.
All these mediums store data and allow us to manipulate or access it in a certain way.
Data structures are a crucial part of computer programming. Since we frequently deal with data manipulation, it is of paramount importance to organize it in an efficient and meaningful way.

## Data Structures In PYTHON:
    Python is equipped with several built in data structures to help us efficiently handle large amounts of data.
    The four primary data built in structures offered in python 3 are:
    List
    Tuple
    Dictionary
    Set


## LIST
The list is perhaps the most commonly used data structure in Python.It allows us to store elements of different data types in one container.
The content of a list are enclosed by square brackets,[].

    list = ["Winterfell","jon snow",30]
    print (list[0]) #Output: Winterfell -- Indexing
    print(len(list)) #Output: 3 -- length of the list

The beauty of list lies in fact that we are not bound to one type of data.
Lists are mutable ,which further expands their functionality
    print(list[2]) # Output : 30
    list[2] += 3
    print(list[2]) # Output : 33

# Using Range
A range can further be converted into a list by using the list() casting.
    num_seq = range(0,10)    # sequence o to 9
    num_list = list(num_seq)
    print(num_list)  # Output : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   $syntax- range(start , stop , step)

# Sequential Indexing
To access the elements of a list or a string which exists inside another list, we can use the concepy of sequential indexing.
    world_cup_winners = [[2006, "Italy"], [2010, "Spain"],
                     [2014, "Germany"], [2018, "France"]]
    print(world_cup_winners[1])   #Output:  [2010, 'Spain']
    print(world_cup_winners[1][1])  # Output: Accessing 'Spain'
    print(world_cup_winners[1][1][0])  # Output: Accessing 'S'


# Merging List
Python makes it really easy to merge lists together. The simplest way is to us '+' operator
    part_A = [1, 2, 3, 4, 5]
    part_B = [6, 7, 8, 9, 10]
    merged_list = part_A + part_B
    print(merged_list) # Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Alternatively you can also use extend() property of a list to add the elements of one list at the end of another.
    part_A.extend(part_B)
    print(part_A)  #Output : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]