#script that also accepts arguments

# import is how we add features to our script, which are really called modules
from sys import argv
# read the WYSS section for how to run this

#tells command to take the arguments and save it in the variables below
script, first, second, third = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)
