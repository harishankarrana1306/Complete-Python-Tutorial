# OS module  ---creating folders
#  execution of program, copy from one folder to another, Sorting

# import os
# print(dir(os))   
# if(os.path.exists("data")):  #It checks for whether path exists or not
#     os.mkdir("data")      


# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1 }")  # it will make or create folder from day 01 to day 100

# to rename the folders name 
# os.rename(f"data/Day{i+1 }",f"data/Tutorial{i+1 }")
# Renaming from day to tutorial



# To know or Print How many folders exist
import os   # can make program to search for folders
folders=os.listdir("data")
for fold in folders:
    print(os.listdir(f"data/{fold}"))
    # folder ke saath saath folder ke ander jitni bhi cheeze rahengi sab print ho jayengi

