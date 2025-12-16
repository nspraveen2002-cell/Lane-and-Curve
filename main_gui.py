from tkinter  import *
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
def fun1():
    runfile('straight_lane_detection.py')

def fun2():
    runfile('advanced_lane_find.py')

def fun3():
    runfile('curved_lane_detection.py')



win=Tk()
win.geometry("750x550")
L1 = Label(win,text="LANE AND CURVE DETECTION",font=("bookman old style",20))
L1.grid(row=0,column=1,padx=10,pady=10)

#b1 = Button(win,text="LANE LINE DETECTION".center(42,' '),font=("bookman old style",20), bg='blue', fg='white', command=fun1)
#b1.grid(row=1,column=1,padx=10,pady=10)

b2 = Button(win,text=" LANE DETECTION".center(40,' '),font=("bookman old style",20), bg='orange', fg='black', command=fun2)
b2.grid(row=2,column=1,padx=10,pady=10)

b3 = Button(win,text="ADVANCED LANE AND CURVE DETECTION".center(40,' '),font=("bookman old style",20), bg='green', fg='white', command=fun3)
b3.grid(row=3,column=1,padx=10,pady=10)


win.mainloop()





