#   functions -perform task whenever called
        # 1. Built-in functions(list,tupple,dictionary,range)
        # 2. User defined Function
a=8
b=8
gmean1=(a*b)/(a+b)
print(gmean1)

c=8
d=8
gmean2=(c*d)/(c+d)
print(gmean2)     # to dont repeat we need functions


# functions
def calgmean(e,f):      # defining function
    mean=(e*f)/(e+f)
    print(mean)


calgmean(40,84)


def greater(a,b):
    if a>b:
        print(a,"Is Greater than ",b)
    else:
        print(b,"Is greater than ",a)

greater(25,15)

def functionn(l,m):
    pass           #Pass means mai ye function badd me likhunga
