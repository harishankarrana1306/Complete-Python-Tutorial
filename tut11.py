# String -- like an array of character 
# for printing we can use both single or double quote

# when u wanna make " as a part of string then there are two option
# with print() agar kisi cheez ko hm ''' ''' /""" """ke ander karde to wo puri string bann jayegi
name ="Hari"
friend = "Viraj"
print("hello " + name)
print('Hii ! "How are u dude "')  # method 1
print("Hii ! \"How are u dude ")   # method 2 

print(''' 
      Hello                
      wassup
      how u doing
      ''')

# usefull when u r writing story or novel 

print(name[0],name[1],name[2])   


# to print every character one by one of array in sequence 

print("lets use it for loop")
for character in name:  # name ke character ke ander jaoo
    print(character)    # characters ko print kardo 