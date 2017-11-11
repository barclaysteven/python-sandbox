# Basic string functions
my_str = "steven"
print("Starting string: " + my_str)
print("Using capitalize function: " + my_str.capitalize())
print("Reversing the string: " + "".join(reversed(my_str)))
print("Using upper function: " + my_str.upper())
print("Using the split function on 'e': " + str(my_str.split("e")))

# Dealing with multi word strings
sentence = "Shay loves Beauty and the Beast"
print("Starting Sentence: " + sentence)
print("Using replace function: " + sentence.replace("loves", "is crazy about"))

# String formatting
name = "Lexi"
loc = "Festro"
print("Hello, my name is {}, and I'm from {}".format(name, loc))


