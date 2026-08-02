a="harry" 
print(len(a))
print(a.upper())
print(a.lower())


#  rstrip() -- removes character like !,&,%,$ or whatsoever present at end only

name="hari&&&&&"

print(name.rstrip("&"))

friend="viraj"
print(friend.replace("viraj","Jonny"))

# split() --- jaha spaces honge wo eek aalag element ho jayega

friends ="kriyal viraj sharvil"

print(friends.split(" "))

#           Capitalize()

# hi = "hello"   or
hi="heLLo"    # automatic 1-upper case ,rest - all lower case 

print(hi.capitalize())

#               Centre() - add spaces 

string ="Welcome"  # total characters =7

print(string.center(14))   # add spaces and make it of 14

#          count()  - the no of times given value occur 

b ="Harry Harry veer "
print(b.count("Harry"))
print(b.count("veer"))


#   endswith()  - its check if it ends with given value
#     it also checks for a value in-btwn the string by providing
#     start and end index positions.

c = "Welcome to PICT!!"    
print(c.endswith("!!"))    # returns True or False 
print(c.endswith("come",3,7))  #for last its n-1


#       find()   

d = "Hello This is my family"
print(d.find("family"))   # provides first index occurance
print(d.find("harry"))    # when no value find --returns -1

# index  -- when no values found - provides error 

#    isalnum() - returns True only if the entire string consists of only
#                   A-z,a-z,0-9 if any other found --false

e="harishankar#"
print(e.isalnum( ))

#    isalalpha() - returns True only if the entire string consists of only
#                   A-z,a-z if any other found --false

f="harishankar"
print(f.isalpha())

#   islower  - returns true only if the entire string - lower case

g="viraj "
print(g.islower())

#   isupper  - returns true only if the entire string - upper case

k="VIRAJ "
print(k.isupper())

#   isprintable  - returns true only if the entire string are printable ow false

h="viraj\n"    #\n not printable
print(h.isprintable())

#        isspace() -- returns true only string contain spaces

i = "viraj suryavanshi"    # false
i = "       "              # true
print(i.isspace())  

#  istitle()  true only if First letter of each word is capital
j= "Harishankar Singh"
print(j.istitle())    # true

#      startswith() - Checks if the string starts with given value

l= "This is mine 3rd day of coding"
print(l.startswith("This"))    #true

# swapcase()  --lower to upper and upper to lower
m = "Hii this is hari"
print(m.swapcase())

#  title() -- Capitalized Each first letter of the word
m="harishankar"
print(m.title())
