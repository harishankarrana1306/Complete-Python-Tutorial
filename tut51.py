# seek() and tell() functions
# --used to work with file objects and their positions within a file

# with open ("myfile.txt",'r') as f:
#     print(type(f))

#     f.seek(3) #Move to the 3th position in the file

# #read the next 5 bytes
#     data=f.read(6)
#     print(data)  #print after seeking(from specific location)


with open("myfile.txt",'w') as f:
    f.write("Hello World!")
    f.truncate(5)  # files me sirf 5 characters rahenge 


with open('myfile.txt','r') as f :
    print(f.read())