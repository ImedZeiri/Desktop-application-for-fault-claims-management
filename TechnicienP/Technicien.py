from tkinter import *
import smtplib
import speech_recognition as sr
import pyttsx3
import connection
import tkinter.ttk as ttk
from email.message import EmailMessage
from tkinter import messagebox

class test2:
    def mainT():
        windwT = Tk()
        windwT.geometry("1280x700")
        windwT.minsize(1280,700)
        windwT.maxsize(1280,700)
        windwT.title("Interface Technicien")
        windwT.iconbitmap("tt.ico")
        background_image = PhotoImage(file='../Images/TechImg.PNG')
        background_label = Label(windwT, image=background_image)
        background_label.place(relwidth=1, relheight=1)


        def ffrm2():
            Frame1 = Frame(windwT)
            Frame1.place(relx=0.3, rely=0.125, relheight=0.81, relwidth=0.6558)
            Frame1.configure(relief='groove')
            Frame1.configure(borderwidth="0")
            Frame1.configure(relief="groove")
            Frame1.configure(background="white")

            Mail_Ad = Entry(Frame1)
            Mail_Ad.place(relx=0.102, rely=0.0, relheight=0.07, relwidth=0.3)
            Mail_Ad.insert(0, 'Adresse Mail')

            Mail_Pwd = Entry(Frame1)
            Mail_Pwd.place(relx=0.482, rely=0.0, relheight=0.07, relwidth=0.3)
            Mail_Pwd.configure(show='*')
            Mail_Pwd.insert(0, 'Password ')

            Sub = Entry(Frame1)
            Sub.place(relx=0.2, rely=0.135, relheight=0.07, relwidth=0.585)
            Sub_Label = Label(Frame1)
            Sub_Label.configure(text='Objet :')
            Sub_Label.place(relx=0.0873, rely=0.15, relheight=0.05, relwidth=0.1)
            Sub_Label.configure(background="white")

            Mail_Content_Label = Label(Frame1)
            Mail_Content_Label.configure(text='Message :')
            Mail_Content_Label.place(relx=0.102, rely=0.25, relheight=0.05, relwidth=0.1)
            Mail_Content_Label.configure(background="white")

            Mail_Content = Text(Frame1)
            Mail_Content.place(relx=0.2, rely=0.3, relheight=0.3, relwidth=0.585)

            def Sent_Mail():
                Ad_SRC = Mail_Ad.get()
                PWD_SRC = Mail_Pwd.get()
                Objet = Sub.get()
                Contenu = Mail_Content.get("1.0", "end")
                print(Ad_SRC, PWD_SRC, Objet, Contenu)
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login(Ad_SRC, PWD_SRC)
                    email = EmailMessage()
                    email['From'] = Ad_SRC
                    email['To'] = 'amal9fersi@gmail.com'
                    email['Subject'] = Objet
                    email.set_content(Contenu)
                    server.send_message(email)
                    messagebox.showinfo('valid','Mail has been sent succefuly ')

                except:
                    messagebox.showwarning('er','Login Failed Verify your Password')

            def Mailling():
                listener = sr.Recognizer()
                engine = pyttsx3.init()

                def talk(text):
                    engine.say(text)
                    engine.runAndWait()

                def get_info():
                    with sr.Microphone() as source:
                        print('listenning ...')
                        voice = listener.listen(source)
                        info = listener.recognize_google(voice)
                        print(info)
                        return info.lower()

                def send_email(reciver, subject, msg):
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    server.login('amal9fersi@gmail.com', 'mot de passe mail')
                    email = EmailMessage()
                    email['From'] = 'amal9fersi@gmail.com'
                    email['To'] = reciver
                    email['Subject'] = subject
                    email.set_content(msg)
                    server.send_message(email)

                Email_list = {
                    "engineer": "intizeiri@gmail.com",
                    "student": "yasminezeiri@gmail.com",
                }

                def get_email_info():
                    try:
                        talk('A qui vous voulez envoyer un email ?')
                        name = get_info()
                        reciver = Email_list[name]
                        print(reciver)
                        talk('Quel est le sujet de votre mail ?')
                        subject = get_info()
                        talk('''c'est quoi votre message ''')
                        msg = get_info()
                        print(name, subject, msg)
                        send_email(reciver, subject, msg)
                    except:
                        talk('''s'il vous plait verifier votr choix''')
                        messagebox.showwarning('Error','''s'il vous plait verifier votr choix''')


                talk('bonjour cher technicien ')
                get_email_info()


            B_Rec_Vocal = Button(Frame1)
            B_Rec_Vocal.place(relx=0.2, rely=0.84, height=25, width=170)
            B_Rec_Vocal.configure(text="Vocal")
            B_Rec_Vocal.configure(command=Mailling)

            B_Rec_Man = Button(Frame1)
            B_Rec_Man.place(relx=0.53, rely=0.84, height=25, width=170)
            B_Rec_Man.configure(text="Envoyer")
            B_Rec_Man.configure(command=Sent_Mail)



        def ffrm1():
            Frame2 = Frame(windwT)
            Frame2.place(relx=0.3, rely=0.125, relheight=0.81,  relwidth=0.6558)
            Frame2.configure(relief='groove')
            Frame2.configure(borderwidth="0")
            Frame2.configure(relief="groove")
            Frame2.configure(background="white")

            def DisplayData():
                tree.delete(*tree.get_children())
                connection.Database()
                connection.cursor.execute("SELECT * FROM `Intervention` ORDER BY `v1` ASC")
                fetch = connection.cursor.fetchall()
                for data in fetch:
                    tree.insert('', 'end', values=data)
                connection.cursor.close()
                connection.conn.close()

            def Delete():
                if tree.selection():
                    result = messagebox.askquestion(' Delete Data Row In SQLite',
                                                      'Are you sure you want to delete this record?', icon="warning")
                    if result == 'yes':
                        curItem = tree.focus()
                        contents = (tree.item(curItem))
                        selecteditem = contents['values']
                        tree.delete(curItem)
                        connection.Database()
                        try:
                            connection.cursor.execute("DELETE FROM `Intervention` WHERE `v1` == " + selecteditem[0])
                        except :
                            pass
                        connection.conn.commit()
                        connection.cursor.close()
                        connection.conn.close()
                    else:
                        DisplayData()




            # ==================================LIST WIDGET========================================
            scrollbary = Scrollbar(Frame2, orient=VERTICAL)
            scrollbarx = Scrollbar(Frame2, orient=HORIZONTAL)
            tree = ttk.Treeview(Frame2,columns=(1, 2, 3, 4), selectmode="extended",
                                height=20, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
            scrollbary.config(command=tree.yview)
            scrollbary.pack(side=RIGHT, fill=Y)
            scrollbarx.config(command=tree.xview)
            scrollbarx.pack(side=BOTTOM, fill=X)

            tree.heading(1, text="Zone ", anchor=W)
            tree.heading(2, text="Temps", anchor=W)
            tree.heading(3, text="Type ", anchor=W)
            tree.heading(4, text=" ", anchor=W)

            tree.configure(height=8)
            tree.column("#0", width=200)
            tree.column("#1", width=130)
            tree.column("#2", width=130)
            tree.column("#3", width=130)
            tree.place(relx=0.06, rely=0.26)

            btn_delete = Button(Frame2, width=15, text="Terminez", command=Delete)
            btn_delete.place(relx=0.3, rely=0.125)

            DisplayData()



        BTN = Button(windwT)
        imInter = PhotoImage(file="../Images/ImInter.PNG")
        BTN.place(relx=0.03, rely=0.44, height=25, width=170)
        BTN.configure(activebackground="#ececec")
        BTN.configure(activeforeground="#000000")
        BTN.configure(background="#d9d9d9")
        BTN.configure(disabledforeground="#a3a3a3")
        BTN.configure(foreground="#000000")
        BTN.configure(highlightbackground="#d9d9d9")
        BTN.configure(highlightcolor="black",border=0)
        BTN.configure(pady="0")
        BTN.configure(image=imInter)
        BTN.configure(command=ffrm1)


        BTN1 = Button(windwT)
        imRecl = PhotoImage(file="../Images/ImRec.PNG")
        BTN1.place(relx=0.03, rely=0.564, height=27, width=170)
        BTN1.configure(activebackground="#ececec")
        BTN1.configure(activeforeground="#000000")
        BTN1.configure(background="#d9d9d9")
        BTN1.configure(disabledforeground="#a3a3a3")
        BTN1.configure(foreground="#000000")
        BTN1.configure(highlightbackground="#d9d9d9")
        BTN1.configure(highlightcolor="black")
        BTN1.configure(pady="0")
        BTN1.configure(image=imRecl,border=0)
        BTN1.configure(command=ffrm2)


        windwT.mainloop()
    mainT()
