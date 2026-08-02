# we know jo bhi atti hai input as string aati hai

# to take it as input 
a =int(input("Whats your age : \n")) 
print("The age  is :",a)

#   if - elif - else 
if(a>18):
 print("you can drive") # intentation(space before print)

elif(a==18):
 print("Still you can drive") # intentation(space before print)

else:
 print("You can not drive")   # use space instead of{}
 print("No")

#For conditional check we use ==, >, <, >=, <=, !=

# print(a>18)          #print true or false
# print(a<18)
# print(a>+18)
# print(a>=18)
# print(a==18)

#    Nested if-else   -- eek if ke ander if

num=18

if(num<0):
 print("Number is negative")
elif(num>10):
     if(num<=10):
      print("Number is between 0 and 10")
     elif(num>10 and num<=18):
      print("The number is between 10 and 18")
     else:
       print("The number is greater than 18")
else:
  print("Number is Zero")


  