
def phonenumbertest():
    p= input("Phone number:-")

    value=False

    if len(p)==12 and p[3]=="-" and p[7]=="-":
        if p[0:2].isdigit and p[3:7].isdigit and p[7:].isdigit:
            value= True

    else:
        value = False

    if value == True:

        print(p,"is a valid phone number")
    else:
        print(p,"Is not a valid phone number")

phonenumbertest()

