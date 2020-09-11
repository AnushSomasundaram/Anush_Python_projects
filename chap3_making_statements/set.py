#a tuple is a regular list which cannot be manipulated.it is fixed(and is defined using parenthesis())
#a set is a list where elements cannot repeat.(depicted using AQUARE BRACKETS {})
zoo=("Kangaroo","leopard","Moose")
print('Tuple:',zoo,"\t Length:",len (zoo))
print(type(zoo))

bag={"Red","Green","Blue"}

bag.add("Yellow")

print(" \nSet:-", bag, "\t length:-", len(bag))

print(type(bag))

print("\n Is green in bag :","Green" in bag)

print("\n Is Orange in bag :","Orange" in bag)

box={"Red","Purple","Yellow"}

print("\nSet",box,"\t\tLength",len(box))

print("Common to both sets:",bag.intersection(box))
