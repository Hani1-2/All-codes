# Slide 5, 8

class FileSaver:
   def saveToFile(self,fileName):
       f=open(fileName,'w')
       #try this: f.write(str(self))
       for item in self:
           f.write(str(self)+'\n')
       f.close()

class PhoneBook(list, FileSaver):
   #For pretty printing
   def __str__(self):
       strg='Name,Phone No., Email\n'
       for item in self:
           strg+=item[0]+', '+item[1]+', '+item[2]+'\n'
       return strg

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
Book1.saveToFile('MyFile.txt')
print(Book1)
print(Book1.search('Maria Waqas'))



### Slide 10, 11
#
# class FileSaver:
#    def saveToFile(self,fileName):
#        f=open(fileName,'w')
#        for item in self:
#            f.write(str(item) + '\n')
#        f.close()
#
# class FileReader:
#    def readFromFile(self,fileName):
#        f=open(fileName,'r')
#        for line in f:
#            self.append(eval(line))
#        f.close()
#
# class PhoneBook(list,FileSaver,FileReader):
#    #For pretty printing
#    def __str__(self):
#        strg='Name    ,Phone No., Email\n'
#        for item in self:
#            strg+=item[0]+', '+item[1]+', '+item[2]+'\n'
#        return strg
#
#    #Searching a contact by first or last name
#    def search(self,name):
#        contactsFound=PhoneBook()
#        for item in self:
#            if name in item[0]:
#                contactsFound.append(item)
#        return contactsFound
#
# Book1=PhoneBook()
# Book1.append(['Ibshar Ishrat','2006','osaid@neduet.edu.pk'])
# Book1.append(['Maria Waqas','111','mariaw@neduet.edu.pk'])
# Book1.saveToFile('MyFile.txt')
# Book1.readFromFile('MyFile.txt')
# print(Book1)



### Slide 15, 16
##
# class FileSaver:
#    def saveToFile(self,obj,fileName):
#        f=open(fileName,'w')
#        for item in obj:
#            f.write(str(item)+'\n')
#        f.close()
#
# class FileReader:
#    def readFromFile(self,obj,fileName):
#        f=open(fileName,'r')
#        for line in f:
#            obj.append(eval(line))
#        f.close()
#
# class PhoneBook(list):
#    #For pretty printing
#    def __str__(self):
#        strg='Name,Phone No., Email\n'
#        for item in self:
#            strg+=item[0]+', '+item[1]+', '+item[2]+'\n'
#        return strg
#
#    #Searching a contact by first or last name
#    def search(self,name):
#        contactsFound=PhoneBook()
#        for item in self:
#            if name in item[0]:
#                contactsFound.append(item)
#        return contactsFound
#
#    def saveToFile(self, FileName):
#        fs=FileSaver()
#        fs.saveToFile(self,FileName)
#
#    def readFromFile(self, FileName):
#        fr=FileReader()
#        fr.readFromFile(self,FileName)
#
# Book1=PhoneBook()
# Book1.append(['Ibshar Ishrat','2006','osaid@neduet.edu.pk'])
# Book1.append(['Maria Waqas','111','mariaw@neduet.edu.pk'])
# Book1.saveToFile('MyFile.txt')
# Book1.readFromFile('MyFile.txt')
# print(Book1)

## 2nd heirarchy
# class FileSaver:
#    def saveToFile(self,fileName):
#        f=open(fileName,'w')
#        for item in self:
#            f.write(str(item) + '\n')
#        f.close()
#
# class FileReader:
#    def readFromFile(self,fileName):
#        f=open(fileName,'r')
#        for line in f:
#            self.append(eval(line))
#        f.close()
#
# class PhoneBook(list):
#    #For pretty printing
#    def __str__(self):
#        strg='Name    ,Phone No., Email\n'
#        for item in self:
#            strg+=item[0]+', '+item[1]+', '+item[2]+'\n'
#        return strg
#
#    #Searching a contact by first or last name
# class MyContacts(PhoneBook,FileSaver,FileReader):
#    def search(self,name):
#        contactsFound=PhoneBook()
#        for item in self:
#            if name in item[0]:
#                contactsFound.append(item)
#        return contactsFound
#
# Book1=MyContacts()
# Book1.append(['Ibshar Ishrat','2006','osaid@neduet.edu.pk'])
# Book1.append(['Maria Waqas','111','mariaw@neduet.edu.pk'])
# Book1.saveToFile('MyFile.txt')
# Book1.readFromFile('MyFile.txt')
# print(Book1)
