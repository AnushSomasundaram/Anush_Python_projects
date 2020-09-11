basket=["Apple","Bun","cola"]
crate=["Egg","Fig","Grape"]
print("Basket List:-",basket)
print("Basket Elements",len(basket))

basket.append("Damson")
print("Appended:-",basket)
print("last item removed:-",basket.pop())
print("basket list:-",basket)

basket.extend(crate)
print("Extended list:",basket)
del basket[1]
print("item removed",basket)

del basket[1:3]
print("Sliced list:",basket)

