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
