# #Slide 4,5
# #
# from tkinter import Tk,Label,Entry,Button
#
# class TempConverter(Tk):
#    def __init__(self):
#        super().__init__()
#        self.minsize(300,200)
#        self.maxsize(500,400)
#        self.title('Temperature Converter')
#        self.createConverter()#it help widget to place in the window , this self id due to initiator
#        self.mainloop()
#    def createConverter(self):
#        l1 = Label(self, text='Enter temperature in Celsius: ')
#        l1.pack()
#        self.e1 = Entry(self)
#        self.e1.pack()
#        b1 = Button(self, text='Convert', command=self.convertToFah)
#        b1.pack()
#
#    def convertToFah(self):
#        answer = int(self.e1.get()) * 9 / 5 + 32
#        l2 = Label(self, text='Equivalent temperature in Fahrenheit is ' + str(answer))
#        l2.pack()
#
# t = TempConverter()


# class createConverter:
#    def __init__(self,r):
#        self.root=r
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
# from tkinter import Tk,Label,Entry,Button,Frame
#
# class TempConverter(Tk):
#    def __init__(self):
#        super().__init__()
#        self.minsize(300,200)
#        self.maxsize(500,400)
#        self.title('Temperature Converter')
#        c=createConverter(self)
#        self.mainloop()
#
# class createConverter(Frame):
#    def __init__(self,r):
#        super().__init__(r)
#        l1=Label(self,text='Enter temperature in Celsius: ')
#        l1.pack()
#        self.e1=Entry(self)
#        self.e1.pack()
#        b1=Button(self,text='Convert',command=self.convertToFah)
#        b1.pack()
#        self.pack()
#    def convertToFah(self):
#        answer=int(self.e1.get())*9/5+32
#        l2=Label(self,text='Equivalent temperature in Fahrenheit is '+str(answer))
#        l2.pack()
#
# t=TempConverter()



###Slide 6,7
##



###Slide 12
##
# from tkinter import Tk, Canvas
#
# class MyCanvas(Tk):
#    def __init__(self):
#        super().__init__()
#        myCanvas=Canvas(self,width=500,height=500,background='pink')
#        myCanvas.create_line(10,10,50,10,fill='black',width=4)
#        myCanvas.create_arc(20,20,100,100,fill='black')
#        myCanvas.create_rectangle(150,150,250,200,fill='red')
#        myCanvas.create_text(125,125,text='Python')
#        myCanvas.pack()
#        self.mainloop()
#
# m=MyCanvas()

#
#
# #Slide 15,16,17
#
# from tkinter import Tk,Label,Entry,Button,Frame,Canvas
#
# class GraphPlotter(Tk):
#    def __init__(self):
#        super().__init__()
#        self.minsize(500,500)
#        self.title('My Line Graph Plotter')
#        c=LineGraph(self)
#        self.mainloop()
#
# class LineGraph(Frame):
#    def __init__(self,r):
#        super().__init__(r)
#        l1=Label(self,text='Equation of line is y=mx+c')
#        l1.pack()
#        l2=Label(self,text='Enter value for m: ')
#        l2.pack()
#        self.e1=Entry(self)
#        self.e1.pack()
#        l3=Label(self,text='Enter value for c: ')
#        l3.pack()
#        self.e2=Entry(self)
#        self.e2.pack()
#        b1=Button(self,text='Draw Line',command=self.drawLine)
#        b1.pack()
#        self.pack()
#    def drawLine(self):
#        #calculating y for x in range 0 to 399
#        y=[]
#        m=int(self.e1.get())
#        c=int(self.e2.get())
#        for x in range (400):
#            y.append(m*x+c)
#        c1=Canvas(self, width=400,height=400,background='red')
#        for x in range (399):
#            c1.create_line(x,400-y[x],x+1,400-y[x+1],fill='black',width=4)
#        c1.pack()
#
# g=GraphPlotter()



###Slide 20,21
# ##
# from tkinter import Tk,Label,Entry,Button,Frame,Canvas
# import matplotlib.pyplot as plt
#
# class GraphPlotter(Tk):
#    def __init__(self):
#        super().__init__()
#        self.minsize(500,500)
#        self.title('My Line Graph Plotter')
#        c=LineGraph(self)
#        self.mainloop()

# class LineGraph(Frame):
#    def __init__(self,r):
#        super().__init__(r)
#        l1=Label(self,text='Equation of line is y=mx+c')
#        l1.pack()
#        l2=Label(self,text='Enter value for m: ')
#        l2.pack()
#        self.e1=Entry(self)
#        self.e1.pack()
#        l3=Label(self,text='Enter value for c: ')
#        l3.pack()
#        self.e2=Entry(self)
#        self.e2.pack()
#        b1=Button(self,text='Draw Line',command=self.drawLine)
#        b1.pack()
#        self.pack()
#    def drawLine(self):
#        #calculating y for x in range 0 to 399
#        x=[]
#        y=[]
#        m=int(self.e1.get())
#        c=int(self.e2.get())
#        for i in range (400):
#            x.append(i)
#            y.append(m*i+c)
#        plt.plot(x,y)
#        plt.xlabel('x')
#        plt.ylabel('y')
#        plt.title('My Line Graph')
#        plt.show()

#g=GraphPlotter()
# class LineGraph(Frame):
#    def __init__(self,r):
#        super().__init__(r)
#        l1=Label(self,text='input a list of x values')
#        l1.pack()
#        self.e1=Entry(self)
#        self.e1.pack()
#        l2=Label(self,text='input a list of y values ')
#        l2.pack()
#        self.e2=Entry(self)
#        self.e2.pack()
#        l3=Label(self,text='input a label for x values')
#        l3.pack()
#        self.e3=Entry(self)
#        self.e3.pack()
#        l4=Label(self,text='input a label for y values')
#        l4.pack()
#        self.e4=Entry(self)
#        self.e4.pack()
#        b1=Button(self,text='Draw Line',command=self.drawLine)
#        b1.pack()
#        self.pack()
#
#    def drawLine(self):
#        # calculating y for x in range 0 to 399
#        # x = []
#        # y = []
#        x_axis = self.e1.get()
#        y_axis = self.e2.get()
#        label_x = self.e3.get()
#        label_y = self.e4.get()
#        x1=x_axis.split(',')
#        x1=[int(i)for i in x1]
#        y1=y_axis.split(',')
#        y1=[int(i)for i in y1]
#        plt.plot(x1, y1)
#        plt.xlabel(label_x)
#        plt.ylabel(label_y)
#        plt.title('My Line Graph')
#        plt.show()
# g= GraphPlotter()
#
from abc import ABC , abstractmethod
class a:
    b = 1
    @abstractmethod
    def c(self):
        print(a.b)
class d :
    def c(self):
        print(a.b)
w = d()
w.c()
