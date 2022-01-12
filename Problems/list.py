my_list = [34,82.6,"Darth Vader" , 17 , "Hannibal"]

#my_tuple = (34, "Hannibal", 5)   Convert the list into tuple and print first last index of list and the length

e = []
e.append(my_list[0])
e.append(my_list[4])
e.append(len(my_list))
#print(e)
my_tuple = tuple(e)
print(my_tuple)

# alternate way

tuple = (my_list[0] , my_list[len(my_list)-1],len(my_list))
print(tuple)
#print(my_list)