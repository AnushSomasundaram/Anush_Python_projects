#there is a python time module as well as a python datetime module

from time import *

start_timer=time()

struct=localtime(start_timer)


print("Starting countdown at ",strftime("%X",struct))
i=10
while i>-1:
    print(i)
    i-=1
    sleep(1)

end_timer=time()

difference=round(end_timer-start_timer)
print("\n Runtime ",difference,"seconds")




