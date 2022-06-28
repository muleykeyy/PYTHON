################################### QUESTION ###########################
# Create a dictionary with random numbers.
# Find square of even numbers
# Keys are NOT change, only values will change
# Add dictionary

############################## Classical Solution ######################
numbers=range(10)
dict={}

for n in numbers:
    if n % 2 == 0:
        dict[n]=n**2

############################# Solution with Dictionary Comperehensions ###############################
{n:n**2 for n in numbers if n%2==0}