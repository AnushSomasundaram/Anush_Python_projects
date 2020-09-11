#when two operands are compared by the computer it checks if the criteria holds true by comparing their
#ascii code values and returns one of two values True or False(boolean).

nil=0
num=0
max=1
cap="A"
low="a"

print("Equality:\t",nil,"=",num,nil==num)
print("Equality:\t",cap,"=",low,cap==low)
print("Inequality: ",min,"!=",max,min!=max)
print("Greater: \t",nil,">",max,nil>max)
print("Lesser: \t",nil,"<",max,nil<max)
print("More or equal: \t",nil,">=",num,nil>=num)
print("less or equal: \t",max,"<=",num,max<=num)