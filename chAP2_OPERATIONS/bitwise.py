
a=10
b=5 
print("a=",a,"\t b=",b)

#we are using xor gate to sitch the values of a nd b by manipulating bits
#1010^0101=1111(decimal15)

a=a^b

#1111^0101=1010(decimal 10)
b=a^b

#1111^1010=0101(decimal 5)
a=a^b

print("a=",a,"b=\t",b)