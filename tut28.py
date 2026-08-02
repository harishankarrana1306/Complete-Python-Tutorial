letter="Hey my name is {0} and i am from {1} "
country="india"
name="harry"
print(letter.format(name, country))


# fstring --app apne string ke ander variable dalll sakte ho

print(f"Hey my name is {name} and i am from {country}")


price=54999.99
txt=f"The price of PS5 is : {price} rupees"
print(txt)
# print(txt.format(price=54999.99))

print((f"{2*30}"))
print(type(f"{2*30}"))