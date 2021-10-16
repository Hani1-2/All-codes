from tkinter import*
# rt=Tk()
# # def converter():
# #     c=float(e.get())
# #     F=c*9/5+32
# #     l2=Label(rt,'fahrenheit'+str(F))
# #     l2.grid(row=2)
# #
# #
# #
# #
# #
# #
# #
# #
# # rt=Tk()
# # l1=Label(rt,text='enter temp:')
# # l1.grid(row=0,column=0)
# # e=Entry(rt)
# e.grid(row=0,column=1)
# b=Button(rt,text='convert',command=converter)
# b.grid(row=1)
# rt.mainloop()
# r=Tk()
# r.title('haniya')
# l1=Label(r,text='you are here')
# l1.pack()
# r.mainloop()
# lst=[['7','8','9'],['4','5','6'],['1','2','3'],['*','0','#']]
# rt=Tk()
# rt.title('DIALPAD')
# f=Frame(rt)
# for r in range (4):
#     for c in range(3):
#         l1=Label(f,text=lst[r][c])
#         l1.grid(row=r,col=c,relief='RAISED')
# f.pack()
# rt.mainloop()
# a=100
# b=456
# if a>b:
#     print('hello')
# else:
#     print('bye')
# l=['haniya','sameer','rumaisa']
import numpy as np
import cv2

img = cv2.imread('capstone_image.PNG' , cv2.IMREAD_GRAYSCALE)
original_image = cv2.imread('capstone_image.PNG',1)
img = cv2.GaussianBlur(img, (5,5), 0)
cv2.imshow('Detected Coins' , original_image)
cv2.waitkey(0)
cv2.destroyAIWindows()











