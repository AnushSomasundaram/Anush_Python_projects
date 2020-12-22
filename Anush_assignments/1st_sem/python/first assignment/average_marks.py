#Write a program to read five subjects marks and find the average.

marks=[]

i=0


while i<5:
    marks.append(int(input("Enter the marks out of 100 in subject :-")))
    i=i+1


total=0
for ele in marks:
    total=ele+total

average = total/5

print("The average marks acquired :-" , average,".")

