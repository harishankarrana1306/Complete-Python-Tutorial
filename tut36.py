# Exceptional Handling

#instead of int if u provide string it will terminate program at the starting 

a=input("Enter the Number : ")  
print(f"Multiplication table of {a} is : ")
try:
   for i in range(1,11):
    print(f"{int(a)} X {i} =  {int(a)*i}")
# except Exception as e:
except:
#   print(e)   # e means by default python error statement 
  print("Invalid Input")


print(5)


try:
    num=int(input("Enter an integer : "))
    a=[6,3]
    print(a[num])
except ValueError:
   print("Number entered is not an Integer. ")
except IndexError:
   print("Index Error")


