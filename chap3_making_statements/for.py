# A a for keyword loops over all items in any list specified to the in keyword

chars=["A","B","C"]
fruit=("Apple","Banana","Cherry")
dict={'name':"mike","ref":"Pyhton","sys":"Win"}

print("\nElements:\t",end=" ")

for i in chars:
    print(i,end=" ")

for item in enumerate(chars):
        print(item ,end=" ")

print("\nZipped\t ", end="")
for item in zip(chars,fruit):
    print(item , end=" ")

print("\n paired")
for key, value in dict.items():
    print(key,"=",value)





 