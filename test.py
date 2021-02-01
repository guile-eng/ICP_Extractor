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

    config['DEFAULT'] = {"1": "Al 308.215",
                         "2": "Ca 430.253",
                         "3": "P 213.618",
                         "4": "K 766.491",
                         "5": "Na 589.592",
                         "6": "Fe 238.204",
                         "7": "/",
                         "8": "As 188.980",
                         "9": "B 249.772",
                         "10": "Cd 214.439",
                         "11": "Co 258.033",
                         "12": "Cr 267.716",
                         "13": "Cu 327.395",
                         "14": "Hg 194.164",
                         "15": "Mg 279.553",
                         "16": "Mn 257.610",
                         "17": "Mo 202.032",
                         "18": "Ni 225.385",
                         "19": "Ni 227.877",
                         "20": "Pb 220.353",
                         "21": "Sb 206.834",
                         "22": "Si 251.611",
                         "23": "Sn 189.925",
                         "24": "Ti 336.122",
                         "25": "V 319.068",
                         "26": "Zn 213.857",
                         "27": "Zn 472.215"}

    with open('setup.ini', 'w') as configfile:
        config.write(configfile)


def rconfig():
    global config
    config = configparser.ConfigParser()

    if len(config.read('setup.ini'))==0:
        configfile()
        rconfig()
    else:
        config.read('setup.ini')


    
rconfig()

for key,value in config.items('DEFAULT'):
    print(f'"{key}":"{value}",')


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
