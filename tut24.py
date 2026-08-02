#tupples are ordered collection of data items -- immutable

tup=(1,)  # to make tupple of just 1 we have to use , otherwise python will get confused
tup=(1,2,3,5,6,89,23,"green","Yellow")
# tup=[1,2,3,5,6,89,23]   # this will become list 

print(type(tup),tup)  #return -- []--list , ()- tuple

# Why to use tupple if we cant change them
# -- it requires sometime where we dont want to change value

print(tup[0])
print(tup[1])
print(tup[2])

if 3421 in tup:
    print("yes")
else:
    print("no")

# Sliciing in tupple --- tup(start:end:jump index)
   #slicing karne ke badd tupple change nhi hota new tupple bann jata hau

print(tup[0:7:2])  #starts-0th, end= n-1, jump=2 
print(tup[0:])   #starts with zero
