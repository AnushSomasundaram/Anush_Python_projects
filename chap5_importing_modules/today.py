#python has a date time module

from datetime import *

today=datetime.today()
print("Today is ",today)

for i in ["year","month","day","hour","minute","second","microsecond"]:

    print(i,":\t",getattr(today,i))

print("Time",today.hour,":",today.minute,sep=" ")

day=today.strftime("%A")
month=today.strftime("%B")

print("Date:",day,month,today.day)



