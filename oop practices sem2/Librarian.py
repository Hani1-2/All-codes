from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, id, password, person,email):
    self.__id = id
    self.__password = password
    self.email=email
    self.__person = person
  def resetPassword(self,NewPassword):
      self.__password=NewPassword

class Librarian(Account):
##  Add_Books_in_Library=0
  Total_Books_in_Library=500
  def __init__(self, id=1, password=1234, person='Librarian',email='Lib@gmail.com'):
    super().__init__(id, password, person,email)
  def add_book_item(self,AddBooks):
      AddBooks = int(input('How many book you want to add'))
      self.Add_Books_in_Library=AddBooks
##      global Add_Books_in_Library
      self.Add_Books_in_Library+=Librarian.Total_Books_in_Library
      Librarian.Total_Books_in_Library+=self.Add_Books_in_Library
  def get_Num_Books(self):
##      Total_Books_in_Library=Total_Books_in_Library+Add_Books_in_Library
      return("The Total Number of book present in the Library are",self.Add_Books_in_Library)

# a1=Librarian(1,'rmt','user','rmt')
# a1.add_book_item(500)
# print(a1.get_Num_Books())
# a2=Librarian(1,'rmt','user','rmt')
# a2.add_book_item(200)
# print(a2.get_Num_Books())
