from tkinter import *

root = Tk()
root.title('Intrest Calculator')

def Clear():
    p.delete(0,END)
    r.delete(0,END)
    t.delete(0,END)

def SI():
    SI_label = Label(root,text=int(p.get())*int(t.get())*int(r.get())/100)
    SI_label.grid()

def CI():
    pr = int(p.get())
    tr = int(t.get())
    rr = int(r.get())
    CI_label = Label(root,text=pr*((1+rr/100)**tr)-pr)
    CI_label.grid()
    

SI_Button = Button(root,text='Calculate SI',padx=20,pady=20,command=SI)
CI_Button = Button(root,text='Calcualte CI',padx=20,pady=20,command=CI)
Clear_Button = Button(root,text='Clear',padx=20,pady=20,command=Clear)

lp = Label(root,text='Principal')
lt = Label(root,text='Time')
li = Label(root,text='Intrest Rate')

p = Entry(root,borderwidth=10,bg = 'Yellow')
t = Entry(root,borderwidth=10,bg = 'Yellow')
r = Entry(root,borderwidth=10,bg = 'Yellow')

lp.grid(column=0,row=0)
p.grid(column=1,row=0)

lt.grid(column=0,row=1)
t.grid(column=1,row=1)

li.grid(column=0,row=2)
r.grid(column=1,row=2)

SI_Button.grid(column=0,row=3)
CI_Button.grid(column=1,row=3)
Clear_Button.grid()

root.mainloop()