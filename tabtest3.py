import tkinter as tk
from tkinter import ttk

root = tk.Tk()

style = ttk.Style()

style.layout('TNotebook.Tab', []) # turn off tabs

note = ttk.Notebook(root)

f1 = ttk.Frame(note)
txt = tk.Text(f1, width=40, height=10)
txt.insert('end', 'Page 0 : a text widget')
txt.pack(expand=1, fill='both')
note.add(f1)

f2 = ttk.Frame(note)
lbl = tk.Label(f2, text='Page 1 : a label')
lbl.pack(expand=1, fill='both')
note.add(f2)

note.pack(expand=1, fill='both', padx=5, pady=5)

def do_something():
    note.select(1)
ttk.Style().theme_use('alt')
root.after(3000, do_something)
root.mainloop()