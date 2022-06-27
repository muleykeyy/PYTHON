##############################################
# STRINGS
##############################################

name="müleyke"

# OR

#name='müleyke'

# Multiline Strings:

long_str= """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


# Access Elements of the String:
name[0]
name[3]

# Slice:
name[0:4] # 0 is included but 4 is not included

long_str[5:12]

"Sed" in long_str # Output : False cause case Python is case sensitive

"sed" in long_str # Now its True


#################################  STRING METHODS ##################################

# To see methods:
dir(str)


# len : Function. Gives size of string.
len(name)
len("python")
type(len)

############################ Method VS Function #########################################
# Methods are associated with the objects of the class they belong to.
# Functions are not associated with any object.
# We can invoke a function just by its name.

# upper() & lower() : Upper - Lower Case conversion.

name.isupper() # Bool

name.upper() # convert upper case
"PYTHON".lower() # convert lower case

# type(upper()) # Gives ERROR! Cause its a METHOD!

# replace() : Returns a string where a specified value is replaced with a specified value
name.replace("e","a")

# split(): Splits the string at the specified separator, and returns a list

"Hilal Müleyke Yüksel".split()
name.split("e")

# capialize(): Converts the first character to upper case
name.capitalize()

# center(): Will center align the string, using a specified character (space is default) as the fill character.
name.center(15,"*")

# count(): Returns the number of times a specified value occurs in a string
txt="I love drive fast as fast i can!"
txt.count("fast")

# find(): Searches the string for a specified value and returns the position of where it was found
txt.find("love")

# title(): Converts the first character of each word to upper case
txt.title()