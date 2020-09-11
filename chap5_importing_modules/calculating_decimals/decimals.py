from decimal import *
item=Decimal(0.70)
rate=Decimal(1.05)

tax= item*rate
total=item+tax

#python has a decimal module...floating point errors can be avoided using the floating point module

print("Item:\t",item)
print("Tax:\t",tax)
print("Total:\t",total)