from tkinter import *
import pandas as pd
import numpy as np
from pandas import DataFrame as df
from tkinter import filedialog
import matplotlib.pyplot as plt
from tkinter import messagebox, ttk
import tkinter as tk
from datetime import datetime

#############root window
root= Tk()
root.title(" ICP Data Extractor by Mr.Gee (v. 1.1)")

frame1=LabelFrame(root,padx=10, pady=10, bd=0)
frame1.grid(row=0, column=0)

def current_t():
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  return current_time

def frame_csv(reset):
  global framecsv
  if (reset==1):
    framecsv.destroy()
  framecsv=LabelFrame(frame1,text="CSV Report Load Setup",height=50, width=500)
  framecsv.grid(row=0, column=1)

frame_csv(0)

frame2=LabelFrame(frame1,padx=10, pady=10, bd=0)
frame2.grid(row=0, column=0)

frame3=LabelFrame(root,text="  Log",padx=10, pady=10, bd=0)
frame3.grid(row=1, column=0)

def help_w():
  help = Toplevel()
  help.title(" Help")
  help.geometry("500x500")

  frame_about=LabelFrame(help,text="Support/Bugs")
  frame_about.pack(side=TOP)

  frame_h=LabelFrame(help,text="Instructions:", bd=0)
  frame_h.pack(side=TOP)

  
  about = Label(
      frame_about, text='   Developed by: Guilherme Carvalho  \n  email: guicampos96@gmail.com   \n', font=('helvetica', 10))
  about.pack()

  help_t = Text(frame_h, width=60, height=25, font=('helvetica', 9), highlightbackground='gray', spacing2=2)
  help_t.pack()
  help_t.insert(END, """This program extracts and process data from the samples using the ICP exported file
    
1. Open the CSV file

2. Check the Setup options you want 
  
  (noblk= remove the blank samples, nostd= remove the standard samples, nohno3= remove samples that have HNO in their label name, Selec. All Samples = Start the loading screen with all samples selected, Selec. All Samples = Start the loading screen with all elements selected)

3. Load the data

4. Select the samples and the elements that you want in the final report

5. Select the type of report and create the report ("Report" only has concentration column for each sample/element,"Full Report" include all columns, "Calc. Report" calculate the average and standard deviation of the samples by NIR)

The final document will be created in the same folder as the running program
""")
  help_t.configure(state=DISABLED)

#Sample/Elements window

def setupw():
  global setup
  global vars
  global vare
  global f
  global op_v
  l_names()
  setup = Toplevel()
  setup.title(" ICP Data setup")
  setup.geometry("500x450")

  ###########
  frame_s=LabelFrame(setup,text="Samples", cursor="arrow")
  # frame_s.pack(side=tk.LEFT)
  frame_s.place( width=150, x=25)
  
  scrollbary = tk.Scrollbar(frame_s)
  scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
  scrollbarx = tk.Scrollbar(frame_s, orient=HORIZONTAL)
  scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
  checklist = tk.Text(frame_s, width=15)
  checklist.pack(side=tk.BOTTOM, expand=True)


  vars = []
  for i in list_names["Label"]:
    var = tk.BooleanVar()
    checkbutton = tk.Checkbutton(checklist, text=i, variable=var, bg="white")
    vars.append(var)
    checklist.window_create("end", window=checkbutton)
    checklist.insert("end", "\n")
    checklist.config(yscrollcommand=scrollbary.set, cursor="arrow")
    checklist.config(xscrollcommand=scrollbarx.set)
    if (all_s==1):
      checkbutton.select()
    


  scrollbary.config(command=checklist.yview)
  scrollbarx.config(command=checklist.xview)

  
  checklist.configure(state="disabled")# disable the widget so users can't insert text into it




  ############
  frame_e=LabelFrame(setup,text="Elements", cursor="arrow")
  # frame_e.pack(side=tk.LEFT)
  frame_e.place( width=150, x=200)

  scrollbary = tk.Scrollbar(frame_e)
  scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
  scrollbarx = tk.Scrollbar(frame_e, orient=HORIZONTAL)
  scrollbarx.pack(side=tk.BOTTOM, fill=tk.X)
  checklist = tk.Text(frame_e, width=15)
  checklist.pack(side=tk.BOTTOM, expand=True)

  vare = []
  for i in list_elements["Elements"]:
    var = tk.BooleanVar()

    vare.append(var)
    checkbutton = tk.Checkbutton(checklist, text=i, variable=var, bg="white")
    checklist.window_create("end", window=checkbutton)
    checklist.insert("end", "\n")
    checklist.config(yscrollcommand=scrollbary.set, cursor="arrow")
    checklist.config(xscrollcommand=scrollbarx.set)
    if (all_e==1):
      checkbutton.select()


  scrollbary.config(command=checklist.yview)
  scrollbarx.config(command=checklist.xview)

  
  checklist.configure(state="disabled")# disable the widget so users can't insert text into it
  ###############

  frame_calc=LabelFrame(setup,text="Final Report", cursor="arrow",padx=10, pady=10)
  frame_calc.place( width=120, x=370)

  v = tk.IntVar()
  v.set(1)  # initializing the choice, i.e. Python

  options = [("Report", 1),
           ("Full Report", 2),
             ("Calc. Report", 3)]

  def ShowChoice():
    global op_v
    op_v=v.get()

  tk.Label(frame_calc, 
           padx = 20).pack()

  for op, val in options:
      tk.Radiobutton(frame_calc, 
                     text=op,
                     padx = 20, 
                     variable=v, 
                     command=ShowChoice,
                     value=val).pack()

  ShowChoice()
  button_c=Button(frame_calc,text="Create Report", command=filter, height=1, width=225).pack()


