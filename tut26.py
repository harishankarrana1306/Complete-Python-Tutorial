import time

timestamp = time.strftime('%H;%M;%S')
print(timestamp)
hour = int(time.strftime('%H'))
print(hour)


if (hour>= 0 and hour<12) :
    print("Hello!, Good Morning Sir") 

elif(hour >=12 and hour<16):
    print("Hello!, Good Afternoon Sir") 

else:
    print("Hello!, Good Evening Sir") 