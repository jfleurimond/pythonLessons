#this one i like your scirpts with argv
#after defining the function anything indented 4 lines after it is attached
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")


#ok that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#this just takes one argument

def print_one(arg1):
    print(f"arg1: {arg1}")

#this one takes no arguments
def print_none():
    print("I got nothin")

print_two("Zed", "Shaw")
print_two_again("Zed", "shaw")
print_one("First")
print_none()

#random test to see if I can write to a file in one try. Plot-twist it works :)
# test = open("./textOpen.txt", 'w').write("Writing to the file in one line")