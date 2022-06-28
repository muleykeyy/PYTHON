########################################## LAMBDA ############################################

def sum(a,b):
    return a+b

sum(9,6)

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

add= lambda a,b:a+b
add(9,6)

########################################## MAP #########################################

# Dont need for

# Executes a specified function for each item in an iterable. The item is sent to the function as a parameter.

salaries=[6000,4000,8000,9000]
def salary(x):
    return x * 20 /100 + x

salary(5000)

for s in salaries:
    print(salary(s))

list(map(salary,salaries))
list(map(lambda x:x*20/100+x,salaries))

############################################ FILTER #################################################

# Dont need if

list_store=[1,2,3,4,5,6,7,8,9,10]

list(filter(lambda x: x%2 ==0,list_store))

############################################# REDUCE ############################

from functools import reduce

lists=[1,5,9]
reduce(lambda j,k:j+k,lists)