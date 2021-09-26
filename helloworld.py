from tkinter import ttk

from tkinter import *

root = Tk()
root.title('Auction House')
p1 = PhotoImage(file = 'icons8-judge-64.png')
root.iconphoto(False, p1)

def myClick():
    myLabel = Label(root, text="test")
    myLabel.pack()

n = ttk.Notebook(root)
f1 = ttk.Frame(n)   # first page, which would get widgets gridded into it
f2 = ttk.Frame(n)   # second page
n.add(f1, text='One')
n.add(f2, text='Two')

myLabel = Label(f1, text="Hello World!");
myButton = Button(f2, text="Click Me !!",padx=30,pady=10,command=myClick)
entry = Entry()
text_box = Text()
myLabel.pack()
myButton.pack()
entry.pack()
text_box.pack()
root.mainloop()