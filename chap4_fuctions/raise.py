day=32

try :
    if day>31:
        raise ValueError("Invalid day number")
        #more statements to execute get added here

except ValueError as msg:
    print("The program found an", msg)
finally:
    print("But today is a beautiful day")

    