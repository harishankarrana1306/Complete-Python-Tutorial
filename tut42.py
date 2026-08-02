# Enumerate function in python

# marks=[34,43,45,46,26,47]
# index=0
# for i in marks:
#     print(i)
#     if(index == 3):
#         print("We are at 3rd index")
#     index+=1



    # Enumerate 

marks=[34,43,45,46,26,47]

for index, i in enumerate(marks): # provides value along with index
    print(i)
    if(index == 3):
        print("We are at 3rd index")
    # index+=1   ye karne ki jaroorat nhi hai

# changing the start index

for index, i in enumerate(marks,start=1):
    print(i)
    if(index == 3):
        print("We are at 3rd index starting from 1")