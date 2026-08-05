#  Lambda Functions in python -- to write anonymous functions

# def double(x):
#     return x*2       #rather than writing this

double = lambda x: x*2 
cube = lambda y: y*y*y
average = lambda x,y: (x+y)/2

def app(fx,value):
    return 6*fx(value)

print(double(5))
print(cube(6))
print(average(4,8))

print(app(cube,4))   # here fx is cube    or

print(app(lambda y: y*y*y,4))

