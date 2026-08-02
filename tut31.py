# sets ----No repetation or duplication -{a,s,d,f,g}-unordered
# list =[a.s.d.f.g]    can make changes
# tupple=(a,s,d,f,g)   cant make changes

s={2,4,6,2}
print(s)   # it will return two(2) only once --{2,4,6}

info={"carla",19,"hello",5.9,19}
print(info)    # provides unordered output koi bhi kahi bhi aajeyga output me 

newset=()
print(type(newset))   #returns dictionary-{} type

hari=set()
print(type(hari))     #return set type

for i in info:
    print(i)
    # for j in i :
    #     print(j)   # trhow error as int obj not itterable