def loadcsv():
  global noblank
  global nostd
  global noHNO3
  global all_s
  global all_e

  noblank=a.get()
  nostd=b.get()
  noHNO3=c.get()
  all_s=d.get()
  all_e=e.get()

  l_elements()
  l_samples()
  setupw()


## Functions#######################################################################

def calculate ():
  global v_s
  global v_e
  i=0
  vve=[]
  vvs=[]
  for x in range(len(vars)):
    i=vars[x].get()
    vvs.append(i)
  for x in range(len(vare)):
    i=vare[x].get()
    vve.append(i)

  v_s = pd.DataFrame(vvs)
  v_e = pd.DataFrame(vve, columns=list_elements.columns)



def openFile ():
  frame_csv(1)
  
  global reset
  global pathname
  global csvfile
  global a
  global b
  global c
  global d
  global e

  pathname = filedialog.askopenfilename(initialdir="/user/desktop", title="Select file ...", filetypes= ( ("CSV file", ".csv"),("All files", "*.*") )  )
  file_label=Label(framecsv,text=pathname, height=1, width=50 ).pack(side=BOTTOM)
  csvfile=pd.read_csv(pathname,header=2)
  a= IntVar()
  checknoblk = tk.Checkbutton(framecsv, text="No Blank", variable=a)
  checknoblk.pack(side=LEFT)

  b= IntVar()
  checknostd = tk.Checkbutton(framecsv, text="No Standards", variable=b)
  checknostd.pack(side=LEFT)

  c= IntVar()
  checknohno3 = tk.Checkbutton(framecsv, text="No HNO3", variable=c)
  checknohno3.pack(side=LEFT)

  d= IntVar()
  allsamples = tk.Checkbutton(framecsv, text="Selec. All Samples", variable=d)
  allsamples.pack(side=LEFT)

  e= IntVar()
  allelements = tk.Checkbutton(framecsv, text="Selec. All Elements", variable=e)
  allelements.pack(side=LEFT)


  checknoblk.select()
  checknostd.select()
  checknohno3.select()
  allsamples.select()

  reset=1
 

def l_elements():
  global list_elements
  list_elements=[]
  for n in range(0,len(csvfile.index),1):  
    if (csvfile.iloc[n,3] not in list_elements):
      list_elements.append(csvfile.iloc[n,3])
  T.insert(END,current_t() +" - Elements have been read successfully!\n")
  list_elements=pd.DataFrame(list_elements, columns=["Elements"])

