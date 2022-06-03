import time
from tkinter import *
import webbrowser
from tkinter import messagebox
import connection
import sqlite3


class lg:

    def main_screen():
        windw = Tk()
        windw.geometry("1041x588")
        windw.maxsize(1041, 588)
        windw.minsize(1041, 588)
        windw.title("Bienvenu Chez Notre Application")
        windw.iconbitmap("tt.ico")
        background_image = PhotoImage(file='../Images/LoginVF.PNG')
        background_label = Label(windw, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        def login_sucess(verif):
            def destW():
                windw.destroy()

            def Control():
                from ControlerP.Controler import Cntrl
                Cntrl().mainC()

            def techc():
                from TechnicienP.Technicien import test2
                test2().mainT()

            def adminc():
                from AdminP.Admin import Adc



            if verif == 2:
                conn = sqlite3.connect('../BD/data.db')
                cur = conn.cursor()
                cur.execute(
                    " select distinct v2 from Utilisateur where v7 ='" + username1 + "' and v4 ='" + password1 + "';")
                name = cur.fetchone()
                conn.commit()
                conn.close()
                messagebox.showinfo("Welcome", "Bienvenue cher Technicien: "+name[0])
                destW()
                print("windw est destroy")
                time.sleep(1)
                print("1 s   est passee")
                techc()
            if verif == 1:
                conn = sqlite3.connect('../BD/data.db')
                cur = conn.cursor()
                cur.execute(
                    " select distinct v2 from Utilisateur where v7 ='" + username1 + "' and v4 ='" + password1 + "';")
                name = cur.fetchone()
                conn.commit()
                conn.close()
                messagebox.showinfo("Welcome", "Bienvenue cher Administrateur: "+name[0])
                destW()
                print("windw est destroy")
                time.sleep(1)
                print("1 s   est passee")
                adminc()
            if verif == 3:
                conn = sqlite3.connect('../BD/data.db')
                cur = conn.cursor()
                cur.execute(
                    " select distinct v2 from Utilisateur where v7 ='" + username1 + "' and v4 ='" + password1 + "';")
                name = cur.fetchone()
                conn.commit()
                conn.close()
                messagebox.showinfo("Welcome", "Bienvenue cher Controlleur : "+name[0])
                destW()
                print("windw est destroy")
                time.sleep(1)
                print("1 s   est passee")
                Control()

        def login_verify():
            global username1
            global password1
            username1 = Entry1.get()
            password1 = Entry2.get()

            print('email')
            print(username1)
            print('password')
            print(password1)
            Entry1.delete(0, END)
            Entry2.delete(0, END)

            ###############################################################

            try:
                conn = sqlite3.connect('../BD/data.db')
                cur = conn.cursor()
                cur.execute(
                    " select distinct v6 from Utilisateur where v7 ='" + username1 + "' and v4 ='" + password1 + "';")
                role = cur.fetchone()
                conn.commit()
                conn.close()
                global verif
                verif = role[0]
                print("-----------------------")
                print(role)
                print("-----------------------")
                print(role[0])

                l = ['admin', 'tech', 'cont']
                if role[0] in l:
                    if role[0] == l[0]:
                        login_sucess(1)
                    if role[0] == l[1]:
                        login_sucess(2)
                    if role[0] == l[2]:
                        login_sucess(3)


            except:
                   if role == None:
                       messagebox.showwarning("", "Verifier Votre Saisie")



###############################################################

###################################################

        def siteWeb():
            webbrowser.open("https://www.tunisietelecom.tn")
            print("ok")

        LgImg = PhotoImage(file="../Images/Connexion.png")
        bConnexin = Button(windw)
        bConnexin.place(relx=0.593, rely=0.80, height=33, width=174)
        bConnexin.configure(activebackground="#ececec")
        bConnexin.configure(activeforeground="#000000")
        bConnexin.configure(background="#d9d9d9")
        bConnexin.configure(disabledforeground="#a3a3a3")
        bConnexin.configure(foreground="#000000")
        bConnexin.configure(highlightbackground="#d9d9d9")
        bConnexin.configure(highlightcolor="black")
        bConnexin.configure(pady="0", bd=0)
        bConnexin.configure(image=LgImg)
        bConnexin.configure(command=login_verify)

        Aide = PhotoImage(file="../Images/Aide.png")
        bAide = Button(windw)
        bAide.place(relx=0.92, rely=0.91, height=22, width=60)
        bAide.configure(activebackground="#ececec")
        bAide.configure(activeforeground="#000000")
        bAide.configure(background="#d9d9d9")
        bAide.configure(disabledforeground="#a3a3a3")
        bAide.configure(foreground="#000000")
        bAide.configure(highlightbackground="#d9d9d9")
        bAide.configure(highlightcolor="black")
        bAide.configure(pady="0", bd=0)
        bAide.configure(image=Aide)
        bAide.configure(command=siteWeb)

        Entry1 = Entry(windw)
        Entry1.place(relx=0.61, rely=0.453, height=30, relwidth=0.170)
        Entry1.configure(background="#EBDEF0")
        Entry1.configure(disabledforeground="#a3a3a3", bd=0)
        Entry1.configure(font="TkFixedFont")
        Entry1.configure(foreground="#000000")
        Entry1.configure(insertbackground="black")
        Entry1.insert(0, ' Identifiant ')

        Entry2 = Entry(windw)
        Entry2.place(relx=0.61, rely=0.646, height=30, relwidth=0.170)
        Entry2.configure(background="#EBDEF0")
        Entry2.configure(disabledforeground="#a3a3a3", bd=0)
        Entry2.configure(font="TkFixedFont")
        Entry2.configure(foreground="#000000")
        Entry2.configure(insertbackground="black", show="*")
        Entry2.insert(0, ' Mot de Passe')

        status = Label(windw, text="copyright .. all rights reserved © 2021  By Fersi Amal  ", bd=2, relief=RIDGE,
                       anchor=W)
        status.pack(side=BOTTOM, fill=X)

        windw.mainloop()

    main_screen()
