import sys
sys.path.append('CEP1')
from tkinter import *
from LibraryUser import *

from  Librarian import *
from
class Id:
    def idd(self):
        with open('user_login','r') as f:
            x = f.readlines()
            if '\n' in x:
                x.remove('\n')
                # print(x)
            if x == []:
                self.new_id = 0
            else:
                self.new_id =(x[-1][0])
class main_screen(Tk):
    id = 0
    def __init__(self,id=0):
        super().__init__()
        i = Id()
        i.idd()
        main_screen.id = int(i.new_id)
        # main_screen.id = main_screen.new_id
        self.geometry("300x300")
        self.title("LIBRARY MANAGEMENT SYSTEM")
        Label(self,text="LIBRARY MANAGEMENT SYSTEM", bg='pink', width="300", height="3", font=("Calibri", 13)).pack()
        self.config(bg='cadet blue')
        Label(self,text="").pack()
        Button(self,text="USER", height="3", width="30",command=self.second_screen).pack()
        Label(self,text="").pack()
        Label(self,text="").pack()
        Button(self,text="LIBRARIAN", height="3", width="30",command=self.librarian).pack()### here you've to put your shell execution

        self.mainloop()

    def librarian(self):
        a1 = Librarian()
        a1.add_book_item(500)
        print(a1.get_Num_Books())

    def second_screen(self):
        self.s1 = Toplevel(self)
        self.s1.geometry("300x300")
        self.s1.title("LIBRARY MANAGEMENT SYSTEM")
        Label(self.s1, text="LIBRARY MANAGEMENT SYSTEM", bg='pink', width="300", height="3",font=("Calibri", 13)).pack()
        self.s1.config(bg='cadet blue')
        Label(self.s1, text="").pack()
        Button(self.s1, text="Login", height="3", width="30", command=self.login).pack()
        Label(self.s1, text="").pack()
        Label(self.s1, text="").pack()
        Button(self.s1, text="Register", height="3", width="30", command=self.register).pack()
        self.s1.mainloop()
    def login(self):
        self.screen1 = Toplevel(self.s1)
        self.screen1.title("Login")
        self.screen1.geometry("350x350")
        Label(self.screen1, text="LOGIN", bg='cadet blue', width="300", height="3", font=("Calibri", 13)).pack()
        Label(self.screen1, text="Please enter details below to login").pack()
        Label(self.screen1, text="").pack()

        # global username_verify
        # global password_verify
        #
        self.username_verify = StringVar()
        self.password_verify = StringVar()
        self.id = StringVar()
        #
        # global username_entry1
        # global password_entry1


        Label(self.screen1, text="Username * ").pack()
        self.username_entry1 = Entry(self.screen1, textvariable=self.username_verify)
        self.username_entry1.pack()
        Label(self.screen1, text="").pack()
        Label(self.screen1, text="Password * ").pack()
        self.password_entry1 = Entry(self.screen1, textvariable=self.password_verify)
        self.password_entry1.pack()
        Label(self.screen1, text="").pack()
        Label(self.screen1, text="Id * ").pack()
        self.id_entry1 = Entry(self.screen1, textvariable=self.id)
        self.id_entry1.pack()
        Label(self.screen1, text="").pack()
        Button(self.screen1, text="Login", width=10, height=2,command=self.login_verify).pack()

    def login_sucess(self):
        self.screen2 = Toplevel(self.screen1)
        self.screen2.title("Success")
        self.screen2.geometry("150x100")
        Label(self.screen2, text="Login Sucess").pack()
        Button(self.screen2, text="OK",command=Main_Screen).pack() # command = delete2

    def password_not_recognised(self):
        self.screen3 = Toplevel(self.screen1)
        self.screen3.title("Success")
        self.screen3.geometry("150x100")
        Label(self.screen3, text="Password Error").pack()
        Button(self.screen3, text="OK",command=self.screen3.destroy).pack()

    def user_not_found(self):
        self.screen4 = Toplevel(self.screen1)
        self.screen4.title("Success")
        self.screen4.geometry("150x100")
        Label(self.screen4, text="User Not Found").pack()
        Button(self.screen4, text="OK",command=self.screen4.destroy).pack() # command = delete4
    def login_verify(self):
        username1 = self.username_verify.get()
        password1 = self.password_verify.get()
        id1 = self.id.get()
        self.username_entry1.delete(0, END)
        self.password_entry1.delete(0, END)
        self.id_entry1.delete(0, END)


        with open('user_login','r') as f:
            value = f.read()
            if (id1+','+username1+' '+password1)in value:
                self.login_sucess()
            else:
                self.user_not_found()

    def register(self):
        self.screen = Toplevel(self.s1)
        self.screen.title("Register")
        self.screen.geometry("300x300")
        Label(self.screen, text="REGISTERATION", bg='cadet blue', width="300", height="3", font=("Calibri", 13)).pack()

        self.username = StringVar()
        self.password = StringVar()

        Label(self.screen, text="Please enter details below").pack()
        Label(self.screen, text="").pack()
        Label(self.screen, text="Username * ").pack()

        self.username_entry = Entry(self.screen,textvariable= self.username).pack()
        Label(self.screen, text="Password * ").pack()
        self.password_entry = Entry(self.screen,textvariable=self.password).pack()
        Label(self.screen, text="").pack()
        Button(self.screen, text="Register", width=10, height=1, command=self.register_user).pack()
    def register_user(self):
        print("working")
        username_info = self.username.get()
        password_info = self.password.get()
        main_screen.id+=1
        file = open('user_login', "a+")
        file.write(str(main_screen.id)+','+username_info + ' ' + password_info+','+'\n')

        file.close()

        Label(self.screen, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()
        Label(self.screen, text = '')
        Label(self.screen, text=f'Your id is {main_screen.id} bring it when you comeback').pack()


o = main_screen()
