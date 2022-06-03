from tkinter import *
import matplotlib.pyplot as plt
import sqlite3
import random
import tkinter.ttk as ttk
import numpy as np

class Cntrl:
    def mainC():
        windwC = Tk()
        windwC.geometry("1300x650")
        windwC.minsize(1300,650)
        windwC.maxsize(1300,650)
        windwC.title("Interface contrôleur ")
        windwC.iconbitmap("tt.ico")
        background_image = PhotoImage(file='../Images/img.PNG')
        background_label = Label(windwC, image=background_image)
        background_label.place(relwidth=1, relheight=1)

        def suivi():
            Frame1 = Frame(windwC)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="#FFFFFF")
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

            tree = ttk.Treeview(Frame1, columns=(1, 2, 3, 4), show="headings", height="3")
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
            query()

        def Stat():
            def f1():
                x = np.linspace(1, 1000, 50)
                plt.loglog()
                plt.plot(x, 1. / x)
                plt.plot(x, 1. / x ** 2)

                plt.xlabel('Durée de vie ')
                plt.ylabel('Machine KOMAX ')
                plt.title('Durée de vie de Machine KOMAX ')
                plt.grid(True)
                plt.savefig("../Images/test.png")
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
                n, bins, patches = plt.hist(x, 50, facecolor='b', alpha=0.5)

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

            Frame1 = Frame(windwC)
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
            Message4.configure(
                text='''Cet indicateur permet d’évaluer l’indisponibilité et les arrêts des boitiers.''')
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

        def plan():
            Frame1 = Frame(windwC)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='solid')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="solid")
            Frame1.configure(background="#FFFFFF")

            def Database():
                global conn, cursor
                conn = sqlite3.connect('../BD/data.db')
                cursor = conn.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS `Planning` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Pname TEXT, Ptype TEXT, Pmember TEXT, address TEXT, tache TEXT, dure TEXT)")

            def Read():
                tree.delete(*tree.get_children())
                Database()
                cursor.execute("SELECT * FROM `Planning` ORDER BY `Pmember` ASC")
                fetch = cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=(data[1], data[2], data[3], data[4], data[5], data[6]))
                cursor.close()
                conn.close()
                txt_result.config(text="Successfully read the data from database", fg="black")


            def Create():
                if Pname.get() == "" or Pmember.get() == "" or Ptype.get() == "" or ADDRESS.get() == "" or Tache.get() == "" or Dure.get() == "":
                    txt_result.config(text="Please complete the required field!", fg="red")
                else:
                    Database()
                    cursor.execute(
                        "INSERT INTO `Planning` (Pname, Pmember, Ptype, address, Tache, Dure) VALUES(?, ?, ?, ?, ?, ?)", (
                        str(Pname.get()), str(Pmember.get()), str(Ptype.get()), str(ADDRESS.get()), str(Tache.get()),
                        str(Dure.get())))
                    conn.commit()
                    Read()
                    try:
                        Pname.set("")
                        Pmember.set("")
                        Ptype.set("")
                        ADDRESS.set("")
                        Tache.set("")
                        Dure.set("")
                        cursor.close()
                        conn.close()
                        txt_result.config(text="Created a data!", fg="green")
                    except:
                        pass


            Pname = StringVar()
            Pmember = StringVar()
            Ptype = StringVar()
            ADDRESS = StringVar()
            Tache = StringVar()
            Dure = StringVar()

            Buttons = Frame(Frame1, width=300, height=100)
            Buttons.pack(side=BOTTOM)
            RadioGroup = Frame(Frame1)
            Male = Radiobutton(RadioGroup, text="Curative", variable=Ptype, value="Curative", font=('arial', 16)).pack(side=LEFT)
            Female = Radiobutton(RadioGroup, text="Preventive", variable=Ptype, value="Preventive", font=('arial', 16)).pack(side=LEFT)

            # ==================================LABEL WIDGET=======================================
            txt_Pname = Label(Frame1, text="Planning:", font=('arial', 16), bd=15)
            txt_Pname.place(relx=0.089, rely=0.03, relheight=0.04
                               , relwidth=0.185)
            txt_Pmember = Label(Frame1, text="Member:", font=('arial', 16), bd=15)
            txt_Pmember.place(relx=0.089, rely=0.08, relheight=0.04
                               , relwidth=0.185)
            txt_Ptype = Label(Frame1, text="Type:", font=('arial', 16), bd=15)
            txt_Ptype.place(relx=0.089, rely=0.13, relheight=0.04
                               , relwidth=0.185)
            txt_address = Label(Frame1, text="Address:", font=('arial', 16), bd=15)
            txt_address.place(relx=0.089, rely=0.18, relheight=0.04
                               , relwidth=0.185)
            txt_Tache = Label(Frame1, text="Tâche:", font=('arial', 16), bd=15)
            txt_Tache.place(relx=0.089, rely=0.23, relheight=0.04
                               , relwidth=0.185)
            txt_Dure = Label(Frame1, text="Duré:", font=('arial', 16), bd=15)
            txt_Dure.place(relx=0.089, rely=0.28, relheight=0.04
                               , relwidth=0.185)
            txt_result = Label(Buttons)
            txt_result.place(relx=0.089, rely=0.33, relheight=0.04
                               , relwidth=0.185)

            # ==================================ENTRY WIDGET=======================================
            Pname = Entry(Frame1, textvariable=Pname, width=30)
            Pname.place(relx=0.289, rely=0.03)
            Pmember = Entry(Frame1, textvariable=Pmember, width=30)
            Pmember.place(relx=0.289, rely=0.08)
            RadioGroup.place(relx=0.289, rely=0.13)
            address = Entry(Frame1, textvariable=ADDRESS, width=30)
            address.place(relx=0.289, rely=0.18)
            Tache = Entry(Frame1, textvariable=Tache, width=30)
            Tache.place(relx=0.289, rely=0.23)
            Dure = Entry(Frame1, textvariable=Dure, width=30)
            Dure.place(relx=0.289, rely=0.28)

            # ==================================BUTTONS WIDGET=====================================
            btn_create = Button(Buttons, width=10, text="Create", command=Create)
            btn_create.pack(side=LEFT)


            # ==================================LIST WIDGET========================================
            scrollbary = Scrollbar(Frame1, orient=VERTICAL)
            scrollbarx = Scrollbar(Frame1, orient=HORIZONTAL)
            tree = ttk.Treeview(Frame1, columns=("Pname", "Pmember", "Ptype", "Address", "Tache", "Dure"),
                                selectmode="extended", height=13, yscrollcommand=scrollbary.set,
                                xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)
            tree.heading('Pname', text="Planning", anchor=W)
            tree.heading('Pmember', text="Type", anchor=W)
            tree.heading('Ptype', text="Member", anchor=W)
            tree.heading('Address', text="Address", anchor=W)
            tree.heading('Tache', text="Tâche", anchor=W)
            tree.heading('Dure', text="Duré", anchor=W)
            tree.column('#0', stretch=NO, minwidth=0, width=0)
            tree.column('#1', stretch=NO, minwidth=0, width=80)
            tree.column('#2', stretch=NO, minwidth=0, width=120)
            tree.column('#3', stretch=NO, minwidth=0, width=80)
            tree.column('#4', stretch=NO, minwidth=0, width=150)
            tree.column('#5', stretch=NO, minwidth=0, width=120)
            tree.column('#6', stretch=NO, minwidth=0, width=120)
            tree.place(relx=0.09, rely=0.39)
            Read()

        windwC.BTN = Button(windwC)
        imPlanning = PhotoImage(file="../Images/Planning.PNG")
        windwC.BTN.place(relx=0.06, rely=0.546, height=28, width=117)
        windwC.BTN.configure(activebackground="#424949",bd=0)
        windwC.BTN.configure(activeforeground="#424949")
        windwC.BTN.configure(background="#424949")
        windwC.BTN.configure(disabledforeground="#424949")
        windwC.BTN.configure(foreground="#424949")
        windwC.BTN.configure(highlightbackground="#424949")
        windwC.BTN.configure(highlightcolor="black")
        windwC.BTN.configure(pady="0")
        windwC.BTN.configure(image=imPlanning)
        windwC.BTN.configure(command=plan)


        windwC.BTN1 = Button(windwC)
        imSuivi = PhotoImage(file="../Images/Suivi.PNG")
        windwC.BTN1.place(relx=0.061, rely=0.44, height=30, width=116)
        windwC.BTN1.configure(activebackground="#ececec",bd=0)
        windwC.BTN1.configure(activeforeground="#000000")
        windwC.BTN1.configure(background="#d9d9d9")
        windwC.BTN1.configure(disabledforeground="#a3a3a3")
        windwC.BTN1.configure(foreground="#000000")
        windwC.BTN1.configure(highlightbackground="#d9d9d9")
        windwC.BTN1.configure(highlightcolor="black", border=0)
        windwC.BTN1.configure(pady="0")
        windwC.BTN1.configure(image=imSuivi)
        windwC.BTN1.configure(command=suivi)

        windwC.BTN2 = Button(windwC)
        imStat = PhotoImage(file="../Images/Stat.PNG")
        windwC.BTN2.place(relx=0.06, rely=0.65, height=30, width=120)
        windwC.BTN2.configure(activebackground="#ececec")
        windwC.BTN2.configure(activeforeground="#000000")
        windwC.BTN2.configure(background="#d9d9d9")
        windwC.BTN2.configure(disabledforeground="#a3a3a3")
        windwC.BTN2.configure(foreground="#000000")
        windwC.BTN2.configure(highlightbackground="#d9d9d9")
        windwC.BTN2.configure(highlightcolor="black")
        windwC.BTN2.configure(pady="0")
        windwC.BTN2.configure(image=imStat, border=0)
        windwC.BTN2.configure(command=Stat)




        windwC.mainloop()
    mainC()
