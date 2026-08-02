countries = ("spain","Italy","Japan","Russia","India")

temp=list(countries)     #temporary list

temp.append("America")  # add item
temp.pop(3)            # remove item  -starts with 0
temp[2]=('Finland')

countries = tuple(temp)  #again convertine temp list into tuple
print(countries)

print(len(countries))
#merging Two tuple

a=(0,1,2,3,4,5)
b=(6,7,8,9)
c=a+b
print(c)

res=c.index(7,4,9)  # Find 7, start-4, end-9-1,
print(res)
