noe=int(input("The number of elements in each list:-"))
L=[]
M=[]
print("Input the elements of list L")
x=0

while x < noe :

    
    L.append(int(input("input element:-")))

    x=x+1

print("Input the elements of list M")
x=0
while x < noe :

    M.append(int(input("input element:-")))
    
    x=x+1

N=[]

for i in range(0, len(L)): 
    N.append(L[i] + M[i])

print("The final list N is:-")
for i in range(0,len(N)):
    print(N[i])


 





