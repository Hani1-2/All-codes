# # Slide 6
#
# Contacts=[]
#
# #Adding contacts
# Contacts.append(['Maria Waqas', '111', 'mariaw@neduet.edu.pk'])
# Contacts.append(['Ibshar Ishrat', '222', 'ibshar@neduet.edu.pk'])
#
# #Printing the phonebook
# print(Contacts)
#
# #Sorting the phonebook name-wise
# Contacts.sort()
# print(Contacts)
#
# #Searching a contact by first or last name
# #write a function
#
#
#
# #Slide 7,8,9
#
# class PhoneBook:
#
#    def __init__(self):
#        self.contacts=[]
#
#    #Adding contacts
#    def addContact(self,name,phone,email):
#        self.contacts.append([name,phone,email])
#
#    #Printing the phonebook
#    def __str__(self):
#        strg='Name,Phone No., Email\n'
#        for item in self.contacts:
#            strg+=item[0]+', '+item[1]+', '+item[2]+'\n'
#        return strg
#
#    #Sorting the phonebook name-wise
#    def sortContacts(self):
#        self.contacts.sort()
#
#    #Searching a contact by first or last name
#    #implement the method
#
# Book1=PhoneBook()
# Book1.addContact('Maria Waqas','111','mariaw@neduet.edu.pk')
# Book1.addContact('Ibshar Ishrat','222','ibshar@neduet.edu.pk')
# print(Book1)
# Book1.sortContacts()
# print(Book1)



###Slide 10,11,12
##
class PhoneBook(list):

   #Adding contacts
   #Explicit definition not needed,
   #append method of list can be directly accessed

   #Printing the phonebook
   #Explicit definition not needed,
   #object will be printed as a two dimensional list

   #For pretty printing
   def __str__(self):
       strg='Name,Phone No., Email\n'
       for item in self:
           strg+=item[0]+', '+item[1]+', '+item[2]+'\n'
       return strg

##    #For even prettier printing
##    def __str__(self):
##        temp='{name:20}{phone:15}{email:20}\n'
##        strg='Name                Phone          Email\n'
##        for item in self:
##            strg+=temp.format(name=item[0],phone=item[1],email=item[2])
##        return strg


   #Sorting the phonebook name-wise
   #Explicit definition not needed,
   #sort method of list can be directly accessed

   #Searching a contact by first or last name
   def search(self,name):
       contactsFound=PhoneBook()
       for item in self:
           if name in item[0]:
               contactsFound.append(item)
       return contactsFound


Book1=PhoneBook()
Book1.append(['Maria Waqas','111','mariaw@neduet.edu.pk'])
Book1.append(['Ibshar Ishrat','222','ibshar@neduet.edu.pk'])
print(Book1)
Book1.sort()
print(Book1)
print(Book1.search('Maria'))



#Slide 13

# class String(str):
#    def wordCount(self):
#        l=self.split(' ')
#        return len(l)
#
# sentence=String('I am Maria Waqas, your teacher for the course CS-116')
# print(sentence.wordCount())