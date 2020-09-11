from tkinter import *
import tkinter.messagebox as box

window=Tk()
window.title('Idiots')

frame=Frame(window)

var_1=IntVar()
var_2=IntVar()
var_3=IntVar()

hello_1= Checkbutton(frame,text="Stupid",variable=var_1,onvalue=1,offvalue=0)

hello_2= Checkbutton(frame,text="An idiot",variable=var_2,onvalue=1,offvalue=0)

hello_3= Checkbutton(frame,text="a bozo",variable=var_3,onvalue=1,offvalue=0)

def dialog():
    
   box.showinfo('HAHA','You are correct')

btn=Button(frame,text='Choose',command=dialog)
btn.pack(side=RIGHT,padx=5)
hello_1.pack(side=LEFT)
hello_2.pack(side=LEFT)
hello_3.pack(side=LEFT)
frame.pack(padx=30,pady=30)

window.mainloop()

