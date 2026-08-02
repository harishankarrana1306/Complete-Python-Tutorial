# Finally Clause --Iske ander dala hua code hamesa run karta hai chahe error aaye ya naa aaye
def function1():
  try:
    l=[1,5,6,7]
    i=int(input("Enter the Index : "))
    print(l[i])
    return 1
  except: 
    print("Some error Occured ")
    return 0
  finally:   #return hona hi hona hai
    print("I am always Executed")


x= function1()
print(x)