def l_samples():
  global list_samples

  list_samples= csvfile

  if (noblank==1):
    list_samples= list_samples[list_samples['Type']!='BLK']
  if (nostd==1):
    list_samples= list_samples[list_samples['Type']!='STD']
  if (noHNO3==1):
    l_hno=list_samples[~list_samples['Label'].str.contains('HNO', regex=False)]
    list_samples=l_hno
    print(l_hno)

  T.insert(END,current_t() +" - Samples have been read successfully!\n")

def l_names ():
  global list_names
  list_names=[]
  for n in range(0,len(list_samples),len(list_elements)):
    list_names.append(list_samples.iloc[n,])
  list_names=pd.DataFrame(list_names, columns=csvfile.columns)
  list_names=list_names.reset_index(drop=True)
  print(list_names)

def name_sample():

  select_dup1=[]

  for i in select_samples['Label']:
    select_1=i
    t01= select_1.replace('A','')
    t02= t01.replace('B','')
    t03= t02.replace('C','')
    t04= t03.replace('a','')
    t05= t04.replace('b','')
    t06= t05.replace('c','')
    t07= t06.replace('R','')
    t08= t07.replace('r','')
    t09= t08.strip()
    select_dup1.append(t09)
  select_dup=list(dict.fromkeys(select_dup1))

  return select_dup

def filter():
  global select_samples
  global select_elements
  calculate()
  

  select_samples=list_names.loc[v_s[0],:]
  select_elements=list_elements[v_e].dropna()

  average=1

  n=len(list_elements)
  sl=[]
  csv_final=pd.DataFrame(sl, columns=list_samples.columns)

  for x in select_samples.index:
    for y in select_elements["Elements"]:
      select1=list_samples.iloc[n*x:n*x+n,:]
      select2=select1[select1["Element"]==y]
      csv_final=csv_final.append(select2)
    csv_final=csv_final.append(pd.Series(), ignore_index=True)

  print(csv_final)

  if op_v==2:

    print(csv_final)
    csv_final.to_csv('./ICP_Full_Report.csv', index = False)
    T.insert(END,current_t() +" - Full Report has been created !\n")

  elif op_v==3:
    csv_final= csv_final.dropna(how='all')
    select_dup=name_sample()

    list_average=[]
    list_standard=[]
    l01=[]
    l02=[]

    for x in select_dup:
      for y in select_elements['Elements']:
        slc1=csv_final[csv_final['Label'].str.contains(x, regex=False)]
        slc2=slc1[slc1['Element']==y]
        print(slc2)
        slc_avr= pd.to_numeric(slc2['Concentration'], errors='coerce').mean()
        list_average.append(slc_avr)
        slc_std= pd.to_numeric(slc2['Concentration'], errors='coerce').std()
        list_standard.append(slc_std)
        l01.append(x)
        l02.append(y)
      l01.append('')
      l02.append('')
      list_average.append('')
      list_standard.append('')
    
    data={'Label':l01,'Element': l02 , 'Average': list_average, 'STD': list_standard}
    f_rep= pd.DataFrame.from_dict(data)

    print(f_rep)



    f_rep.to_csv('./ICP_Calculated_Report.csv', index = False)
    T.insert(END,current_t() +" - Full Calculated Report has been created !\n")

  elif op_v==1:
    csv_final=csv_final[["Label","Element","Concentration"]]

    print(csv_final)
    csv_final.to_csv('./ICP_Report.csv', index = False)
    T.insert(END,current_t() +" - Report has been created!\n")

 
 

#########################################################################


#Event log

T =Text(frame3, height=10, width=100)
T.grid(row=0) 

T.insert(END, current_t() + " - Click 'Help' button to read the instructions \n")

#Buttons

b_open= Button(frame2, text="Open CSV file",command= openFile, height=1, width=15).grid(row=0,column=0)
b_load= Button(frame2, text="Load data",command= loadcsv, height=1, width=15).grid(row=1,column=0)
button_quit=Button(frame2,text="Exit", command=root.quit, height=1, width=15).grid(row=3, column=0)
button_help=Button(frame2,text="Help", command=help_w, height=1, width=15).grid(row=2, column=0)


root.mainloop()

