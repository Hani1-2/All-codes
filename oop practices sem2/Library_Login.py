from tkinter import *
import os
class login(Frame,Tk):
    def __init__(self):
        super().__init__()
        self.screen1 = Toplevel(self)
        self.screen1.title("Login")
        self.screen1.geometry("300x300")
        Label(self.screen1, text="LOGIN", bg='cadet blue', width="300", height="3", font=("Calibri", 13)).pack()
        Label(self.screen1, text="Please enter details below to login").pack()
        Label(self.screen1, text="").pack()

        # global username_verify
        # global password_verify
        #
        self.username_verify = StringVar()
        self.password_verify = StringVar()
        #
        # global username_entry1
        # global password_entry1


        Label(self.screen1, text="Username * ").pack()
        username_entry1 = Entry(self.screen1, textvariable=self.username_verify)
        username_entry1.pack()
        Label(self.screen1, text="").pack()
        Label(self.screen1, text="Password * ").pack()
        password_entry1 = Entry(self.screen1, textvariable=self.password_verify)
        password_entry1.pack()
        Label(self.screen1, text="").pack()
        Button(self.screen1, text="Login", width=10, height=2,command=self.login_verify).pack()

    def login_sucess(self):
        self.screen2 = Toplevel(self.screen1)
        self.screen2.title("Success")
        self.screen2.geometry("150x100")
        Label(self.screen2, text="Login Sucess").pack()
        Button(self.screen2, text="OK",command=self.screen2.destroy).pack() # command = delete2

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
        # username_entry1.delete(0, END)
        # password_entry1.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                self.login_sucess()
            else:
                self.password_not_recognised()

        else:
            self.user_not_found()

class register(Frame,Tk):

    def __init__(self):
        super().__init__()
        self.screen = Toplevel(self)
        self.screen.title("Register")
        self.screen.geometry("300x300")
        Label(self.screen, text="REGISTERATION", bg='cadet blue', width="300", height="3", font=("Calibri", 13)).pack()


        # global username
        # global password
        # global username_entry
        # global password_entry
        username = StringVar()
        password = StringVar()

        Label(self.screen, text="Please enter details below").pack()
        Label(self.screen, text="").pack()
        Label(self.screen, text="Username * ").pack()

        self.username_entry = Entry(self.screen,textvariable= username).pack()
        Label(self.screen, text="Password * ").pack()
        self.password_entry = Entry(self.screen,textvariable=password).pack()
        Label(self.screen, text="").pack()

        def register_user():
            print("working")

            username_info = username.get()
            password_info = password.get()

            file = open('user_information', "w")
            file.write(username_info + ':' + password_info)
            file.close()

            # username_entry.delete(0, END)
            # password_entry.delete(0, END)

            Label(self.screen, text="Registration Sucess", fg="green", font=("calibri", 11)).pack()
        Button(self.screen, text="Register", width=10, height=1, command=register_user).pack()



class main_screen(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x300")
        self.title("LIBRARY MANAGEMENT SYSTEM")
        Label(self,text="LIBRARY MANAGEMENT SYSTEM", bg='pink', width="300", height="3", font=("Calibri", 13)).pack()
        self.config(bg='cadet blue')
        Label(self,text="").pack()
        Button(self,text="Login", height="3", width="30",command=login).pack()
        Label(self,text="").pack()
        Label(self,text="").pack()
        Button(self,text="Register", height="3", width="30",command=register).pack()

        self.mainloop()
o = main_screen()





# from tkinter import*
# import tkinter.messagebox
# from tkinter import ttk
# import random
# import time
# import datetime
#
# def main():
#     root = Tk()
#     app = Window1(root)
#
# class Window1:
#     def __init__(self, master):
#         self.master =master
#         self.master.title("Restaurant Login System")
#         self.master.geometry('1350x750+0+0')
#         self.master.config(bg ='powder blue')
#         self.frame = Frame(self.master, bg ='powder blue')
#         self.frame.pack()
#
#         self.Username = StringVar()
#         self.Password = StringVar()
#
#         self.blogin = Button(self.frame, text='Login', width=15 command = self.new_window)
#
#     def new_window(self):
#         self.newWindow = Toplevel(self.master)
#         self.app = Window2(self.newWindow)
#
# class Window2:
#     def __init__(self, master):
#         self.master =master
#         self.master.title("Restaurant Management System")
#         self.master.geometry('1350x750+0+0')
#         self.master.config(bg ='cadet blue')
#         self.frame = Frame(self.master, bg ='powder blue')
#         self.frame.pack()
#
#         self.Username = StringVar()
#         self.Password = StringVar()
#
#         self.blogin = Button(self.frame, text = 'Login', width = 15 command = self.new_)
#
#
#
# if __name__ == 'main__':
#     main()