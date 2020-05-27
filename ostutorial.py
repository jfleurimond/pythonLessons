import os
print(os.name)
print(os.path.abspath('.') + "\n")
print(os.listdir('.'))

# Going to use os.stat to find the file size of a file ex: os.stat(file).st_size




#Great way below to deal with error handling
# import os 
# try: 
    # If the file does not exist, 
    # then it would throw an IOError 
    # filename = 'GFG.txt'
    # f = open(filename, 'rU') 
    # text = f.read() 
    # f.close() 
  
# Control jumps directly to here if  
#any of the above lines throws IOError.     
# except IOError: 
  
    # print(os.error) will <class 'OSError'> 
    # print('Problem reading: ' + filename) 
      
# In any case, the code then continues with  
# the line after the try/except 
