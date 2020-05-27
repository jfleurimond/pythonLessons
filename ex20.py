from sys import argv

script, input_file = argv

#f is the function variable that we pass the input_file through 

def print_all(f):
    print(f.read())

def rewind(f):
    #deals with moving the file to the (0) first byte in the file
    f.seek(0)

def print_a_line(line_count, f):
    #readline() reads the line of a file, and then moves to the next line after \n
    print(line_count, f.readline())

#the f file maintains the current position in the file, after each readline()
current_file = open(input_file)

print("First let's pring the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)