from tkinter import *

from LibraryUser import date, Person, BookItem

class User:
    d = {}
    def __init__(self):
        self.USER_LOG()
    def USER_LOG(self,n='user_login'):
        self.n = n
        with open(self.n, 'r') as f:
            x = len(f.readlines())
            f.seek(0)
            for i in range(x):
                v = f.readline()
                v1 = v.split(',')
                if '\n' in v1:
                    v1.remove('\n')
                User.d[v1[0]] = v1[1:]
User()
class Main_Screen(Tk, Frame):
    def __init__(self):
        super().__init__()
        self.date = date
        self.Book = BookItem.book
        self.title('LIBRARY')
        self.minsize(400, 500)
        self.maxsize(500, 800)
        self.screen = Frame(self)
        Label(self.screen, text="WELCOME TO LIBRARY", width="300", height="5", font=("Bodoni MT Black", 15)).pack(
            side=TOP)
        self.config(bg='cadet blue')
        # photo = PhotoImage(file='D:/book1.png' )
        # Label(self.screen, image=photo).pack()
        Button(self.screen, text="Display Book", width='20', height='2',fg='black', font=("Calibri", 10, "bold"), bd=6, bg='pink',
               command=self.displaybook).pack()
        Button(self.screen, text="General Info ", width='20', height='2',fg='black', font=("Calibri", 10, "bold"), bd=6, bg='olive drab1',command=self.GeneralInfo).pack()
        Button(self.screen, text="Lend Book", width='20', height='2',fg='black', font=("Calibri", 10, "bold"), bd=6, bg='powder blue', command=self.Lend_Book).pack()
        Button(self.screen, text="Book Reservation", width='20', height='2',fg='black', font=("Calibri", 10, "bold"), bd=6, bg='plum1',
               command=self.book_reserve).pack()
        Button(self.screen, text="Return Book", width='20', height='2',fg='black', font=("Calibri", 10, "bold"), bd=6, bg='MediumPurple1',
               command=self.Return_Book).pack()
        Button(self.screen, text="Library Info", width='20', height='2',fg='black', font=("Calibri", 10, "bold"), bd=6, bg='yellow', command=self.LIBRARY_INFO).pack()
        Button(self.screen, text="Payment Method", width='20', height='2',fg='black', font=("Calibri", 10, "bold"), bd=6, bg='khaki1', command=self.payment).pack()
        Button(self.screen, text="Exit", width='20', height='2',fg='black', font=("Calibri", 10, "bold"), bd=6, bg='PaleGreen3',command = self.Exit).pack()

        Label(self.screen, text="CHOOSE ONE OPTION", width="300", height="8", font=("Bodoni MT Black", 15)).pack()

        self.screen.pack()
        self.mainloop()

    def LIBRARY_INFO(self):
        self.s1 = Toplevel(self.screen)
        self.s1.geometry("300x300")
        self.s1.title("LIBRARY INFO")
        Label(self.s1, text="LIBRARY INFO", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s1.config(bg='cadet blue')
        Label(self.s1, text="", bg='cadet blue').pack()
        Button(self.s1, text="CHECK INFO", bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.Address).pack()
        self.s1.mainloop()

    def Address(self):
        Label(self.s1, text="",bg='cadet blue').pack()
        Label(self.s1, text=f'The library is in  Karachi , Pakistan ',  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def Check_Fine(self):
        self.s3 = Toplevel(self.screen)
        self.s3.geometry("700x700")
        self.s3.title("CHECK FINE")
        Label(self.s3, text="CHECK FINE", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s3.config(bg='cadet blue')
        Label(self.s3, text="", bg='cadet blue').pack()
        Label(self.s3, text="", bg='cadet blue').pack()
        Label(self.s3, text='Fine applied if you return book after 10 days', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s3, text="", bg='cadet blue').pack()
        self.day = self.date()  ## just assume that user placed order today and after that i correct it
        self.x = self.day.due_day
        Button(self.s3, text="Check Fine",bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.check_fine).pack()
        self.s3.mainloop()

    def check_fine(self):
        y = self.e7.get()
        l = User.d[self.idd]
        if y not in l:
            Label(self.s3, text='You dont lend this book ').pack()
        else:
            l.remove(y)
            print(l)
            Label(self.s3, text='', bg='cadet blue').pack()
            Label(self.s3, text='Welcome !!! Now you can return the book', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            Label(self.s3, text='', bg='cadet blue').pack()
            l = Label(self.s3, text='Enter today date in local format dd/mm/yy', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            self.e1 = Entry(self.s3)
            self.e1.pack()
            Label(self.s3, text='', bg='cadet blue').pack()
            self.dat= date()
            self.dat.issue_date()
            self.dat.due_date()
            Button(self.s3, text='click',bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.fine).pack()


    def Exit(self):
        self.s7 = Toplevel(self.screen)
        self.s7.geometry("300x300")
        self.s7.title("Maintain User Log")
        Label(self.s7, text="Maintain User Log", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s7.config(bg='cadet blue')
        Label(self.s7, text="", bg='cadet blue').pack()
        Label(self.s7, text="Enter your Id please", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s7, text="", bg='cadet blue').pack()
        self.e8 = Entry(self.s7)
        self.e8.pack()
        Button(self.s7, text="check_log",bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30",command = self.history).pack()
        self.s7.mainloop()
    def history(self):
        string = ''
        st =''
        self.c = self.e8.get()
        try:
            if self.c in self.a.d:
                self.log = self.a.d[self.c]
                for i in self.log:
                    string += (i+',')
                print(string)
            else:
                if self.c in User.d:
                    for i in self.log:
                        string += (i + ',')
                    print(string)
        except:
            Label(self.s7, text='You don\'t have any log',bg='cadet blue').pack()





        with open('user_history','a') as f1:
            y = f1.write(str(self.c)+','+''+string+'\n') ## here you can change file formatting
            Label(self.s7, text=f'Your id is {self.c}',height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            Label(self.s7,text='', bg='cadet blue').pack()
            Label(self.s7,text=f'and your history is {string}', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def fine(self):
        e = self.e1.get()
        self.d = e[:2]
        self.m = e[3:5]
        print(type(e))
        print(self.day.today, int(self.d), self.day.due_day)
        if int(self.day.today)<= int(self.d) <=self.day.due_day:
            Label(self.s3, text='', bg='cadet blue').pack()
            Label(self.s3, text='no fine', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            Label(self.s3, text='Your book return successfully', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        else:
            Label(self.s3, text='you run out of day , You have to pay of 50 Rs for fine', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def Return_Book(self):
        self.s3 = Toplevel(self.screen)
        self.s3.geometry("800x800")
        self.s3.title("Return Book")
        Label(self.s3, text="Return Book", bg='cadet blue', width="300", height="2", font=("Bodoni MT Black", 13)).pack()
        self.s3.config(bg='cadet blue', height="4")
        Label(self.s3, text="", bg='cadet blue').pack()
        self.day = self.date()  ## just assume that user placed order today and after that i correct it
        self.x = self.day.due_day
        Button(self.s3, text="return book", bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="2", width="30", command=self.return_book).pack()
        self.s3.mainloop()

    def return_book(self):
        Label(self.s3, text="",  bg='cadet blue').pack()
        Label(self.s3, text='enter your Id please:', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        self.e2 = Entry(self.s3)
        self.e2.pack()
        Label(self.s3, text='',  bg='cadet blue').pack()
        Button(self.s3, text='click', bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, command=self.returnb).pack()

    def returnb(self):
        self.idd = self.e2.get()
        self.a = User()
        self.a.USER_LOG('user_history')
        if self.idd in self.a.d:
            x = self.a.d.get(self.idd)
            print(x)
            if len(x) == 1:
                Label(self.s3, text='first lend then return the book', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            else:
                Label(self.s3, text=f'you lend the book {x[1:]}', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                Label(self.s3,text = '', bg='cadet blue').pack()
                Label(self.s3, text='Enter book name you want to return', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                self.e7=Entry(self.s3)
                self.e7.pack()
                Label(self.s3, text='', bg='cadet blue').pack()
        else:
            x = User.d[(self.idd)]
            print(x)
            if len(x) == 1:
                Label(self.s3, text='first lend then return the book',  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            else:
                Label(self.s3, text=f'you lend the book {x[1:]}',  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                Label(self.s3,text = '', bg='cadet blue').pack()
                Label(self.s3, text='Enter book name you want to return',  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
                self.e7 = Entry(self.s3)
                self.e7.pack()
                Label(self.s3, text='', bg='cadet blue').pack()
        Button(self.s3, text='check fine', bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, command=self.check_fine).pack()

    def Lend_Book(self):
        self.s2 = Toplevel(self.screen)
        self.s2.geometry("800x800")
        self.s2.title("LEND BOOK")
        self.s2.Book = BookItem.book
        Label(self.s2, text="Lend Book", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s2.config(bg='cadet blue')
        Label(self.s2, text="", bg='cadet blue').pack()
        Label(self.s2, text='You have 10 days to return the book', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s2, text="",  bg='cadet blue').pack()
        Label(self.s2, text="Enter your Id please", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s2, text='',  bg='cadet blue').pack()
        self.u = Entry(self.s2)
        self.u.pack()
        Label(self.s2, text='',  bg='cadet blue').pack()
        Button(self.s2, text='click', bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="1", width="30", command=self.lend_id).pack()

    def lend_id(self):
        self.b = self.u.get()
        Label(self.s2, text="",  bg='cadet blue').pack()
        Label(self.s2, text='Enter the name of book you want to lend:', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s2, text="",  bg='cadet blue').pack()
        self.e3 = Entry(self.s2)
        self.e3.pack()
        Label(self.s2, text='',  bg='cadet blue').pack()
        Button(self.s2, text='price', bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height='3', width="30", command=self.price).pack()
        Label(self.s2, text='',  bg='cadet blue').pack()
        Button(self.s2, text='lend', bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30", command=self.lend_book).pack()
        self.day = self.date()  ## just assume that user placed order today and after that i correct it
        self.x = self.day.due_day
        Label(self.s2, text='',  bg='cadet blue').pack()
        Button(self.s2, text='confirm order', bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="1", width="30", command=self.log1).pack()
        self.s2.mainloop()
    def price(self):
        x =self.e3.get()
        Label(self.s2, text='', bg='cadet blue').pack()
        if x in BookItem.book:
            n = BookItem.book[x]
            Label(self.s2, text=f'The price of book is {n}', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        else:
            Label(self.s2, text= 'Please check the name of book', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def log1(self):
        self.k = self.b
        self.a = User()
        self.a.USER_LOG('user_history')
        if self.k in self.a.d:
            self.c=str(self.e3.get())
            self.a.d[self.k].append(self.c)
            print(self.a.d)
        else:
            if self.k in User.d:
                self.User.d[self.k].append(self.c)
                print(self.User.d)


    def lend_book(self):
        book = BookItem.book
        e = str(self.e3.get())
        from LibraryUser import date
        if e in book:
            Label(self.s2, text='', bg='cadet blue').pack()
            Label(self.s2, text=f'the book {e} is issued', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            Label(self.s2, text='', bg='cadet blue').pack()
            w = date.issue_date(self)
            Label(self.s2, text=f'The issue date is {self.creation_date}', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            Label(self.s2, text='', bg='cadet blue').pack()
            Label(self.s2, text=f'The due date is {self.x}', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        else:
            Label(self.s2,text = '', bg='cadet blue').pack()
            Label(self.s2, text='Book is not available', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def book_reserve(self):
        self.s4 = Toplevel(self.screen)
        self.s4.geometry("400x400")
        self.s4.title("Book Reservation")
        Label(self.s4, text="Book Reservation", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 15)).pack()
        self.s4.config(bg='cadet blue')
        Label(self.s4, text="", bg='cadet blue').pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        Button(self.s4, text="Add Book", fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30", bg='PaleGreen', command=self.add_books).pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        Button(self.s4, text="Reservation Details", fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="30", bg='PaleGreen',
               command=self.fetch_reservation_detail).pack()
        self.day = self.date()  ## just assume that user placed order today and after that i correct it
        self.x = self.day.due_day
        self.s4.mainloop()

    def add_books(self):
        self.s5 = Toplevel(self.screen)
        self.s5.geometry("600x600")
        self.s5.title("Add Book")
        Label(self.s5, text="Add Book", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s5.config(bg='cadet blue')
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="Enter book name:",  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        self.e4 = Entry(self.s5)
        self.e4.pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="Enter author name:",  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        self.e5 = Entry(self.s5)
        self.e5.pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Button(self.s5, text="Add", fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="20", command=self.add_book).pack()

    def add_book(self):
        bname = self.e4.get()
        aname = self.e4.get()
        BookItem.book[bname] = aname
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text='Your book add successfully',  height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        #print(BookItem.book)

    def fetch_reservation_detail(self):
        self.s6 = Toplevel(self.screen)
        self.s6.geometry("600x600")
        self.s6.title("Fetch Reservation Details")
        Label(self.s6, text="Fetch Reservation Details", bg='cadet blue', width="300", height="3",
              font=("Bodoni MT Black", 13)).pack()
        self.s6.config(bg='cadet blue')
        Label(self.s6, text="", bg='cadet blue').pack()
        Label(self.s6, text="Enter the name of book you want to reserve:", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s6, text="", bg='cadet blue').pack()
        self.e6 = Entry(self.s6)
        self.e6.pack()
        Label(self.s6, text="", bg='cadet blue').pack()
        Button(self.s6, text="Reserve", fg='black', font=("Calibri", 10, "bold"), bd=6, height="3", width="20", command=self.fetch_reservation_details).pack()

    def fetch_reservation_details(self):
        Label(self.s6, text="", bg='cadet blue').pack()
        re = str(self.e6.get())
        from LibraryUser import BookReservation
        if re not in BookItem.book:
            Label(self.s6, text='Book is not available to reserve', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        else:
            b = BookReservation.remove_book(self, re)
            Label(self.s6, text='Your book is reserve now', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def payment(self):
        self.s4 = Toplevel(self.screen)
        self.s4.geometry("500x500")
        self.s4.title("PAYMENT")
        Label(self.s4, text="PAYMENT", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s4.config(bg='cadet blue')
        Label(self.s4, text="", bg='cadet blue').pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        Label(self.s4, text="Enter your Account No for payment", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        self.e5 = Entry(self.s4)
        self.e5.pack()
        Label(self.s4, text="", bg='cadet blue').pack()
        Button(self.s4, text='click', bg='turquoise',fg='black', font=("Calibri", 10, "bold"), bd=6, height="2", width="30", command=self.paycheck).pack()

    def paycheck(self):
        self.Ac = self.e5.get()
        if self.Ac.isdigit:
            Label(self.s4, text='Amount is paid', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
            Label(self.s4, text='Thank you come again', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        else:
            Label(self.s4, text='Invalid Account No', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def GeneralInfo(self):
        self.s5 = Toplevel(self.screen)
        self.s5.geometry("600x600")
        self.s5.title("General Info")
        Label(self.s5, text="General Info", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s5.config(bg='cadet blue')
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="Welcome to Student Library", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="You can lend books for 10 days", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="After 10 days fine will be applicable to all students", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="You can reserve book and Add books of your choice", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
        Label(self.s5, text="", bg='cadet blue').pack()
        Label(self.s5, text="There is a payment method by Account", height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()

    def displaybook(self):
        self.s6 = Toplevel(self.screen)
        self.s6.geometry("600x600")
        self.s6.title("Display Book")
        Label(self.s6, text="Display Book", bg='cadet blue', width="300", height="3", font=("Bodoni MT Black", 13)).pack()
        self.s6.config(bg='cadet blue')
        Label(self.s6, text="", bg='cadet blue').pack()
        for i in BookItem.book:
            Label(self.s6, text=f'{i}\n', height="3", font=("Calibri", 10, "bold"), bg='cadet blue').pack()
# Main_Screen()
