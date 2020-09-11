from tkinter import *

window=Tk()
window.title("Message Box Example")

def dialog():   
    var = box.askyesno("Message Box","Proceed?")
    if var==1:
        box.showinfo('Yes Box','proceeding...')

    else:
        box.showinfo('No Box','Cancelling')

btn=Button(window,text="CLick",command=dialog)
btn.pack(padx=150,pady=50)
window.mainloop()

