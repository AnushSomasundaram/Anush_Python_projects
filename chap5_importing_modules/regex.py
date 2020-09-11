#this is tediouswork....it runs but not correctly...point has been acquired

from re import *

pattern=compile("(^|\s)[-_.a-z0-9]+@([-a-z0-9]+\.)+[a-z]{2-6}(\s|$)")

def get_address():
    address=input("Enter your email address\t")
    is_valid=pattern.match(address)
    if is_valid :
        print("valid address:",is_valid.group())
    else:
        print("invalid address!")

get_address()