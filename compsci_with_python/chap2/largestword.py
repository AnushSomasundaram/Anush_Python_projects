length= int(input("Enter the number of elements in the list"))

words=[]

for i in range (0,length):
    print("Word no.",i,":-")
    words.append(str(input()))


longest=0
for i in range (1,length):
    if len(words[i])>len(words[longest]):
        longest=i

print("longest word is :-",words[longest])


    