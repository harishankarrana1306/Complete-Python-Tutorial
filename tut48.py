#Local and global Variable 
# hello ke ander aeesa kya kare ki ye x=5 ho jaye from x=4

x=10
print(x)


def hello():
    global x   #once we add global into fn it changed for x=10 --- x=5
    x=5   #local allag chalta hai global allag chalta hai ye x=4 ko replace nhi karega
    y=5 
    print(x)
    print("hello world")


hello()
print("The global variable is :",x)
# print(y)--->will throw an error as it in not available globally

