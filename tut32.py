# sets method

s1={1,2,5,6}
s2={3,6,7}

print(s1.union(s2))     # A U B 
print(s1.intersection(s2))    # A Intersection B

print(s1,s2)
s1.update(s2) #s1 ke ander wo values laoo jo s2 me hai
print(s1,s2)

cities={"Tokyo","Delhi","Madrid","Berlin"}
cities2={"Newyork","Tokyo","Hyderabad","Madrid",}

cities3=cities.union(cities2)
print(cities3)
cities4=cities.intersection(cities2)
print(cities4)


cities5=(cities.union(cities2))-(cities.intersection(cities2))
print(cities5)   # A U B - A inters B      - Symmetric difference
 #  or             (A-B) U (B-A)
cities6 = (cities-cities2).union(cities2-cities)
print(cities6)    # wo sari values jo common nhi hai

# or direct method
cities5 = cities.symmetric_difference(cities2)
print(cities5)

# disjoint sets --No elements in common
print(cities.isdisjoint(cities2)) # Returns False

# Super sets  --Kya eek set ke all element dusre me hai
print(cities.issuperset(cities2))  # return false for cities & cities2

#   Subset
print(cities.issubset(cities2))  # return false as all element of cities2 are not present in cities

cities.add("Patna")
print(cities)

cities.remove("Patna")    # if wanna remove a string
#cities.remove("Patna2")   # throw error as patna2 not present 
cities.discard("Patna2")   # using discard it ignores the patna2

cities.clear  # used to clear elements of cities

del cities      # deletes the entire set 
print(cities)     #after deleting it says cities not defined

# To check if any element is present in list or not
if "Tokyo" in cities:
  print("it is Present")
else:
  print("it is Absent")


 




