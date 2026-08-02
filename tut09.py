#   TYPE CASTING -- conversion of one data type to another
        #   1. Explicit Conversion --khud karna
        #   2. Implicit conversion - Python khud kar raha


a="1"
b="2"

print(a+b)
    #  Agar same a/b ko hame dusre me change karna hai without declaration

print(int(a)+int(b))     # explicit conversion

# functions -- int(),float(),str(),ord(),hex(),oct(),
# -- tuple(),set(),list(),dict() etc
 
# different data types have different order level
# while conversion lower version convert into higher version

        #   2. Implicit conversion 

c = 1.9
d = 8

print(c + d)    # here d converted from int to float
