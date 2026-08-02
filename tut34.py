ep1={1:45,2:49,3:48,4:41,5:43}
ep2={6:21,7:22,8:23,9:24}
ep1.update(ep2)
print(ep1)

ep1.pop(1)   #remove single key value
print(ep1)
ep1.popitem()  # removes last item key pair
print(ep1)

# ep1.clear()  # become empty dictionary
# print(ep1)

# empt={}      # This is also empty Dictionary
# print(empt)

del ep1[3]   # delete particular key along with its value
print(ep1)


