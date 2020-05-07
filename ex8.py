#more use of the format function in strings 
formatter = " {} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four" ))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter, ))
print(formatter.format(
    "This is my own test", 
    "Seriously it is", 
    "Should print on the same line",
    "Eventhough I'm writing them on seperate lines :)"
))
