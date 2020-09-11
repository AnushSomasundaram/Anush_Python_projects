#precedence means the condition of being considered more important than someone or 
# something else; priority in importance, order, or rank.


a=2
b=4
c=8

print("\nDefault order \t ",a,"*",c,"+",b ,"=",a*c+b)
print("\nForced order:\t ",a,"*","(",c,"+",b,") =",a*(b+c))

print("\n In default order\t",c,"//",b,"-",a,"=",c//b-a)
print("\nForced order\t",c,"//(",b,"-",c,"=",c//(b-a))

print("\nDefault order\t ",c,"%",a,"+",b,"=",c%a+b)
print("\nForced order\t ",c,"%(",a,"+",b,")=",c%(a+b))

print("\nDefault order\t",c,"**",a,"+",b,"=",c**a+b)
print("\nForced order\t",c,"** (",a,"+",b,") =",c**(a+b))
