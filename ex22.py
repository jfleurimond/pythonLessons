#No code at all with this one, just revisting what we learened 

testFile = open("text15exercise.txt", "r")

print(testFile.read())

#format is really interesting you can use {} placeholders to then insert variables/strings/or numbers

list = " {} {} {} {} "

print(list.format(3, 3, 3,1))