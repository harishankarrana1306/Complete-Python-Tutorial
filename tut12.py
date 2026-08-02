#  String Slicing and Operations on String  

name = "harishankar"

print(name[0:5])    # 0 to n-1 same as vector,list deque etc
print(name[1:5])     
print(name[:5])     # automatically takes it from zero index
print(name[0:-3])   #  =[0:len(name)-3]
print(name[-1:-3])  #  =[len(name)-1:len(fruit)-3] =[10:8]--makes no sense --no output
print(name[-3:-1])  # = [11-3:11-1] =[8:10] 10th index get ignored like vector

#length of string
print(len(name))

len1=len(name)
print("The length of Characters are :",len1)

 
 