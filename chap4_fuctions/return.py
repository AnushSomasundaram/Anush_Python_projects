num=input("Enter an integer:")

def square(num):
    if not num.isdigit():
        return "invalid entry"
    else:
        num=int(num)
        return num*num

print(num,"squared is",square(num))

#the if statement could have been placed outside so that the finally result isn't gramatically incorrect

