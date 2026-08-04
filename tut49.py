# file handling 
# w=write(w),r=read(r),a=append(a),create(x),text(t),binary(b)


# Reading to a file
# f = open('myfile.txt','r')
# text=f.read()
# print(text)
# f.close()


# Writting to a file


# f = open('myfile2.txt','a')  # use a inplace of w for append
# f.write("Hello world\n")
# f.close()

# write mode me agar apne aeesi file open kardi jo exist nhi karti to wo bann jayegi

with open('myfile.txt','a') as f :
    f.write("hey i am inside it") 
#using with statement we dont have to use f.close()--automatically

