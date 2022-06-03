from tkinter import *
from tkinter import ttk
import random
import time
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import pygame
from pygame import mixer
import os
import os.path
import sqlite3


class Adc():
    def maininterface():
        windw = Tk()
        windw.geometry("1280x700")
        windw.maxsize(1280, 700)
        windw.minsize(1280, 700)
        windw.title("Interface Adminstrateur")
        windw.config(background="#D7DBDD")
        windw.iconbitmap("tt.ico")
        background_image = PhotoImage(file='../Images/IntAd.PNG')
        background_label = Label(windw, image=background_image)
        background_label.place(relwidth=1, relheight=1)


        def f1():
            x = np.linspace(1, 1000, 50)
            plt.loglog()
            plt.plot(x, 1. / x)
            plt.plot(x, 1. / x ** 2)

            plt.xlabel('Durée de vie ')
            plt.ylabel('Machine KOMAX ')
            plt.title('Durée de vie de Machine KOMAX ')
            plt.grid(True)
            plt.savefig("test.png")
            plt.show()

        def f2():
            x = np.linspace(0, 2 * np.pi, 30)
            y = np.cos(x)
            plt.plot(x, y)
            plt.ylim(-2, 2)
            plt.show()


        def f3():
            plt.grid(True)
            plt.plot([50, 100, 150, 200], [2, 3, 5, 7], "b", linewidth=0.8, marker="*")
            plt.plot([50, 100, 150, 200], [2, 7, 9, 10], "g", linewidth=0.8, marker="+")
            plt.show()

        def f4():
            x = [random.randint(0, 150) for i in range(1000)]
            n, bins, patches = plt.hist(x, 50,facecolor='b', alpha=0.5)

            plt.xlabel('Mise')
            plt.ylabel(u'Probabilité')
            plt.axis([0, 150, 0, 0.02])
            plt.grid(True)
            plt.show()

        def f5():
            name = ['Collecteur tournant', 'PYROLYSE', 'FRAISEUSE', 'ANALYSEUR']
            data = [5000, 26000, 21400, 12000]

            explode = (0, 0.15, 0, 0)
            plt.pie(data, explode=explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
            plt.axis('equal')
            plt.show()

        def aff():
            x = [1, 1, 2, 3, 3, 5, 7, 8, 9, 10,
                 10, 11, 11, 13, 13, 15, 16, 17, 18, 18,
                 18, 19, 20, 21, 21, 23, 24, 24, 25, 25,
                 25, 25, 26, 26, 26, 27, 27, 27, 27, 27,
                 29, 30, 30, 31, 33, 34, 34, 34, 35, 36,
                 36, 37, 37, 38, 38, 39, 40, 41, 41, 42,
                 43, 44, 45, 45, 46, 47, 48, 48, 49, 50,
                 51, 52, 53, 54, 55, 55, 56, 57, 58, 60,
                 61, 63, 64, 65, 66, 68, 70, 71, 72, 74,
                 75, 77, 81, 83, 84, 87, 89, 90, 90, 91
                 ]
            plt.hist(x, bins=10)
            plt.show()


        def quitter():
            user = "Amal"
            messagebox.showinfo("Confirmation","Au revoir "+user)
            windw.destroy()
            time.sleep(1)
            from LoginP.Login import lg
            lg.main_screen()




        def MusicTut():
            mixer.init()
            mixer.music.load('record00.mp3')
            mixer.music.play()
            print("Bienvenue chez Tunisie Telecom")

        def Boitier():
            Frame1 = Frame(windw)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="white")

            tab_parent = ttk.Notebook(Frame1)
            tab1 = ttk.Frame(tab_parent)
            tab2 = ttk.Frame(tab_parent)
            tab_parent.add(tab1, text="Ajouter")
            tab_parent.add(tab2, text="Gérer")
            tab_parent.pack(expand=1, fill='both')

            wrapper1 = LabelFrame(tab2, text="Liste ")
            wrapper2 = LabelFrame(tab2, text="Modification ")

            wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
            wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

            ##########################################################################################

            def Update():
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                c = c.execute('DELETE FROM Boitier WHERE  oid= ' + data.get())

                c.execute("INSERT INTO Boitier VALUES(:v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8)",
                          {'v1': EntryAdresseIPed.get(),
                           'v2': num_seriEntryed.get(),
                           'v3': EntryMarqueed.get(),
                           'v4': EntryPrixed.get(),
                           'v5': Entrydesignationed.get(),
                           'v6': EntryTypeed.get(),
                           'v7': EntryEtateded.get(),
                           'v8': EntryZoneed.get()
                           })

                conn.commit()
                conn.close()

                EntryAdresseIPed.delete(0, END)
                num_seriEntryed.delete(0, END)
                EntryMarqueed.delete(0, END)
                EntryPrixed.delete(0, END)
                Entrydesignationed.delete(0, END)
                EntryTypeed.delete(0, END)
                EntryEtateded.delete(0, END)
                EntryZoneed.delete(0, END)

            def edit():
                editor = Tk()
                editor.title('EDITOR')
                editor.geometry("400x600")

                conn = sqlite3.connect('../BD/data.db')
                c = conn.cursor()
                record_id = data.get()
                c.execute("SELECT * , oid FROM Boitier WHERE oid = " + record_id)
                records = c.fetchall()

                global EntryAdresseIPed
                global num_seriEntryed
                global EntryMarqueed
                global EntryPrixed
                global Entrydesignationed
                global EntryTypeed
                global EntryEtateded
                global EntryZoneed

                Label1 = Label(editor)
                Label1.place(relx=0.05, rely=0.11, height=21, width=100)
                Label1.configure(background="white")
                Label1.configure(disabledforeground="#a3a3a3")
                Label1.configure(foreground="#000000")
                Label1.configure(text='''Adresse IP :''', anchor=W)

                EntryAdresseIPed = Entry(editor)
                EntryAdresseIPed.place(relx=0.22, rely=0.11, height=20, relwidth=0.191)

                Label2 = Label(editor)
                Label2.place(relx=0.05, rely=0.198, height=21, width=100)
                Label2.configure(background="white")
                Label2.configure(disabledforeground="#a3a3a3")
                Label2.configure(foreground="#000000")
                Label2.configure(text='''Marque :''', anchor=W)

                EntryMarqueed = Entry(editor)
                EntryMarqueed.place(relx=0.22, rely=0.286, height=20, relwidth=0.191)

                Label3 = Label(editor)
                Label3.place(relx=0.05, rely=0.286, height=21, width=100)
                Label3.configure(background="white")
                Label3.configure(disabledforeground="#a3a3a3")
                Label3.configure(foreground="#000000")
                Label3.configure(text='''Numéro de série :''', anchor=W)

                num_seriEntryed = Entry(editor)
                num_seriEntryed.place(relx=0.22, rely=0.198, height=20, relwidth=0.191)

                Label4 = Label(editor)
                Label4.place(relx=0.05, rely=0.374, height=21, width=100)
                Label4.configure(background="white")
                Label4.configure(disabledforeground="#a3a3a3")
                Label4.configure(foreground="#000000")
                Label4.configure(text='''Etat :''', anchor=W)

                EntryEtateded = Entry(editor)
                EntryEtateded.place(relx=0.22, rely=0.374, height=20, relwidth=0.191)

                Label5 = Label(editor)
                Label5.place(relx=0.559, rely=0.11, height=21, width=100)
                Label5.configure(background="white")
                Label5.configure(disabledforeground="#a3a3a3")
                Label5.configure(foreground="#000000")
                Label5.configure(text='''Désignation :''', anchor=W)

                Entrydesignationed = Entry(editor)
                Entrydesignationed.place(relx=0.729, rely=0.11, height=20, relwidth=0.191)

                Label6 = Label(editor)
                Label6.place(relx=0.559, rely=0.198, height=21, width=100)
                Label6.configure(background="white")
                Label6.configure(disabledforeground="#a3a3a3")
                Label6.configure(foreground="#000000")
                Label6.configure(text='''Type :''', anchor=W)

                EntryTypeed = Entry(editor)
                EntryTypeed.place(relx=0.729, rely=0.198, height=20, relwidth=0.191)

                Label7 = Label(editor)
                Label7.place(relx=0.559, rely=0.286, height=21, width=100)
                Label7.configure(background="white")
                Label7.configure(disabledforeground="#a3a3a3")
                Label7.configure(foreground="#000000")
                Label7.configure(text='''Zone :''', anchor=W)

                EntryZoneed = Entry(editor)
                EntryZoneed.place(relx=0.729, rely=0.286, height=20, relwidth=0.191)

                Label8 = Label(editor)
                Label8.place(relx=0.559, rely=0.396, height=21, width=99)
                Label8.configure(background="white")
                Label8.configure(disabledforeground="#a3a3a3")
                Label8.configure(foreground="#000000")
                Label8.configure(text='''Prix :''', anchor=W)

                EntryPrixed = Entry(editor)
                EntryPrixed.place(relx=0.729, rely=0.396, height=20, relwidth=0.191)

                for record in records:
                    EntryAdresseIPed.insert(0, record[0]),
                    num_seriEntryed.insert(0, record[1]),
                    EntryMarqueed.insert(0, record[2]),
                    EntryPrixed.insert(0, record[3]),
                    Entrydesignationed.insert(0, record[4]),
                    EntryTypeed.insert(0, record[5]),
                    EntryEtateded.insert(0, record[6]),
                    EntryZoneed.insert(0, record[7]),

                Button1 = Button(editor, background="white", foreground="white", bd=0)
                Button1.place(relx=0.56, rely=0.951, height=30, width=180)
                Button1.configure(text="Enregistrer", command=Update)

            ###########################################################################################

            COLOR_1 = 'white'
            COLOR_2 = 'white'
            COLOR_3 = 'Black'
            COLOR_4 = 'white'
            COLOR_5 = '#FAFAFA'
            COLOR_6 = '#FAFAFA'

            # Notebook Style
            noteStyler = ttk.Style()
            noteStyler.configure("TNotebook", background=COLOR_1, borderwidth=0)
            noteStyler.configure("TNotebook.Tab", background=COLOR_1, foreground=COLOR_3, lightcolor=COLOR_6,
                                 borderwidth=0)
            noteStyler.configure("TFrame", background=COLOR_1, foreground=COLOR_2, borderwidth=0)

            Label1 = Label(tab1)
            Label1.place(relx=0.05, rely=0.11, height=21, width=100)
            Label1.configure(background="white")
            Label1.configure(disabledforeground="#a3a3a3")
            Label1.configure(foreground="#000000")
            Label1.configure(text='''Adresse IP:''', anchor=W)

            EntryAdresseIP = Entry(tab1)
            EntryAdresseIP.place(relx=0.22, rely=0.11, height=20, relwidth=0.191)

            Label2 = Label(tab1)
            Label2.place(relx=0.05, rely=0.198, height=21, width=100)
            Label2.configure(background="white")
            Label2.configure(disabledforeground="#a3a3a3")
            Label2.configure(foreground="#000000")
            Label2.configure(text='''Numéro de série :''', anchor=W)

            num_seriEntry = Entry(tab1)
            num_seriEntry.place(relx=0.22, rely=0.198, height=20, relwidth=0.191)

            Label3 = Label(tab1)
            Label3.place(relx=0.05, rely=0.286, height=21, width=100)
            Label3.configure(background="white")
            Label3.configure(disabledforeground="#a3a3a3")
            Label3.configure(foreground="#000000")
            Label3.configure(text='''Marque :''', anchor=W)

            EntryMarque = Entry(tab1)
            EntryMarque.place(relx=0.22, rely=0.286, height=20, relwidth=0.191)

            Label4 = Label(tab1)
            Label4.place(relx=0.05, rely=0.374, height=21, width=100)
            Label4.configure(background="white")
            Label4.configure(disabledforeground="#a3a3a3")
            Label4.configure(foreground="#000000")
            Label4.configure(text='''Prix :''', anchor=W)

            EntryPrix = Entry(tab1)
            EntryPrix.place(relx=0.22, rely=0.374, height=20, relwidth=0.191)

            Label5 = Label(tab1)
            Label5.place(relx=0.559, rely=0.11, height=21, width=100)
            Label5.configure(background="white")
            Label5.configure(disabledforeground="#a3a3a3")
            Label5.configure(foreground="#000000")
            Label5.configure(text='''Désignation :''', anchor=W)

            Entrydesignation = Entry(tab1)
            Entrydesignation.place(relx=0.729, rely=0.11, height=20, relwidth=0.191)

            Label6 = Label(tab1)
            Label6.place(relx=0.559, rely=0.198, height=21, width=100)
            Label6.configure(background="white")
            Label6.configure(disabledforeground="#a3a3a3")
            Label6.configure(foreground="#000000")
            Label6.configure(text='''Type :''', anchor=W)

            EntryType = Entry(tab1)
            EntryType.place(relx=0.729, rely=0.198, height=20, relwidth=0.191)

            Label7 = Label(tab1)
            Label7.place(relx=0.559, rely=0.286, height=21, width=100)
            Label7.configure(background="white")
            Label7.configure(disabledforeground="#a3a3a3")
            Label7.configure(foreground="#000000")
            Label7.configure(text='''Zone :''', anchor=W)

            EntryZone = Entry(tab1)
            EntryZone.place(relx=0.729, rely=0.286, height=20, relwidth=0.191)

            Label8 = Label(tab1)
            Label8.place(relx=0.559, rely=0.396, height=21, width=99)
            Label8.configure(background="white")
            Label8.configure(disabledforeground="#a3a3a3")
            Label8.configure(foreground="#000000")
            Label8.configure(text='''Etat :''', anchor=W)

            EntryEtat = Entry(tab1)
            EntryEtat.place(relx=0.729, rely=0.396, height=20, relwidth=0.191)

            # create a data base or connect to one
            conn = sqlite3.connect('../BD/data.db')
            # create cursor
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS Boitier(v1 text,
                                                    v2 text ,
                                                    v3 text ,
                                                    v4 text ,
                                                    v5 text ,
                                                    v6 text ,
                                                    v7 text ,
                                                    v8 text );""")

            # commit changes
            conn.commit()
            # close conexion
            conn.close()

            conn = sqlite3.connect('../BD/data.db')
            # create cursor
            c = conn.cursor()

            def submit():
                # create a data base or connect to one
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                c.execute(
                    "INSERT INTO Boitier VALUES(:v1, :v2, :v3, :v4, :v5, :v6, :v7, :v8)",
                    {'v1': EntryAdresseIP.get(),
                     'v2': num_seriEntry.get(),
                     'v3': EntryMarque.get(),
                     'v4': EntryPrix.get(),
                     'v5': Entrydesignation.get(),
                     'v6': EntryType.get(),
                     'v7': EntryEtat.get(),
                     'v8': EntryZone.get()
                     })

                conn.commit()
                # close conexion
                conn.close()

                EntryAdresseIP.delete(0, END)
                num_seriEntry.delete(0, END)
                EntryMarque.delete(0, END)
                EntryPrix.delete(0, END)
                Entrydesignation.delete(0, END)
                EntryType.delete(0, END)
                EntryEtat.delete(0, END)
                EntryZone.delete(0, END)

                # commit changes

            def query():
                # create a data base or connect to one
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                c.execute("SELECT * , oid FROM Boitier")
                records = c.fetchall()
                print(records)

                # loop
                print_records = ''
                for row in records:
                    print(row)  # it print all records in the database
                    tree.insert("", END, values=row)
                conn.close()

            tree = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6, 7, 8), show="headings", height="3")
            tree.pack()
            tree.configure(height=8)
            tree.column("#1", width=60)
            tree.column("#2", width=60)
            tree.column("#3", width=60)
            tree.column("#4", width=60)
            tree.column("#5", width=60)
            tree.column("#6", width=60)
            tree.column("#7", width=60)
            tree.column("#8", width=60)

            tree.heading(1, text="Adresse IP", anchor=W)
            tree.heading(2, text="Num Série", anchor=W)
            tree.heading(3, text="Marque", anchor=W)
            tree.heading(4, text="Prix", anchor=W)
            tree.heading(5, text="Désignation", anchor=W)
            tree.heading(6, text="Type", anchor=W)
            tree.heading(7, text="Zone", anchor=W)
            tree.heading(8, text="Etat", anchor=W)

            tree.pack()

            # create query Button
            query_btn = Button(wrapper1, text="show the base ", command=query)
            query_btn.pack()

            Butto3 = Button(tab1, background="#16A085", foreground="white", bd=0)
            Butto3.place(relx=0.90, rely=0.951, height=20, width=55)
            Butto3.configure(text="Terminer", command=submit)

            data = str(Entry(text="Please enter name: "))

            data = Entry(wrapper2)
            data.place(relx=0.76, rely=0.382, height=20, relwidth=0.186)

            def supprim():
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                lbl1 = Label(wrapper2, text="Connected to SQLite")
                lbl1.pack()
                mydata = c.execute('DELETE FROM Boitier WHERE  oid= ' + data.get())
                conn.commit()
                lb2l = Label(wrapper2, text="Record deleted successfully")
                lb2l.pack()

                conn.close()

            lbl = Label(wrapper2, text="Rechecher")
            lbl.pack(side=LEFT, padx=10)
            btn = Button(wrapper2, text="Supprimer", command=supprim).pack(side=LEFT, padx=10, pady=6)
            btn = Button(wrapper2, text="Modifier", command=edit).pack(side=LEFT, padx=10, pady=7)

            Button1 = Button(tab1, background="#2980B9", foreground="white", bd=0)
            Button1.place(relx=0.96, rely=0.951, height=20, width=20)
            Button1.configure(text="Add", command=submit)

        def Comptes():
            Fruser = Frame(windw)
            Fruser.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Fruser.configure(relief='groove')
            Fruser.configure(borderwidth="0")
            Fruser.configure(relief="groove")
            Fruser.configure(background="white", bd=0)

            COLOR_1 = 'white'
            COLOR_2 = 'white'
            COLOR_3 = 'Black'
            COLOR_4 = 'white'
            COLOR_5 = 'white'
            COLOR_6 = 'white'

            # Notebook Style
            noteStyler = ttk.Style()
            noteStyler.configure("TNotebook", background=COLOR_1, borderwidth=0)
            noteStyler.configure("TNotebook.Tab", background=COLOR_1, foreground=COLOR_3, lightcolor=COLOR_6,
                                 borderwidth=0)
            noteStyler.configure("TFrame", background=COLOR_1, foreground=COLOR_2, borderwidth=0)

            tab_parent = ttk.Notebook(Fruser)
            tab1 = ttk.Frame(tab_parent)
            tab2 = ttk.Frame(tab_parent)
            tab_parent.add(tab1, text="Ajouter")
            tab_parent.add(tab2, text="Gérer")
            tab_parent.pack(expand=1, fill='both')

            wrapper1 = LabelFrame(tab2, text="Customer List")
            wrapper2 = LabelFrame(tab2, text="Search")

            wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
            wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)

            Labelframe12 = LabelFrame(tab1)
            Labelframe12.place(relx=0.012, rely=0.0, relheight=0.099
                               , relwidth=0.185)
            Labelframe12.configure(relief='solid')
            Labelframe12.configure(foreground="black")
            Labelframe12.configure(text='''Utilisateur''')
            Labelframe12.configure(background="white")

            Label1 = Label(tab1)
            Label1.place(relx=0.089, rely=0.203, height=21, width=100)
            Label1.configure(background="white")
            Label1.configure(disabledforeground="#a3a3a3")
            Label1.configure(foreground="#000000")
            Label1.configure(text='''Identifiant''', anchor=W)

            Label2 = Label(tab1)
            Label2.place(relx=0.089, rely=0.303, height=21, width=100)
            Label2.configure(background="white")
            Label2.configure(disabledforeground="#a3a3a3")
            Label2.configure(foreground="#000000")
            Label2.configure(text='''Nom''', anchor=W)

            Label3 = Label(tab1)
            Label3.place(relx=0.089, rely=0.403, height=21, width=100)
            Label3.configure(background="white")
            Label3.configure(disabledforeground="#a3a3a3")
            Label3.configure(foreground="#000000")
            Label3.configure(text='''Prénom''', anchor=W)

            Label4 = Label(tab1)
            Label4.place(relx=0.089, rely=0.503, height=21, width=100)
            Label4.configure(background="white")
            Label4.configure(disabledforeground="#a3a3a3")
            Label4.configure(foreground="#000000")
            Label4.configure(text='''Mot de passe''', anchor=W)

            Label5 = Label(tab1)
            Label5.place(relx=0.092, rely=0.603, height=21, width=100)
            Label5.configure(background="white")
            Label5.configure(disabledforeground="#a3a3a3")
            Label5.configure(foreground="#000000")
            Label5.configure(text='''Type''', anchor=W)

            Label6 = Label(tab1)
            Label6.place(relx=0.092, rely=0.703, height=21, width=100)
            Label6.configure(background="white")
            Label6.configure(disabledforeground="#a3a3a3")
            Label6.configure(foreground="#000000")
            Label6.configure(text='''Login''', anchor=W)

            Entry1 = Entry(tab1)
            Entry1.place(relx=0.296, rely=0.203, height=20, relwidth=0.198)

            Entry2 = Entry(tab1)
            Entry2.place(relx=0.296, rely=0.303, height=20, relwidth=0.198)

            Entry3 = Entry(tab1)
            Entry3.place(relx=0.296, rely=0.403, height=20, relwidth=0.198)

            Entry4 = Entry(tab1)
            Entry4.place(relx=0.296, rely=0.503, height=20, relwidth=0.198)

            Entry5 = Entry(tab1)
            Entry5.place(relx=0.296, rely=0.603, height=20, relwidth=0.191)

            Entry6 = Entry(tab1)
            Entry6.place(relx=0.296, rely=0.703, height=20, relwidth=0.198)

            nom = Entry1.get()
            prenom = Entry2.get()
            mdp = Entry3.get()
            matr = Entry4.get()
            typ = Entry5.get()
            login = Entry6.get()

            # create a data base or connect to one
            conn = sqlite3.connect('../BD/data.db')
            # create cursor
            c = conn.cursor()
            c.execute(""" CREATE TABLE IF NOT EXISTS Utilisateur(
                                             v1 text ,
                                             v2 text ,
                                             v3 text ,
                                             v4 text ,
                                             v5 text ,
                                             v6 text ,
                                             v7 text )""")
            # commit changes
            conn.commit()
            # close conexion
            conn.close()

            def submit():
                l = ['admin', 'tech', 'cont']
                if Entry5.get() in l:
                    # create a data base or connect to one
                    conn = sqlite3.connect('../BD/data.db')
                    # create cursor
                    c = conn.cursor()
                    c.execute("INSERT INTO Utilisateur VALUES(:v1, :v2, :v3, :v4, :v5, :v6, :v7)",
                              {'v1': Entry1.get(),
                               'v2': Entry2.get(),
                               'v3': Entry3.get(),
                               'v4': Entry4.get(),
                               'v5': Entry5.get(),
                               'v6': Entry5.get(),
                               'v7': Entry6.get()
                               })
                    # commit changes
                    conn.commit()
                    messagebox.showinfo("Info","Votre utulisateur est bien ajoute")
                    # close conexion
                    Entry1.delete(0, END)
                    Entry2.delete(0, END)
                    Entry3.delete(0, END)
                    Entry4.delete(0, END)
                    Entry5.delete(0, END)
                    Entry6.delete(0, END)
                    conn.close()
                else:
                    messagebox.showwarning('','Verifier le Type inserer')
            Button1 = Button(tab1, background="#2980B9", foreground="white", bd=0)
            Button1.place(relx=0.96, rely=0.951, height=20, width=20)
            Button1.configure(text="+", command=submit)

            def query():
                # create a data base or connect to one
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                c.execute("SELECT * , oid FROM Utilisateur")
                records = c.fetchall()
                print(records)

                # loop
                print_records = ''
                for row in records:
                    print(row)  # it print all records in the database
                    tree.insert("", END, values=row)
                conn.close()

            tree = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4, 5, 6), show="headings", height="3")
            tree.pack()
            tree.configure(height=8)
            tree.column("#0", width=200)
            tree.column("#1", width=130)
            tree.column("#2", width=130)
            tree.column("#3", width=130)
            tree.column("#4", width=130)
            tree.column("#5", width=130)
            tree.column("#6", width=130)

            tree.heading(0, text="Id", anchor=W)
            tree.heading(1, text="Identifiant", anchor=W)
            tree.heading(2, text="Nom", anchor=W)
            tree.heading(3, text="Prénom", anchor=W)
            tree.heading(4, text="Mot de passe", anchor=W)
            tree.heading(5, text="Type", anchor=W)
            tree.heading(6, text="Login", anchor=W)
            tree.pack()

            query_btn = Button(wrapper1, text="show the base ", command=query)
            query_btn.pack()

            data3 = str(Entry(text="Please enter the Id: "))

            data3 = Entry(wrapper2)
            data3.place(relx=0.76, rely=0.382, height=20, relwidth=0.186)

            def supprim():
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                lbl1 = Label(wrapper2, text="Connected to SQLite")
                lbl1.pack()
                mydata = c.execute('DELETE FROM Utilisateur WHERE  oid= ' + data3.get())
                conn.commit()
                lb2l = Label(wrapper2, text="Record deleted successfully")
                lb2l.pack()

                conn.close()

            def Update():
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                c = c.execute('DELETE FROM Utilisateur WHERE  oid= ' + data3.get())

                c.execute("INSERT INTO Utilisateur VALUES(:v1, :v2, :v3, :v4, :v5, :v6, :v7)",
                          {'v1': Entry1ed.get(),
                           'v2': Entry2ed.get(),
                           'v3': Entry3ed.get(),
                           'v4': Entry4ed.get(),
                           'v5': Entry5ed.get(),
                           'v6': Entry5ed.get(),
                           'v7': Entry6ed.get()
                           })

                conn.commit()
                conn.close()

                Entry1ed.delete(0, END)
                Entry2ed.delete(0, END)
                Entry3ed.delete(0, END)
                Entry4ed.delete(0, END)
                Entry5ed.delete(0, END)
                Entry6ed.delete(0, END)

            def edit():
                editor = Tk()
                editor.title('EDITOR')
                editor.geometry("400x600")

                conn = sqlite3.connect('../BD/data.db')
                c = conn.cursor()
                record_id = data3.get()
                c.execute("SELECT * , oid FROM Utilisateur WHERE oid = " + record_id)
                records = c.fetchall()

                global Entry1ed
                global Entry2ed
                global Entry3ed
                global Entry4ed
                global Entry5ed
                global Entry6ed

                Label1 = Label(editor)
                Label1.place(relx=0.089, rely=0.203, height=21, width=100)
                Label1.configure(background="#FAFAFA")
                Label1.configure(disabledforeground="#a3a3a3")
                Label1.configure(foreground="#000000")
                Label1.configure(text='''Identifiant''', anchor=W)

                Label2 = Label(editor)
                Label2.place(relx=0.089, rely=0.303, height=21, width=100)
                Label2.configure(background="#FAFAFA")
                Label2.configure(disabledforeground="#a3a3a3")
                Label2.configure(foreground="#000000")
                Label2.configure(text='''Nom''', anchor=W)

                Label3 = Label(editor)
                Label3.place(relx=0.089, rely=0.403, height=21, width=100)
                Label3.configure(background="#FAFAFA")
                Label3.configure(disabledforeground="#a3a3a3")
                Label3.configure(foreground="#000000")
                Label3.configure(text='''Prénom''', anchor=W)

                Label4 = Label(editor)
                Label4.place(relx=0.089, rely=0.503, height=21, width=100)
                Label4.configure(background="#FAFAFA")
                Label4.configure(disabledforeground="#a3a3a3")
                Label4.configure(foreground="#000000")
                Label4.configure(text='''Mot de passe''', anchor=W)

                Label5 = Label(editor)
                Label5.place(relx=0.092, rely=0.603, height=21, width=100)
                Label5.configure(background="#FAFAFA")
                Label5.configure(disabledforeground="#a3a3a3")
                Label5.configure(foreground="#000000")
                Label5.configure(text='''Type''', anchor=W)

                Label6 = Label(editor)
                Label6.place(relx=0.092, rely=0.703, height=21, width=100)
                Label6.configure(background="#FAFAFA")
                Label6.configure(disabledforeground="#a3a3a3")
                Label6.configure(foreground="#000000")
                Label6.configure(text='''Login''', anchor=W)

                Entry1ed = Entry(editor)
                Entry1ed.place(relx=0.296, rely=0.203, height=20, relwidth=0.198)

                Entry2ed = Entry(editor)
                Entry2ed.place(relx=0.296, rely=0.303, height=20, relwidth=0.198)

                Entry3ed = Entry(editor)
                Entry3ed.place(relx=0.296, rely=0.403, height=20, relwidth=0.198)

                Entry4ed = Entry(editor)
                Entry4ed.place(relx=0.296, rely=0.503, height=20, relwidth=0.198)

                Entry5ed = Entry(editor)
                Entry5ed.place(relx=0.296, rely=0.603, height=20, relwidth=0.191)

                Entry6ed = Entry(editor)
                Entry6ed.place(relx=0.296, rely=0.703, height=20, relwidth=0.198)

                for record in records:
                    Entry1ed.insert(0, record[0])
                    Entry2ed.insert(0, record[1])
                    Entry3ed.insert(0, record[2])
                    Entry4ed.insert(0, record[3])
                    Entry5ed.insert(0, record[4])
                    Entry6ed.insert(0, record[5])

                    Button1 = Button(editor, background="white", foreground="white", bd=0)
                    Button1.place(relx=0.416, rely=0.915, height=31, width=209)
                    Button1.configure(text="Enregistrer", command=Update)

            lbl = Label(wrapper2, text="Rechecher")
            lbl.pack(side=LEFT, padx=10)
            btn = Button(wrapper2, text="Supprimer", command=supprim).pack(side=LEFT, padx=10, pady=6)

            lbl.pack(side=LEFT, padx=10)
            btn = Button(wrapper2, text="Modifier", command=edit).pack(side=LEFT, padx=10, pady=7)

        ##########################################################################

        def Stat():
            Frame1 = Frame(windw)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="#FFFFFF")

            Labelframe1 = LabelFrame(Frame1)
            Labelframe1.place(relx=0.061, rely=0.071, relheight=0.271
                              , relwidth=0.382)
            Labelframe1.configure(relief='ridge')
            Labelframe1.configure(foreground="black")
            Labelframe1.configure(text='''Indicateur de la quantité des interventions''')
            Labelframe1.configure(background="#FFFFFF")

            Button1 = Button(Labelframe1)
            Button1.place(relx=0.683, rely=0.696, height=25, width=76
                          , bordermode='ignore')
            Button1.configure(takefocus="")
            Button1.configure(text="Afficher", background="#8D5F72", command=f1)

            Message1 = Message(Labelframe1)
            Message1.place(relx=0.04, rely=0.348, relheight=0.548
                           , relwidth=0.643, bordermode='ignore')
            Message1.configure(background="#FFFFFF")
            Message1.configure(foreground="#000000")
            Message1.configure(highlightbackground="#E5E7E9")
            Message1.configure(highlightcolor="black")
            Message1.configure(
                text='''Evolution d’indicateur de la quantité des interventions curative En analysant tous les boitiers''')
            Message1.configure(width=160)

            Labelframe2 = LabelFrame(Frame1)
            Labelframe2.place(relx=0.061, rely=0.353, relheight=0.271
                              , relwidth=0.382)
            Labelframe2.configure(relief='ridge')
            Labelframe2.configure(foreground="black")
            Labelframe2.configure(text='''Consommation de réseau ''')
            Labelframe2.configure(background="#FFFFFF")

            Button2 = Button(Labelframe2)
            Button2.place(relx=0.683, rely=0.696, height=25, width=76
                          , bordermode='ignore')
            Button2.configure(takefocus="")
            Button2.configure(text="Afficher", background="#8D5F72", command=aff)

            Message2 = Message(Labelframe2)
            Message2.place(relx=0.04, rely=0.261, relheight=0.635
                           , relwidth=0.643, bordermode='ignore')
            Message2.configure(background="#FFFFFF")
            Message2.configure(foreground="#000000")
            Message2.configure(highlightbackground="#E5E7E9")
            Message2.configure(highlightcolor="black")
            Message2.configure(
                text='''Cet indicateur nous permit de détecter et d’estimer le taux de consommation pour chaque région.''')
            Message2.configure(width=160)

            Labelframe3 = LabelFrame(Frame1)
            Labelframe3.place(relx=0.552, rely=0.071, relheight=0.271
                              , relwidth=0.383)
            Labelframe3.configure(relief='ridge')
            Labelframe3.configure(foreground="black")
            Labelframe3.configure(text='''Indicateur d’efficacité''')
            Labelframe3.configure(background="#FFFFFF")

            Button3 = Button(Labelframe3)
            Button3.place(relx=0.68, rely=0.696, height=25, width=76
                          , bordermode='ignore')
            Button3.configure(takefocus="")
            Button3.configure(text="Afficher", background="#8D5F72", command=f3)

            Message3 = Message(Labelframe3)
            Message3.place(relx=0.04, rely=0.174, relheight=0.722, relwidth=0.64
                           , bordermode='ignore')
            Message3.configure(background="#FFFFFF")
            Message3.configure(foreground="#000000")
            Message3.configure(highlightbackground="#E5E7E9")
            Message3.configure(highlightcolor="black")
            Message3.configure(
                text='''Cet indicateur permet d’évaluer le bon fonctionnement en réduisant les pannes et les arrêts boitiers.''')
            Message3.configure(width=160)

            Labelframe4 = LabelFrame(Frame1)
            Labelframe4.place(relx=0.552, rely=0.353, relheight=0.247
                              , relwidth=0.383)
            Labelframe4.configure(relief='ridge')
            Labelframe4.configure(foreground="black")
            Labelframe4.configure(text='''Indicateur de fiabilisation''')
            Labelframe4.configure(background="#FFFFFF")

            Button4 = Button(Labelframe4)
            Button4.place(relx=0.68, rely=0.667, height=25, width=76
                          , bordermode='ignore')
            Button4.configure(takefocus="")
            Button4.configure(text="Afficher", background="#8D5F72", command=f4)

            Message4 = Message(Labelframe4)
            Message4.place(relx=0.04, rely=0.19, relheight=0.695, relwidth=0.64
                           , bordermode='ignore')
            Message4.configure(background="#FFFFFF")
            Message4.configure(foreground="#000000")
            Message4.configure(highlightbackground="#E5E7E9")
            Message4.configure(highlightcolor="black")
            Message4.configure(text='''Cet indicateur permet d’évaluer l’indisponibilité et les arrêts des boitiers.''')
            Message4.configure(width=160)

            Labelframe5 = LabelFrame(Frame1)
            Labelframe5.place(relx=0.270, rely=0.640, relheight=0.294
                              , relwidth=0.383)
            Labelframe5.configure(relief='ridge')
            Labelframe5.configure(foreground="black")
            Labelframe5.configure(text='''Indicateur de compétence''')
            Labelframe5.configure(background="#FFFFFF")

            Button5 = Button(Labelframe5)
            Button5.place(relx=0.68, rely=0.72, height=25, width=76
                          , bordermode='ignore')
            Button5.configure(takefocus="", background="#8D5F72")
            Button5.configure(text="Afficher", command=f5)

            Message5 = Message(Labelframe5)
            Message5.place(relx=0.04, rely=0.24, relheight=0.664, relwidth=0.64
                           , bordermode='ignore')
            Message5.configure(background="#FFFFFF")
            Message5.configure(foreground="#000000")
            Message5.configure(highlightbackground="#E5E7E9")
            Message5.configure(highlightcolor="black")
            Message5.configure(
                text='''le service met en place un indicateur de compétence pour suivre l’état des boitiers fixant comme objectif de diminuer cet indicateur''')
            Message5.configure(width=160)

        def Intervention():
            Fruser = Frame(windw)
            Fruser.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Fruser.configure(relief='groove')
            Fruser.configure(borderwidth="0")
            Fruser.configure(relief="groove")
            Fruser.configure(background="white", bd=0)

            COLOR_1 = 'white'
            COLOR_2 = 'white'
            COLOR_3 = 'Black'
            COLOR_4 = 'white'
            COLOR_5 = 'white'
            COLOR_6 = 'white'

            # Notebook Style
            noteStyler = ttk.Style()
            noteStyler.configure("TNotebook", background=COLOR_1, borderwidth=0)
            noteStyler.configure("TNotebook.Tab", background=COLOR_1, foreground=COLOR_3, lightcolor=COLOR_6,
                                 borderwidth=0)
            noteStyler.configure("TFrame", background=COLOR_1, foreground=COLOR_2, borderwidth=0)

            tab_parent = ttk.Notebook(Fruser)
            tab1 = ttk.Frame(tab_parent)
            tab2 = ttk.Frame(tab_parent)
            tab_parent.add(tab1, text="Ajouter")
            tab_parent.add(tab2, text="Gérer")
            tab_parent.pack(expand=1, fill='both')


            wrapper1 = LabelFrame(tab2, text="Customer List")
            wrapper2 = LabelFrame(tab2, text="Search")


            wrapper1.pack(fill="both", expand="yes", padx=20, pady=10)
            wrapper2.pack(fill="both", expand="yes", padx=20, pady=10)


            Labelframe12 = LabelFrame(tab1)
            Labelframe12.place(relx=0.012, rely=0.0, relheight=0.099
                               , relwidth=0.185)
            Labelframe12.configure(relief='solid')
            Labelframe12.configure(foreground="black")
            Labelframe12.configure(text='''Intervention ''')
            Labelframe12.configure(background="white")


            Label1 = Label(tab1)
            Label1.place(relx=0.089, rely=0.203, height=21, width=100)
            Label1.configure(background="white")
            Label1.configure(disabledforeground="#a3a3a3")
            Label1.configure(foreground="#000000")
            Label1.configure(text='''Zone :''', anchor=W)

            Label2 = Label(tab1)
            Label2.place(relx=0.089, rely=0.303, height=21, width=100)
            Label2.configure(background="white")
            Label2.configure(disabledforeground="#a3a3a3")
            Label2.configure(foreground="#000000")
            Label2.configure(text='''Temps :''', anchor=W)

            Label3 = Label(tab1)
            Label3.place(relx=0.089, rely=0.403, height=21, width=100)
            Label3.configure(background="white")
            Label3.configure(disabledforeground="#a3a3a3")
            Label3.configure(foreground="#000000")
            Label3.configure(text='''Type :''', anchor=W)

            Entry1 = Entry(tab1)
            Entry1.place(relx=0.296, rely=0.203, height=20, relwidth=0.198)

            Entry2 = Entry(tab1)
            Entry2.place(relx=0.296, rely=0.303, height=20, relwidth=0.198)

            Entry3 = Entry(tab1)
            Entry3.place(relx=0.296, rely=0.403, height=20, relwidth=0.198)

            nom = Entry1.get()
            prenom = Entry2.get()
            mdp = Entry3.get()

            # create a data base or connect to one
            conn = sqlite3.connect('../BD/data.db')
            # create cursor
            c = conn.cursor()
            c.execute(""" CREATE TABLE IF NOT EXISTS Intervention(
                                             v1 text ,
                                             v2 text ,
                                             v3 text  )""")
            # commit changes
            conn.commit()
            # close conexion
            conn.close()

            def submit():
                # create a data base or connect to one
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()
                c.execute("INSERT INTO Intervention VALUES(:v1, :v2, :v3)",
                          {'v1': Entry1.get(),
                           'v2': Entry2.get(),
                           'v3': Entry3.get(),
                           })
                # commit changes
                conn.commit()
                messagebox.showinfo("Info", "Votre Intervention est bien ajoute")
                # close conexion
                Entry1.delete(0, END)
                Entry2.delete(0, END)
                Entry3.delete(0, END)
                conn.close()

            Button1 = Button(tab1, background="#2980B9", foreground="white", bd=0)
            Button1.place(relx=0.96, rely=0.951, height=20, width=20)
            Button1.configure(text="+", command=submit)

            def query():
                # create a data base or connect to one
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                c.execute("SELECT * , oid FROM Intervention")
                records = c.fetchall()
                print(records)

                # loop
                print_records = ''
                for row in records:
                    print(row)  # it print all records in the database
                    tree.insert("", END, values=row)
                conn.close()

            tree = ttk.Treeview(wrapper1, columns=(1, 2, 3, 4), show="headings", height="3")
            tree.pack()
            tree.configure(height=8)
            tree.column("#0", width=200)
            tree.column("#1", width=130)
            tree.column("#2", width=130)
            tree.column("#3", width=130)


            tree.heading(1, text="Zone ", anchor=W)
            tree.heading(2, text="Temps", anchor=W)
            tree.heading(3, text="Type ", anchor=W)
            tree.heading(4, text="Id ", anchor=W)

            tree.pack()

            query_btn = Button(wrapper1, text="show the base ", command=query)
            query_btn.pack()

            data3 = str(Entry(text="Please enter the Id: "))

            data3 = Entry(wrapper2)
            data3.place(relx=0.76, rely=0.382, height=20, relwidth=0.186)

            def supprim():
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                lbl1 = Label(wrapper2, text="Connected to SQLite")
                lbl1.pack()
                mydata = c.execute('DELETE FROM Intervention WHERE  oid= ' + data3.get())
                conn.commit()
                lb2l = Label(wrapper2, text="Record deleted successfully")
                lb2l.pack()

                conn.close()

            def Update():
                conn = sqlite3.connect('../BD/data.db')
                # create cursor
                c = conn.cursor()

                c = c.execute('DELETE FROM Intervention WHERE  oid= ' + data3.get())

                c.execute("INSERT INTO Intervention VALUES(:v1, :v2, :v3)",
                          {'v1': Entry1ed.get(),
                           'v2': Entry2ed.get(),
                           'v3': Entry3ed.get()
                           })

                conn.commit()
                conn.close()

                Entry1ed.delete(0, END)
                Entry2ed.delete(0, END)
                Entry3ed.delete(0, END)

            def edit():
                editor = Tk()
                editor.title('EDITOR')
                editor.geometry("400x600")

                conn = sqlite3.connect('../BD/data.db')
                c = conn.cursor()
                record_id = data3.get()
                c.execute("SELECT * , oid FROM Intervention WHERE oid = " + record_id)
                records = c.fetchall()

                global Entry1ed
                global Entry2ed
                global Entry3ed

                Label1 = Label(editor)
                Label1.place(relx=0.089, rely=0.203, height=21, width=100)
                Label1.configure(background="#FAFAFA")
                Label1.configure(disabledforeground="#a3a3a3")
                Label1.configure(foreground="#000000")
                Label1.configure(text='''Zone''', anchor=W)

                Label2 = Label(editor)
                Label2.place(relx=0.089, rely=0.303, height=21, width=100)
                Label2.configure(background="#FAFAFA")
                Label2.configure(disabledforeground="#a3a3a3")
                Label2.configure(foreground="#000000")
                Label2.configure(text='''Temps''', anchor=W)

                Label3 = Label(editor)
                Label3.place(relx=0.089, rely=0.403, height=21, width=100)
                Label3.configure(background="#FAFAFA")
                Label3.configure(disabledforeground="#a3a3a3")
                Label3.configure(foreground="#000000")
                Label3.configure(text='''Type''', anchor=W)


                Entry1ed = Entry(editor)
                Entry1ed.place(relx=0.296, rely=0.203, height=20, relwidth=0.198)

                Entry2ed = Entry(editor)
                Entry2ed.place(relx=0.296, rely=0.303, height=20, relwidth=0.198)

                Entry3ed = Entry(editor)
                Entry3ed.place(relx=0.296, rely=0.403, height=20, relwidth=0.198)


                for record in records:
                    Entry1ed.insert(0, record[0])
                    Entry2ed.insert(0, record[1])
                    Entry3ed.insert(0, record[2])

                SaveBtn = Button(editor)
                SaveBtn.place(relx=0.416, rely=0.915, height=31, width=209)
                SaveBtn.configure(text="enregistrer",bg="white",foreground="black")
                SaveBtn.configure(command=Update)


            lbl = Label(wrapper2, text="Rechecher")
            lbl.pack(side=LEFT, padx=10)
            btn = Button(wrapper2, text="Supprimer", command=supprim).pack(side=LEFT, padx=10, pady=6)

            lbl.pack(side=LEFT, padx=10)
            btn = Button(wrapper2, text="Modifier", command=edit).pack(side=LEFT, padx=10, pady=7)

        menubar = Menu(windw)
        windw.config(menu=menubar)
        menufichier = Menu(menubar, tearoff=1)  # pour que activer ou nn voir si en mettre =0
        menubar.add_cascade(label="Fichier", menu=menufichier)
        menufichier.add_command(label="Exit TT",command=quitter)
        menuedition = Menu(menubar, tearoff=1)
        menubar.add_cascade(label="Edition", menu=menufichier)

        windw.BTN1 = Button(windw, text="azert")
        imCmpt = PhotoImage(file="../Images/Gcmpt.PNG")
        windw.BTN1.place(relx=0.099, rely=0.292, height=30, width=130)
        windw.BTN1.configure(activebackground="#ececec")
        windw.BTN1.configure(activeforeground="#000000")
        windw.BTN1.configure(background="#d9d9d9")
        windw.BTN1.configure(disabledforeground="#a3a3a3")
        windw.BTN1.configure(foreground="#000000")
        windw.BTN1.configure(highlightbackground="#d9d9d9")
        windw.BTN1.configure(highlightcolor="black")
        windw.BTN1.configure(pady="0")
        windw.BTN1.configure(image=imCmpt, border=0)
        windw.BTN1.configure(command=Comptes)

        windw.BTN2 = Button(windw)
        imStat = PhotoImage(file="../Images/GStat.PNG")
        windw.BTN2.place(relx=0.099, rely=0.415, height=30, width=130)
        windw.BTN2.configure(activebackground="#ececec")
        windw.BTN2.configure(activeforeground="#000000")
        windw.BTN2.configure(background="#d9d9d9")
        windw.BTN2.configure(disabledforeground="#a3a3a3")
        windw.BTN2.configure(foreground="#000000")
        windw.BTN2.configure(highlightbackground="#d9d9d9")
        windw.BTN2.configure(highlightcolor="black")
        windw.BTN2.configure(pady="0")
        windw.BTN2.configure(image=imStat, border=0)
        windw.BTN2.configure(command=Stat)

        windw.BTN3 = Button(windw)
        imBoit = PhotoImage(file="../Images/GBoitier.PNG")
        windw.BTN3.place(relx=0.099, rely=0.558, height=30, width=130)
        windw.BTN3.configure(activebackground="#ececec")
        windw.BTN3.configure(activeforeground="#000000")
        windw.BTN3.configure(background="#d9d9d9")
        windw.BTN3.configure(disabledforeground="#a3a3a3")
        windw.BTN3.configure(foreground="#000000")
        windw.BTN3.configure(highlightbackground="#d9d9d9")
        windw.BTN3.configure(highlightcolor="black")
        windw.BTN3.configure(pady="0")
        windw.BTN3.configure(image=imBoit, border=0)
        windw.BTN3.configure(command=Boitier)

        windw.BTN4 = Button(windw)
        imInter = PhotoImage(file="../Images/GInter.PNG")
        windw.BTN4.place(relx=0.099, rely=0.69, height=30, width=130)
        windw.BTN4.configure(activebackground="#ececec")
        windw.BTN4.configure(activeforeground="#000000")
        windw.BTN4.configure(background="#d9d9d9")
        windw.BTN4.configure(disabledforeground="#a3a3a3")
        windw.BTN4.configure(foreground="#000000")
        windw.BTN4.configure(highlightbackground="#d9d9d9")
        windw.BTN4.configure(highlightcolor="black")
        windw.BTN4.configure(pady="0")
        windw.BTN4.configure(image=imInter, border=0)
        windw.BTN4.configure(command=Intervention)

        windw.BTN7 = Button(windw)
        imSound = PhotoImage(file="../Images/Audio.PNG")
        windw.BTN7.place(relx=0.9459, rely=0.027, height=30, width=30)
        windw.BTN7.configure(activebackground="#ececec")
        windw.BTN7.configure(activeforeground="#000000")
        windw.BTN7.configure(background="#d9d9d9")
        windw.BTN7.configure(disabledforeground="#a3a3a3")
        windw.BTN7.configure(foreground="#000000")
        windw.BTN7.configure(highlightbackground="#d9d9d9")
        windw.BTN7.configure(highlightcolor="black")
        windw.BTN7.configure(pady="0")
        windw.BTN7.configure(image=imSound, border=0)
        windw.BTN7.configure(command=MusicTut)

        # windw.config(menu=menubar)
        windw.mainloop()

    maininterface()