######################################

# FUNCTIONS

#######################################
list_store=[]
def adding_element(a,b):
    """
        Takes two number a and b.
        Multiple this numbers
        And add results to a list

    """
    c=a*b
    list_store.append(c)
    print(list_store)

adding_element(10,3)
adding_element(25,5)
adding_element(41,2)

######################################### DEFAULT PARAMETERS/ARGUMENTS ######################

def divide(h,m):
    print(h/m)

divide(5,2)
############################
def divide(k=5,l=2):
    print(k/l)

divide()

# In this example we use default parameters. pi not change its always same!
def area(pi=3.14159,radius=4):
    a=radius**2*pi
    print("The area of circle is : ",a)

area()

########################### Return #########################
def calculate(varm,moisture,charge):
    return (varm + moisture)/charge

g=calculate(78,23,18)*10
print(g)

########## Calling a Function#################################

def standard(i, j):
    return i * 10/100*j*j

def all_functions(varm,moisture,charge,j,i):
    y=calculate(varm,moisture,charge)
    z=standard(i,j)
    print(i*10)

all_functions(3,2,7,20,7)

###################################### LOCAL & GLOBAL VARIABLES ################################################


list_store2=[1,2]  #global

def add_element(d,e):
    g=d*e #local: we can not see in global
    list_store2.append(g)
    print(list_store2)

add_element(5,3)



