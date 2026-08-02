# LIST
# list of marks of student ,list of participated student etc
# list start with square baracket and sepearated by ,
l=[3,4,5,6,7,8,9]
print(l)
# print(l[:])   this can also print whole element of list
print(type(l))

print(l[0])        # list index
print(l[1])
print(l[2])
print(l[3])
print()
print(l[-3])     # total length - 3   (7-3 = 4)
print(l[1:4])  # from 1 to n-1 = 3 
print(l[0:8:2])  #starts from 0th jump at every 2nd index and till (8-1)th index

if 7 in l:
    print("yes")
else:
    print("No")



# Eek list ke ander string , boolean bhi aa sakta hau
#list allow duplicates items




# List Comprehension
lst=[i for i in range(10)]
lst1=[i for i in range(10)  if i%2==0]
print([lst])
print([lst1])
    