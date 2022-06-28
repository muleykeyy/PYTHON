####################################### QUESTION #######################################

# Write divide_students function.
# If index is even take students in a different list
# If index is odd take students in an another different list
# Return this two list in a list.

students=["Ayşe","Ali","Veli","Fatma","Sudem","Berkay"]

def divide_students(students):
    groups = [[], []]
    for index,students in enumerate(students):
        if index % 2 == 0:
            groups[0].append(students)
        else:
            groups[1].append(students)

    print(groups)
    return groups

st=divide_students(students)