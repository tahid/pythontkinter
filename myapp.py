from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def update(rows):
    for i in rows:
        trv.insert('','end',values=i)

def search():
    trv.delete(*trv.get_children())
    q2 = q.get()
    query = "select id,forename,surname,street from customers where forename like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)
def clear():
    query = "select id,forename,surname,street from customers"
    cursor.execute(query)
    rows = cursor.fetchall()
    update(rows)
mydb = mysql.connector.connect(host="localhost",user="houseauctionusr",passwd="fu34n5ju4h35",database="houseauctioncrm",auth_plugin="mysql_native_password")
cursor = mydb.cursor()

root = tk.Tk()
q = StringVar()
wrapper1 = Frame(root)
wrapper2 = LabelFrame(root,text="Search")
wrapper3 = LabelFrame(root,text="Customer Data")

wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)

trv = ttk.Treeview(wrapper1,columns=(1,2,3,4),show="headings",height="12")
trv.pack(fill="both",expand="yes")
trv.heading(1, text="customer Id")
trv.heading(2,text="First Name")
trv.heading(3,text="Last Name")
trv.heading(4,text="street")



query = "select id,forename,surname,street from customers"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)


lbl = Label(wrapper2, text="search")
lbl.pack(side=tk.LEFT,padx=10)
ent = Entry(wrapper2,textvariable=q)
ent.pack(side=tk.LEFT,padx=6)
btn = Button(wrapper2,text="Search",command=search)
btn.pack(side=tk.LEFT,padx=6)
btn2 = Button(wrapper2,text="Clear",command=clear)
btn2.pack(side=tk.LEFT,padx=6)
root.title("My Application")
root.geometry("1920x1080")
#('aqua', 'clam', 'alt', 'default', 'classic')
ttk.Style().theme_use('alt')
root.mainloop()