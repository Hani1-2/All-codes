###Slide 17,18
##
##from tkinter import Tk,Label,Entry,Button
##
##def convertToFah():
##    answer=int(e1.get())*9/5+32
##    l2=Label(root,text='Equivalent temperature in Fahrenheit is '+str(answer))
##    l2.pack()
##
##
##root=Tk()
##root.minsize(300,200)
##root.maxsize(500,400)
##root.title('Temperature Converter')
##
##l1=Label(root,text='Enter temperature in Celsius: ')
##l1.pack()
##e1=Entry(root)
##e1.pack()
##b1=Button(root,text='Convert',command=convertToFah)
##b1.pack()
##
##root.mainloop()



###Slide 19,20
##
# from tkinter import Tk,Label,Entry,Button
#
# class TempConverter:
#    def __init__(self):
#        self.root=Tk()
#        self.root.minsize(300,200)
#        self.root.maxsize(500,400)
#        self.root.title('Temperature Converter')
#        self.createConverter()
#        self.root.mainloop()
#    def createConverter(self):
#        l1=Label(self.root,text='Enter temperature in Celsius: ')
#        l1.pack()
#        self.e1=Entry(self.root)
#        self.e1.pack()
#        b1=Button(self.root,text='Convert',command=self.convertToFah)
#        b1.pack()
#    def convertToFah(self):
#        answer=int(self.e1.get())*9/5+32
#        l2=Label(self.root,text='Equivalent temperature in Fahrenheit is '+str(answer))
#        l2.pack()
#
# t=TempConverter()



###Slide 21,22
##
# from tkinter import Tk,Label,Entry,Button
#
# class TempConverter(Tk):
#    def __init__(self):
#        super().__init__()
#        self.minsize(300,200)
#        self.maxsize(500,400)
#        self.title('Temperature Converter')
#        self.createConverter()
#        self.mainloop()
#
#    def createConverter(self):
#        l1=Label(self,text='Enter temperature in Celsius: ')
#        l1.pack()
#        self.e1=Entry(self)
#        self.e1.pack()
#        b1=Button(self,text='Convert',command=self.convertToFah)
#        b1.pack()
#
#    def convertToFah(self):
#        answer=int(self.e1.get())*9/5+32
#        l2=Label(self,text='Equivalent temperature in Fahrenheit is '+str(answer))
#        l2.pack()
#
# t=TempConverter()