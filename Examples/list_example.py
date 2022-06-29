# FIND:
# Number of elements in list
# Elements in index 0 and index 12
# Create new list as a ["M","A","C","H","I","N","E"]
# Delete element in index 5
# Add a new element
# Add element which you delete in index 5

lst=["M","A","C","H","I","N","E","L","E","A","R","N","I","N","G"]
print(len(lst))
print(lst[0])
print(lst[12])

new_list=[]
new_list.append(lst[0:7])
print(new_list)

lst.pop(5)
print(lst)

lst.extend("HMY")
print(lst)

lst.insert(5,"N")
print(lst)
