##############################################################

# LISTS

# List items are ordered, changeable, and allow duplicate values.
#############################################################

numbers=[1,2,3,4]
type(numbers)
chars=["h","m","y"]

mixed=[1,2,3,"h","m",True,[3,5,7]]
mixed[3]
mixed[6]
mixed[6][2] # list in list. First go list and select the element you want.

mixed[0:5] # 0 is include 5 is not include

dir(numbers) # To see all methods.

######################################## LIST METHODS #####################################

# len()
len(numbers)

# append(): Adds an element at the end of the list
numbers.append("hilal")
print(numbers)

# clear(): Removes all the elements from the list
a=[1,2,3,4,5]
a.clear()
print(a)

# copy(): Returns a copy of the list
n=numbers.copy()
print(n)

# count(): Returns the number of elements with the specified value
numbers.count("hilal")

# extend(): Add the elements of a list (or any iterable), to the end of the current list
numbers.extend(chars)
print(numbers)

# index(): Returns the index of the first element with the specified value
numbers.index("m")

# insert(): Adds an element at the specified position
numbers.insert(2,"müleyke")
print(numbers)

# pop(): Removes the element at the specified position
numbers.pop(5)
print(numbers)

# remove(): Removes the item with the specified value
numbers.remove("y")
print(numbers)

# reverse(): Reverses the order of the list
name=["veli","ali","kadir"]
name.reverse()
print(name)

# sort(): Sort the list
name.sort()
print(name)  # Sort alphabetically

l=[8,9,1,0,7,6,51]
l.sort()
print(l)  # Sort numerically