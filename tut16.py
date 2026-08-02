# switch case statement

x=int(input())
print("Enter  the Number ",x)
match x:
    
     # If x=O
 case 0:
    print("X is zero")

 case 1:
    print("The number is odd")
 case 4:
      print("The number is divisible by 2")
 case 7:
      print("The number is SEVEN")
 case _ if x!=80:
        print("The number is not 80")
      
 case _:    #_ used for default case
       print("THE NUMBER IS :",x)

       #when two or more case are true and u want to run only one -- break:




 