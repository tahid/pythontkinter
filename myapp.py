from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


root = tk.Tk()

wrapper1 = LabelFrame(root,text="Customer List")
wrapper2 = LabelFrame(root,text="Search")
wrapper3 = LabelFrame(root,text="Customer Data")
wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)
root.title("My Application")
root.geometry("1920x1080")
root.mainloop()