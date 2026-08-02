# default & Parameterized function

def avg(a=9,b=1):
    print((a+b)/2)


avg(b=4)  # then it will automatically take a=9
avg(4)  # then it will automatically take b=1

def name(fname,mname = "Jhon",lname="Whatson"):
    print("Hello,",fname,mname,lname)

name("amy", "Aggarwal")

# Keywords Arguments --can change the order of arguments

avg(b=5,a=10)  # can give arguments in diff order too


# variable Length Argument

def average(*numbers):     # numbers ki list by own
    sum=0
    for i in numbers:
        sum= sum + i
    # print("Average is" ,sum/(len(numbers)))
    return sum/(len(numbers))

# average(10,15,20,15)
c=average(10,15,20,15)
print(c)