n=int(input("How many students? :-"))
CompWinners={}
for a in range(n):
    key=input("Name of student:-")
    value=int(input("Number of competitions won: "))
    CompWinners[key]=value

print("The dictionary now is :")
print(CompWinners)
