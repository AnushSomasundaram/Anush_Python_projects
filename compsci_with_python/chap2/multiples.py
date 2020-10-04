threefive=[]

for i in range(0,100):
    
    if i%3==0 or i%5==0:
        threefive.append(i)

print("Number of elements in list are",len(threefive))
print("The Elements in the list are:- ")

for i in threefive:
    print(i," ")
