################# QUESTION: #################

# Write the code for string: If index is odd then letter is lower case, if index is even then letter is upper case.
#  input: "hello i am try to learn python"
#  output: "HeLlO I Am tRy tO LeArN PyThOn"

a="hello i am try to learn python"

def answer(string):
    new_a=""

    for index in range(len(string)):
        if index % 2 == 0:
            new_a +=string[index].upper()
        else:
            new_a += string[index].lower()
    print(new_a)

answer(a)

################################################# OR ########################################

def second_answer(s):
    a_new=""
    for i, letter in enumerate(s):
        if i%2 == 0:
            a_new+=letter.upper()
        else:
            a_new+=letter.lower()
    print(a_new)

second_answer("hello it is hilal müleyke")

