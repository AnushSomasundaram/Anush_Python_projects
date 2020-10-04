length = int(input("Length Of List"))

pointlesslist=[]

print("Input the List elements:-\n")

for i in range(1,length+1):
    print("The Element",i,":-")
    pointlesslist.append(input())


varele = pointlesslist[length-1]

for i in range(0,length-1):
    temp=pointlesslist[i]
    pointlesslist[i]=pointlesslist[i+1]
    pointlesslist[length-1]=temp

for i in range(0,length-1):
    print("The Element",i,":-")
    pointlesslist[i]



