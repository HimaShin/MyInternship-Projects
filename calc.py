from tkinter import *  #first import tkinter module
def click(event):
    global scvalue
    text=event.widget.cget('text')
    # print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
                


        scvalue.set(value)
        screen.update()
    elif text=='C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

r=Tk()
r.title('Himakar-GUI CALCULATOR')
r.geometry('600x900')
# r.wm_iconbitmap(r'C:\Users\ACER\Downloads\hill.ico')
scvalue=StringVar()
scvalue.set("")
screen=Entry(r,textvariable=scvalue,font='lucida 40 bold')
screen.pack(fill=X,ipadx=8,pady=10,padx=10)


# frame-1
f=Frame(r,bg='grey')
b=Button(f,text='9',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='8',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='7',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='+',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)
f.pack()

# frame-2
f=Frame(r,bg='grey')
b=Button(f,text='6',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='5',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='4',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='-',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

f.pack()

# frame-3
f=Frame(r,bg='grey')
b=Button(f,text='3',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='2',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='1',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='*',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

f.pack()

#frame-4
f=Frame(r,bg='grey')
b=Button(f,text='0',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='00',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='.',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='/',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)
f.pack()

#frame-5
f=Frame(r,bg='grey')
b=Button(f,text='%',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='**',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='C',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

b=Button(f,text='=',padx=23,pady=18,font='lucida 24 bold')
b.pack(side=LEFT,padx=13,pady=12)
b.bind('<Button-1>',click)

f.pack()

r.mainloop()