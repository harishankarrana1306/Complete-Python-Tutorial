# For loop    --string Itterate

name = "Harishankar"
for i in name:           # i means identifier or every character
    # print(i, end=",")   or
     print(i, end=" ")    # H a r i s h ... print hoga
     if(i=="r"):
       print("Runned after r ", end=" ")  # H a r runned after r i s h a n k a r 


for i in range(len(name)):
 print(name,end=" ")      # print harishankar 11 times
 print(i,end=" ")         # print indexes

print()

num = {3,4,5,6,7,8}
for i in num:
    print(num,end=" ")    # 3,4,5,6,7,8 cursor stills at this position after running this program

print()    # cursor moves to next line

for i in range(len(num)):
    print(i,end=" ")     # will print indexing
print()

    #for Itterating List in array

colour = ["red","Blue","Orange","Green"] 
for external in colour:
    print(external)
    for i in external:
     print(i)

 # for printing numbers from 0 TO N  
n = int(input("Enter the number : "))

for k in range(n):       # Zero se leke n-1 tak jayega
   # for k in range (0,10) or whatever we can assign range here too
   print(k+1,end=" ")    # for starting form 1 , k1
print()
for k in range(1,12,3):
   print(k)