#########################################################

# DICTIONARY
# key - value pair.

########################################################

d = {"name": "Müleyke",
   "age":25,
   "title": "AI Engineer"}
d["age"]

cars = {"Audi": ["R8",2022],
        "Volvo":["XC90",2021],
        "Honda":["Civic",2016]}
cars["Audi"][0]

################################## KEY #####################################
"BMW" in cars
"Honda" in cars
cars.get("Audi")

# Change value:
cars["Honda"]=["Accord",2022]
cars

# Get all Keys: Returns list
cars.keys()
# Get all Values: Returns dictionary
cars.values()
# Get all Pairs: Returns a list containing a tuple for each key value pair
cars.items()

# Update values:
cars.update({"Audi":"RS7"})
cars

##################################################################################

# TUPLE
# A tuple is a collection which is ordered and unchangeable.
###################################################################################
t=("müleyke",25,1997)
t[1]

# If you want to change the element:
t=list(t)
t[1]=35
t=tuple(t)
