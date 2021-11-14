from os import fdopen, path
import tkinter
from tkinter.constants import CENTER, COMMAND, Y
from numpy.lib.shape_base import tile
import pandas as pd
import tkinter as tk
from tkinter import Grid, Image, Label, Misc, PhotoImage, ttk


l1=pd.read_excel("kk.xlsx")

asd1=l1.columns.array

xx=[]


for j in asd1:
    j = j
    xx.append(j)

xx.pop(0)

grafo=[]
for k in xx:
    t1=l1[k]
    t2=[]
    for j in t1:
        t2.append(j)
    grafo.append(t2)


def dij(graf, src,op2):
    d1=len(graf)
    d2=len(graf[0])
    infi=999999999


    dist=[float(infi)]*d1
    punt=[-1]*d1
    dist[src]=0

    cola=[]
    for i in range(d1):
        cola.append(i)
    
    while cola:
        min=float(infi)
        min_index=-1
        for i in range(len(dist)):
            if(dist[i]<min and i in cola):
                min=dist[i]
                min_index=i
        u=min_index
        cola.remove(u)

        for i in range(d2):
            if graf[u][i] and i in cola:
                if (dist[u] + graf[u][i]<dist[i]):
                    dist[i]=dist[u]+graf[u][i]
                    punt[i]=u
    ll=[]
    def mostrarcamino(punt,j,xx):
        if(punt[j]==-1):
            ll.append(xx[j])
            return
        mostrarcamino(punt,punt[j],xx)
        ll.append(xx[j])
    mostrarcamino(punt,op2,xx)
    return ll
#######################################################
# Creating tkinter window
window = tk.Tk()
window.title('MHB Shortest Jobs SpA')
window.geometry('1100x900')
  
# label text for title
ttk.Label(window, text = "MHB Shortest Jobs SpA", 
          background = 'green', foreground ="white", 
          font = ("Times New Roman", 15)).grid(row = 0, column = 1)
img=tk.PhotoImage(file="metro.png") 
# label
t1=ttk.Label(window, text = "Selecciona la estacion de inicio :",
          font = ("Times New Roman", 10))#.grid(column = 1,
          #row = 5, padx = 10, pady = 25,columnspan=1)
t2=ttk.Label(window, text = "Selecciona la estacion de destino :",
          font = ("Times New Roman", 10))#.grid(column = 1,
          #row = 6, padx = 10, pady = 25)
m1=Label(window,image=img,).grid(column = 1,row = 1)
t1.grid(column=0,row=5)
t2.grid(column=0,row=6)

#img=tkinter.PhotoImage(file="metro.png")

# Combobox creation

n = tk.StringVar()
n2 = tk.StringVar()
list = ttk.Combobox(window, textvariable = n)
list1 = ttk.Combobox(window, textvariable = n2)
def klk(xx):
    c1=0
    for i in range(0,len(xx)):
        if(list.get()==xx[i]):
            c1=i
            break
    return c1
def klk1(xx):
    c1=0
    for i in range(0,len(xx)):
        if(list1.get()==xx[i]):
            c1=i
            break
    return c1
f2=Label(wraplength=500)
f3=Label()
f2.grid(column=1,row=8)
f3.grid(column=1,row=9)
def fff():
    mm=dij(grafo,klk(xx),klk1(xx))
    f2["text"]="la ruta mas corta es: "+str(mm)
    f3["text"]="La cantidad de estaciones es: "+str(len(mm))
#list.bind("<<ComboboxSelected>>",lambda _ : fff()) and list1.bind("<<ComboboxSelected>>",lambda _ : fff())

# Adding combobox drop down list
list1["values"]=(xx)
list['values'] = (xx)
b1=tkinter.Button(window,text="Calcular ruta",command=lambda: fff())
list.grid(column = 1, row = 5)
list1.grid(column=1, row= 6)
b1.grid(column=1,row=7)

list.current()

window.mainloop()
