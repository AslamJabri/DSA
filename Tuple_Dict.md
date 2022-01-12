A tuple is a very similar to a list, except for the fact that its contents cannot be changed. A TUPLE IS IMMUTABLE.
However it contains mutable elements like a list.These elements can be altered.
The contents are enclosed in () in tuple.
We can do  Merge ,Search,Nested,Index functions in tuples.
Since tuples are immutable we can't add or delete element from them.Furthermore ,it isn't possible to append another tuple to an existing tuple.



# Dictionary
When we think of dictionary ,the image pops up is about a vast book containing words and their meainings.
Just like that dictionary is a data which has key : value
    $ Syntax {key:value}
A dictionary stores key-value pairs where each unique key is an index which holds the value associated with it
Dictionaries are unordered because the entries are not stored in a linear structure.

# The dict() Constructor#
As the name suggests, the dict() constructor can be used to construct a dictionary. Don’t worry about the term “constructor” for now. Think of it as an operation which gives us a dictionary.
If our keys are simple strings without special characters, we can create entries in the constructor. In that case, values will be assigned to keys using the = operator.
A popular practice is to create an empty dictionary and add entries later.

# Accessing Values
For many, this is where a dictionary has an edge over a list or a tuple. Since there are no linear indices, we do not need to keep track of where values are stored.

Instead, we can access a value by enclosing its key in square brackets, []. This is more meaningful than the integer indices we use for tuples and lists.

Alternatively, we can use the get() method as follows:

# Dictionary Comprehension #

Python also supports dictionary comprehensions, which work very similar to list comprehensions. We’ll be creating new key-value pairs based on an existing dictionary.

However, to iterate the dictionary, we’ll use the dict.items() operation which turns a dictionary into a list of (key, value) tuples.

Here’s a simple example where the keys of the original dictionary are squared and '!' is appended to each string value:


# SETS

A set is an unordered collection of data items.
Mutable data structures like lists or dictionaries can’t be added to a set. However, adding a tuple is perfectly fine.
One might wonder, “Why would I need a set?”
Well, a set is perfect when we simply need to keep track of the existence of items.
It doesn’t allow duplicates, which means that we can convert another data structure to a set to remove any duplicates.

# Creating  a SET
The content of a set are encapsulated in curly braces {}. 
A set() constructor is used for creating a set alternately.

# SET theory operation
In Python, union can be performed using either the pipe operator, |, or the union() method:
    set_A = {1, 2, 3, 4}
    set_B = {'a', 'b', 'c', 'd'}

    print(set_A | set_B)
    print(set_A.union(set_B))
    print(set_B.union(set_A))

    Output:
    {1, 2, 3, 4, 'd', 'b', 'c', 'a'}
    {1, 2, 3, 4, 'd', 'b', 'c', 'a'}
    {1, 2, 3, 4, 'd', 'b', 'c', 'a'}

In Python, intersection can be performed using either the & operator or the intersection() method:

    set_A = {1, 2, 3, 4}
    set_B = {2, 8, 4, 16}

    print(set_A & set_B)
    print(set_A.intersection(set_B))
    print(set_B.intersection(set_A))

    Output:
    {2, 4}
    {2, 4}
    {2, 4}

# Difference
In Python, the difference between two sets can be found using either the - operator or the difference() method.
Do keep in mind that the difference operation is not associative, i.e., the positions of the sets matter.
set_A - set_B returns the elements which are only present in set_A.
set_B - set_A would do the opposite.
    set_A = {1, 2, 3, 4}
    set_B = {2, 8, 4, 16}

    print(set_A - set_B)
    print(set_A.difference(set_B))
    print(set_B - set_A)
    print(set_B.difference(set_A))

    Output:
    {1,3}
    {1,3}
    {16,8}
    {16,8}