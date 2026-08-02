# List methods 

lis=[1,1,3,8,1,6]
# lis.append(7)        #append takes only one element
# lis.sort()          # increasing order
# lis.sort(reverse=True)    # Decreasing order
# lis.append([7,8,9])  # here list is treated as single
print(lis)
print(lis.index(8))    #gives the index at which 6 is present
print(lis.count(1))   #it count how many times 1 comes in list --2


#whereas to make copy

m=lis.copy()
m[0]=0
print(m.count(1))
print(m)
print(lis)

# m = lis
# m[0]=0   # m change kiya to lis bhi change ho jaayegi
# print(m)

lis.insert(1,899) # 899 ki list me index 1 hogi added not replaced
print(lis)

n=[100,200,300,400]
k=lis+n       # method 1
print(k)
lis.extend(n) # method 2
print(lis)







