#functions providing a return as a value 

def add(a , b):
    print(f"Adding {a} + {b}")
    return a + b


sum = add(5, 7)

print(sum)

def subtract(a , b):
    print(f"Adding {a} - {b}")
    return a - b

def multiply(a , b):
    print(f"Adding {a} * {b}")
    return a * b

def division(a , b):
    print(f"Dividing {a} / {b}")
    return a / b

# Above we had the function return a value using some math 

def greeting (name):
    return(f"Hello {name}, how are you today?")


print(greeting("Justin"))