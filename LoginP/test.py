import sqlite3
from tkinter import *
from tkinter import messagebox

user = "amal"
passw ="amal"
conn = sqlite3.connect('../BD/data.db')
cur = conn.cursor()
cur.execute(
    " select distinct v6 from Utilisateur where v7 ='" + user + "' and v4 ='" + passw + "';")
role = cur.fetchone()
conn.commit()
conn.close()
global verif
verif = role[0]
print("-----------------------")
print(role)
print("-----------------------")
print(role[0])

conn = sqlite3.connect('../BD/data.db')
cur = conn.cursor()
cur.execute(
    " select distinct v1 from Utilisateur where v7 ='" + user + "' and v4 ='" + passw + "';")
name = cur.fetchone()
conn.commit()
conn.close()
print("-----------------------")
print(name[0])
print("-----------------------")
messagebox.showinfo("","Bienvenus "+name[0])
