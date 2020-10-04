sentences=str(input("Type in a couple of sentences, and then press enter :- \n"))
wordcount=1
for char in sentences:
    
    if char==" " or char=="  " or char=="   ":
        wordcount+=1


alphacount=0
for char in sentences:

    if char.isalnum :
        alphacount+=1
        
alphacent= (alphacount/len(sentences))*100

print("Number of words in sentences =",wordcount)
print("Number of charecters=",len(sentences))
print("Percentage of alphanumeric charecters:",alphacent,"%")


