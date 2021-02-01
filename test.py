from tkinter.constants import ANCHOR
from numpy.lib.function_base import append
from numpy.lib.shape_base import split
import pandas as pd
import numpy as np
from pandas import DataFrame as df
import tkinter as tk
from tkinter import LabelFrame, Listbox, Toplevel, messagebox, ttk, filedialog
from datetime import datetime
import re
import configparser



def configfile():

    config = configparser.ConfigParser()

    config['DEFAULT'] = {'data': '45', 'template': 'yes', 'asd': '9'}

    config['TEMPLATE'] = {'Al': '' , '/': ''}

    with open('setup.ini', 'w') as configfile:
        config.write(configfile)


def rconfig():
    global config
    config = configparser.ConfigParser()
    config.read('setup.ini')

configfile()
rconfig()

for key in config['TEMPLATE']:
    print(key)


setup = tk.Tk()
setup.title('teste')
setup.geometry("400x400")

# List box all elements
frame_e= LabelFrame(setup, text="Elements")
frame_e.place(width=150, x=200, height=200)

scrollbary = tk.Scrollbar(frame_e)
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
scrollbarx = tk.Scrollbar(frame_e, orient=tk.HORIZONTAL)
scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
elements = tk.Listbox(frame_e)
elements.pack(side=tk.BOTTOM, expand=True)

# List box selected elements

frame_e1 = LabelFrame(setup, text="Selected elements")
frame_e1.place(width=150, x=200, height=200, y=200)

scrollbary = tk.Scrollbar(frame_e1)
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
scrollbarx = tk.Scrollbar(frame_e1, orient=tk.HORIZONTAL)
scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
elements1 = tk.Listbox(frame_e1)
elements1.pack(side=tk.BOTTOM, expand=True)


#Valores
for i in range(7):
    elements.insert(tk.END, f'olá {i}')
    elements1.insert(tk.END, f'tudo bem {i}')

def adicionar(self):
    # print(elements.get(tk.ANCHOR))
    print(elements.get(tk.ANCHOR))
    elements1.insert(0, elements.get(tk.ANCHOR))

def remover(self):
    print(elements1.get(tk.ANCHOR))
    elements1.delete(elements1.curselection())

elements.bind('<Double-Button-1>', adicionar)
elements1.bind('<Double-Button-1>', remover)

def get_sel():
    a=elements1.get(0,tk.END)
    
    return print(a)



b_get = tk.Button(setup, text="Botao",
                   command=configfile, height=1, width=15)
b_get.pack()

setup.mainloop()
