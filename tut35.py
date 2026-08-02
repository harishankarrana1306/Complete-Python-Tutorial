# Use of FOR loop In else Statement

for i in range(5):  # 0 to n-1
    print(i)
else:
    print("Sorry no I")

    # After itterating all the values in for loop 
    # Else will be executed afterwards

for i in range(6):
    print(i)
    if i==4:
        break
# once break else will be not executed
else:
    print("No value found")

