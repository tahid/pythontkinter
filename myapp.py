from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def update(rows):
    for i in rows:
        trv.insert('','end',values=i)

mydb = mysql.connector.connect(host="localhost",user="houseauctionusr",passwd="fu34n5ju4h35",database="houseauctioncrm",auth_plugin="mysql_native_password")
cursor = mydb.cursor()

root = tk.Tk()

wrapper1 = LabelFrame(root,text="Customer List")
wrapper2 = LabelFrame(root,text="Search")
wrapper3 = LabelFrame(root,text="Customer Data")

wrapper1.pack(fill="both", expand="yes",padx=20,pady=10)
wrapper2.pack(fill="both", expand="yes",padx=20,pady=10)
wrapper3.pack(fill="both", expand="yes",padx=20,pady=10)

trv = ttk.Treeview(wrapper1,columns=(1,2,3,4),show="headings",height="6")
trv.pack(fill="both",expand="yes")
trv.heading(1, text="customer Id")
trv.heading(2,text="First Name")
trv.heading(3,text="Last Name")
trv.heading(4,text="street")



query = "select id,forename,surname,street from customers"
cursor.execute(query)
rows = cursor.fetchall()
update(rows)

root.title("My Application")
root.geometry("1920x1080")
root.mainloop()