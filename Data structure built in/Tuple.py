# creating a tuple
tup1 = ("Ford","BMW" , 2022 , "Black")
print(tup1)
print(len(tup1))
print(tup1[1])
print(tup1[2:])


#Dictionary

phonebook = {"Batman":"Gotham City","Spiderman":"New York" , "Iron-Man":"Stark Company"}
print(phonebook)

#Using a dict Constructor
phone_book = dict(Batman=468426, Cersei=237734, Ghostbusters=44678)
# Keys will automatically be converted to strings
print(phone_book)

# Alternative approach
phone_book = dict([('Batman', 468426),
                   ('Cersei', 237734),
                   ('Ghostbusters', 44678)])
print(phone_book)


#Accessing Values

print(phonebook["Batman"])
print(phonebook.get("Spiderman"))

phone_book["Godzilla"] = 445566  #Adding a New Entry
print(phone_book)
phone_book["Godzilla"] = 12312312   # Updating a Entry

phone_book = {"Batman": 468426,
              "Cersei": 237734,
              "Ghostbusters": 44678}
print(phone_book)

cersei = phone_book.pop("Cersei")
print(phone_book)
print(cersei)

# Removes and returns the last inserted pair, as a tuple
# In Python versions before 3.7, popitem() removes and returns the random item
lastAdded = phone_book.popitem()
print(lastAdded)


print(len(phone_book)) # length of the dictionary

print("Batman" in phone_book)  # checking key existence boolean
print("Godzilla" in phone_book)

second_phone_book = {"Catwoman": 67423, "Jaime": 237734, "Godzilla": 37623}

# Add secondphone_book to phone_book
phone_book.update(second_phone_book)
print(phone_book)

#Dictionary Comprehension

houses = {1: "Gryffindor", 2: "Slytherin", 3: "Hufflepuff", 4: "Ravenclaw"}
new_houses = {n**3: house + "!" for (n, house) in houses.items()}
print(houses)
print(new_houses)