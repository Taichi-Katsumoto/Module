'''
Created on 2019/04/10

@author: Taichi
'''
import tkinter
from tkinter import ttk

def lab(text,width,column,row):
    A=tkinter.Label(text=text,width=width)
    A.grid(column=column,row=row)
    return A

def Ent(text,width,column,row):
    A=tkinter.Entry(width=width)
    A.insert(tkinter.END,text)
    A.grid(column=column,row=row)
    return A

def Check(text,width,column,row,var,ONOFF):
    var.set(ONOFF)
    A=tkinter.Checkbutton(text=text,variable=var,width=width)
    A.grid(column=column,row=row)
    return A

def Butt(root,text,width,column,row,command):
    A=tkinter.Button(root,text=text,command=command,width=width)
    A.grid(column=column,row=row)
    return A

def Combo(root,var,value,state,text,width,column,row):
    A=ttk.Combobox(root,textvariable=var,state=state,values=value,width=width)
    A.set(text)
    A.grid(column=column,row=row)
    return A