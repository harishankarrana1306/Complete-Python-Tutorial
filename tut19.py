# Break and continue Statement
for i in range(12):
 if(i == 5):
   break 
    # continue
 print("5 X",i,"=",5*i)
 
 
print("loop exit when i==5")


# continue means uss wali valur ko choor ke baaki sab ko print karo


# infinite loop  here till 100
i = 0
while True:
  print(i)
  i=i+1
  if(i%100==0):
    break
 
  