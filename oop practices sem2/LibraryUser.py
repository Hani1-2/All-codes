###### Libarary User ########


class Address:
  def __init__(self,city, country):
    self.__city = city
    self.__country = country
  def lib(self):
    print(f'the library is in  {self.__city}  {self.__country} ')
class Person:
  dic = {}
  member_id = 0
  def __init__(self, name, email):
    self.name = name
    self.email = email

    Person.member_id += 1
    print('Your Id is',Person.member_id,'bring it when you return the book')

  def user_info(self):
    Person.dic[Person.member_id] = [self.name, self.email]
    return Person.dic


# class Constants:
#     def __init__(self):
#         self.MAX_BOOKS_ISSUED_TO_A_USER = 5
#         self.MAX_LENDING_DAYS = 10
import datetime as dt
class date:
    def __init__(self):
        self.due_day = 0
        self.creation_date = dt.datetime.now()
        self.today = self.creation_date.strftime('%d')
        self.due_date()
    def issue_date(self):
        self.creation_date = dt.datetime.now()
        print('the book issued on', self.creation_date)
    def due_date(self):
        self.month =self.creation_date.strftime('%m')
        if int(self.today) > 20 :
            if int(self.month)%2 == 0:
                due = 30 - int(self.today)
                self.due_day = 10 - due
            elif int(self.month)%2 != 0:
                due = 31 - int(self.today)
                self.due_day = 10 - due
        else:
            self.due_day = int(self.today) + 10
            # print('you have 10 days to return the book')
        return self.due_day
    def check_fine(self):
        # print('Welcome !!! Now you can return the book')
        day = input('Enter today date in local format dd/mm/yy')
        self.d = day[:2]
        self.m = day[3:5]
        print(self.month)
        if int(self.today)<= int(self.d) <=self.due_day:
            print('no fine')
        elif int(self.month) != self.m:
            print('You\'re a month late , fine is applicable for you' )
        else:
            print('you run out of day , You have to pay of 50 Rs for fine')
class BookReservation(date):
  def __init__(self):
    super().__init__()
    # d = date()
    # self.__creation_date = d.creation_date
  def add_book(self):
    book_name = input('enter book name')
    author_name = input('enter author name')
    BookItem.book[book_name]=author_name
    print('your book add successfully')
  def remove_book(self,book):
    BookItem.book.pop(book)

  def return_book(self):
    id = int(input('enter your Id please'))
    x = Person.dic.get(id)
    if len(x)==2:
        print('first lend then return the book')
    else:
        print('you lend the book',Person.dic[id][2])
        date.check_fine(self)
        print('Your book return successfully')

  def fetch_reservation_details(self):
    reserve = input('enter the name of book you want to reserve')
    if reserve not in BookItem.book:
        print('Book is not available to reserve')
    else:
        self.remove_book(reserve)
        print('your book is reserve now')



class BookItem:


    book = {'silent patient by Alex Michaelides': '90$','alchemist by polu coello':'50$', 'One Hundred Years of Solitude by  Gabriel García Márquez':'100$' ,'War and Peace by Leo Tolstoy':'80$','Lolita by Vladimir Nabokov':'40$','In Search of Lost Time by Marcel Proust':'120$','Ulysses':'100$',
             'The Great Gatsby by':'120$','One Hundred Years of Solitude by Gabriel Garcia Marquez':'100$' ,'Hamlet by William Shakespeare':'200$','harry potter by JK Rowling':'200$','The Handmaid\'s Tale by Margaret Atwood':'30$',
             'Educated by Tara Westover':'45$','Where the Crawdads Sing by Delia Owens':'39$','A Thousand Splendid Suns by Khaled Hosseini':'90$'}
  # book = {'silent patient': 'author','alchemist':'Paoulo','stay with me':'abeo'}
class BookLending(BookItem,date):
  def __init__(self):
    super().__init__()
    self.d=date()
  def lend_book(self):
    try:
      user_input = input('Enter the name of book you want to lend')
      if user_input in BookItem.book:
        print(f'the book{user_input} is issued')
        print(f'the issued date is {self.d.creation_date}')
        print(f'the due date is {self.d.due_day}')
        Person.dic[Person.member_id].append(user_input)


      else:
        print('Book is not available')
    except:
      print('try it again')
          
#
#
#
# a = Address('Karachi','Pakistan')
# a.lib()
# print('WELCOME IN OUR STUDENT LIBRARY')
# name = input('Enter your name')
# email = input('Enter your email')
# p = Person(name,email)
# p.user_info()
# r = BookReservation()
# while True:
#     print('************ FEATURES **************\n'\
#     '1. Display book\n'\
#     '2. Lend book\n' \
#     '3. Reserve book\n' \
#     '4. Add book\n' \
#     '5. Return book\n'\
#     'press any to exit')
#     try:
#         user = int(input('Enter your choice \n>>>'))
#         if user == 1:
#             print(BookItem.book.keys())
#         elif user == 2:
#             l = BookLending()
#             print('You have 10 days to return the book')
#             l.lend_book()
#         elif user == 3:
#             r.fetch_reservation_details()
#         elif user == 4:
#             r.add_book()
#         elif user == 5:
#             r.return_book()
#
#     except:
#         print('user log' ,Person.dic)
#         break






