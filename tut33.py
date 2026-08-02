# Dictionary -orderes

# dic={
#    "Harry": "Human Being",
#    "Spoon": "Object to Eat",
# }

# print(dic["Harry"])
# print(dic["Spoon"])

# empid={
#      1: "Sharvil",       # key : Value
#      2: "Viraj",
#      3: "Hari",
#      4: "Kriyal",
# }
# print()
# print(empid[1])
# print(empid[2])
# print(empid[3])
# print(empid[4])

info={"name":'Karan',"Age":19,"Eligible":True}
print(info)
print(info['name'])
# to get all keys together
print(info.keys())   # to get all keys
print(info.values())
print(info.items())    # To get [key & value]  in pair s

for key in info.keys():
    # print(key,info[key])   #key--prints key ,info[key]--prints values at key
    print(f"The value at corresponding to the key {key} is : {info[key]}")

for key,value in info.items():
  print(f"The value at corresponding to the key {key} is : {value}")
  

