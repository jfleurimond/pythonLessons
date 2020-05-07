# basics of creating a function

def print_two(*args):
	arg1, arg2 = args 
	print(f"arg1: {arg1}, arg2: {arg2}")
print_two("juice", "bob")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")
print_two_again("guwop", "thugger")

def print1(arg1):
    print(f"arg1: {arg1}")
print1("bob")

def print_none():
    print("I got nothing to say")

print_none()