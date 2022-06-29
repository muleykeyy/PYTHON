# Write a code for:
# Capitalize all letters of given string.
# Put space instead of comma
# Separate sentence word by word

# input: "I will learn Python, then i start to learn machine learning"
# output: ["I","WILL","LEARN" ...]

text= "I will learn Python, then i start to learn machine learning"

text=text.upper()
text=text.replace(",","")
text=text.split(" ")
print(text)

