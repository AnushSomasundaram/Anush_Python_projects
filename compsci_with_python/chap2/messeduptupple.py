fibonacci=[]

    
number_of_terms=9
counter=0
first=0
second=1
temp=0

while counter < number_of_terms:
    fibonacci.append(first)
    temp=first+second
    second=first
    first=temp
    counter+=1



fibonacci=tuple(fibonacci)


for i in fibonacci:
    print(i)


