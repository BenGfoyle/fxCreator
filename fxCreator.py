# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:22:45 2019

@author: bguilfoyle
Overview: Create a polynomial based on user defined perameters with a GUI
"""

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
from tkinter import *
pi = np.pi
sin = np.sin; cos = np.cos; tan = np.tan;
sinh = np.sinh; cosh = np.cosh; tanh = np.tanh;

#==============================================================================
def makePlot(x,y):
    """
    Overview: Make a plot of x vs y
    """
    plt.plot(x,y)
    plt.title("f(x) vs x")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.xlim(x[0],x[len(x) -1])
    plt.ylim(min(y),max(y))
    plt.grid()
    plt.show()
#==============================================================================
def calculate():
    eq = []; x1 = eval(txt2.get()); x2 = eval(txt3.get())
    for x in np.arange(x1,x2, (x2 - x1) / 1000):
        eq.append(eval(txt1.get()))
    xRange = np.linspace(x1,x2,len(eq))
    makePlot(xRange,eq)
#==============================================================================
"""
GUI
"""
#Define window, name, and parameters
window = Tk()
window.title("Function Generator")
window.geometry('450x300')

#Insert text with user input text field.
lbl1 = Label(window, text = "Enter an equation")
lbl1.grid(column = 0, row = 0)

txt1 = Entry(window, width = 20)
txt1.grid(column = 0, row = 1)

#button that runs "clicked" function on click
btn1 = Button(window, text = "Make Plot", command = calculate)
btn1.grid(column = 0, row = 4)

lbl2 = Label(window, text = "x range")
lbl2.grid(column = 0, row = 2)

txt2 = Entry(window, width = 10)
txt2.grid(column = 0, row = 3)
txt3 = Entry(window, width = 10)
txt3.grid(column = 1, row = 3)

#loop until closed
window.mainloop()
#==============================================================================
