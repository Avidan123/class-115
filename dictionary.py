from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("dictionary")

mutable_lbl=Label(root)
mutable_lbl.place(relx=0.5,rely=0.2,anchor=CENTER)
immutable_lbl=Label(root)
immutable_lbl.place(relx=0.5,rely=0.5,anchor=CENTER)
tkinter_lbl=Label(root)
tkinter_lbl.place(relx=0.5,rely=0.8,anchor=CENTER)

d={
   "mutable":"value that can be changed",
   "immutable":"value that cannot be changed",
   "tkinter": "it is the GUI library of python"
   }
def function1():
    mutable_lbl["text"]=d["mutable"]
    
def function2():
    immutable_lbl["text"]=d["immutable"]

def function3():
    tkinter_lbl["text"]=d["tkinter"]



b1=Button(root,text="press for definition of mutable",command=function1)
b1.place(relx=0.5,rely=0.1,anchor=CENTER)
b2=Button(root,text="press for definition of immutable",command=function2)
b2.place(relx=0.5,rely=0.4,anchor=CENTER)
b3=Button(root,text="press for definition of tkinter",command=function3)
b3.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()
