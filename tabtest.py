from tkinter import ttk
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

def CreateUI(self):
    tv = ttk.Treeview(self)
    tv['columns'] = ('Name', 'Mobile', 'course')
    tv.heading("#0", text='RollNo', anchor='w')
    tv.column("#0", anchor="w")
    tv.heading('Name', text='Name')
    tv.column('Name', anchor='center', width=100)
    tv.heading('Mobile', text='Mobile')
    tv.column('Mobile', anchor='center', width=100)
    tv.heading('course', text='course')
    tv.column('course', anchor='center', width=100)
    tv.pack()
    self.treeview = tv

def demo():
    root = tk.Tk()
    root.title("ttk.Notebook")
    p1 = tk.PhotoImage(file = r'icons8-judge-64.png')
    root.iconphoto(False, p1)
    root.wm_iconphoto(False, p1)
   
    nb = ttk.Notebook(root)

    # adding Frames as pages for the ttk.Notebook 
    # first page, which would get widgets gridded into it
    page1 = ttk.Frame(nb)

    # second page
    page2 = ttk.Frame(nb)
    text = ScrolledText(page2)
    text.pack(expand=1, fill="both")

    nb.add(page1, text='One')
    nb.add(page2, text='Two')

    nb.pack()
    CreateUI(root)
    root.mainloop()

if __name__ == "__main__":
    demo()