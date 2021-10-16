from tkinter import *

class Main_Screen(Tk,Frame):
    def __init__(self):
        super().__init__()
        self.title('LIBRARY')
        self.minsize(700,500)
        self.maxsize(800,600)
        self.screen = Frame(self)
        Label(self.screen, text="WELCOME TO LIBRARY", bg='gray', width="300", height="3", font=("Calibri", 15)).pack(side=TOP)
        self.config(bg='gray')
        photo = PhotoImage(file='D:/book1.png',)
        Label(self.screen,image=photo).pack()
        Button(self.screen, text="General Info ",width='20',height='2',bg='olive drab1').pack()
        Button(self.screen, text="Lend Book",width='20',height='2',bg='powder blue').pack()
        Button(self.screen, text="Book Reservation",width='20',height='2',bg='plum1').pack()
        Button(self.screen, text="Return Book",width='20',height='2',bg='MediumPurple1').pack()
        Button(self.screen, text="Check Fine",width='20',height='2',bg='PaleGreen3').pack()
        Button(self.screen, text="Library Info", width='20', height='2', bg='khaki1',command = self.LIBRARY_INFO).pack()
        # Label(self.screen, text="CHOOSE ONE OPTION", bg='gray', width="300", height="3", font=("Calibri", 15)).pack(side=)
        self.screen.pack()
        self.mainloop()
    def LIBRARY_INFO(self):
        self.s1 = Toplevel(self.screen)
        self.s1.geometry("300x300")
        self.s1.title("LIBRARY INFO")
        Label(self.s1, text="LIBRARY INFO", bg='pink', width="300", height="3", font=("Calibri", 13)).pack()
        self.s1.config(bg='cadet blue')
        Label(self.s1, text="").pack()
        Button(self.s1, text="CHECK INFO", height="3", width="30",command=self.Address).pack()
        self.s1.mainloop()

    def Address(self):
        Label(self.s1, text="").pack()
        Label(self.s1, text=f'The library is in  Karachi , Pakistan ').pack()



Main_Screen()