from tkinter import *
import tkinter
from tkinter import ttk
import pandas as pd
import operator
from os import dup2, fdopen, path, terminal_size
import tkinter
from tkinter.constants import CENTER, COMMAND, Y
from typing import Text
from numpy.lib.shape_base import tile
import pandas as pd
import tkinter as tk
from tkinter import Grid, Image, Label, Misc, PhotoImage, ttk
import operator

###########################################
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
###########################################
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
    p=[]
    c1=[]
   
    def mostrarcamino(punt,j,xx):
        if(punt[j]==-1):
            ll.append(xx[j])
            return
        mostrarcamino(punt,punt[j],xx)
        ll.append(xx[j])
        
    mostrarcamino(punt,op2,xx)
    ñ9=round(dist[op2],2)
    p.append(ñ9)
    c1.append(ll)
    c1.append(p)
    return c1

###############################################################
v=Tk()
v.title("Minimal Routes")
v.geometry("1010x753")
im=PhotoImage(file="press.png")
fondo=Label(image=im,text="imagen 5.0 de fonde",bd=0)

fondo.place(x = 0, y = 0, relwidth = 1, relheight = 1)

v2 = Toplevel(v)
v2.geometry("392x568")
im1=PhotoImage(file="tr.png")
im2=PhotoImage(file="boton.png")
im3=PhotoImage(file="boton1.png")
im4=PhotoImage(file="UNO.png")

fondo1=Label(v2,image=im1,text="imagen 5.0 de fonde",bd=0)
fondo1.place(x = 0, y = 0, relwidth = 1, relheight = 1)
v2.title("Traslados")

def uno():
    if(b1.getboolean(s=TRUE)):
        v3=Toplevel(v2)
        v3.geometry("863x404")
        v3.title("Traslado 1:1")
        fondo1=Label(v3,image=im4,text="imagen 5.0 de fonde",bd=0)
        fondo1.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        f2=Label(v3,wraplength=250)
        f3=Label(v3)
        n = tk.StringVar()
        n2 = tk.StringVar()
        list = ttk.Combobox(v3,state="readonly", textvariable = n)
        list1 = ttk.Combobox(v3,state="readonly", textvariable = n2)
        list1["values"]=(xx)
        list['values'] = (xx)
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
       
        def fff():
            mm=dij(grafo,klk(xx),klk1(xx))
            tt=str(mm[0])
            tt1=str(mm[1])
            f2["text"]="Los locales visitados son: "+tt
            f3["text"]="Con una distancia de: "+tt1+"KM"
            f2.place(x=521,y=230)
            f3.place(x=521,y=200)    
        b2=tkinter.Button(v3,text="Calcular ruta",command=lambda: fff())
        b2.place(x=554,y=95)
        list.place(x=521,y=28)
        list1.place(x=521,y=68)
        list.current()
        v3.mainloop()
           
def dos():
    if(b2.getboolean(s=TRUE)):
        v3=Toplevel(v2)
        v3.geometry("392x568")
        v3.title("Traslado 1:3")
        n = tk.StringVar()
        list = ttk.Combobox(v3,state="readonly", textvariable = n)
        list["values"]=(xx)
        list.grid(column=1,row=1)
        def unotres(u):
            v=0
            for i in range(0,len(xx)):
                if(u==xx[i]):
                    v=i
            return grafo[v]
        def tresp(ini):
            dic={}
            for i in range(0,len(ini)):
                dic[i]=ini[i]
    
            dicor = sorted(dic.items(), key=operator.itemgetter(1))
            m1=dicor[1]
            m2=dicor[2]
            m3=dicor[3]
            return m1,m2,m3
        d1=tk.Button(v3)
        d2=tk.Button(v3)
        d3=tk.Button(v3)
        def p2(u):
            ini=unotres(u)
            cer=tresp(ini)
            d1["text"]=str(xx[cer[0][0]])
            d2["text"]=str(xx[cer[1][0]])
            d3["text"]=str(xx[cer[2][0]])
            d1.grid(column=3,row=3)
            d2.grid(column=3,row=4)
            d3.grid(column=3,row=5)
            if(d1.getboolean(s=TRUE)):
                return p2(xx[cer[0][0]])
            elif(d2.getboolean(s=TRUE)):
                return p2(xx[cer[1][0]])
            elif(d3.getboolean(s=TRUE)):
                return p2(xx[cer[2][0]])
            else:
                return 0
                
            """for i in cer:
                #print(str(cn)+".-"+str(xx[i[0]])+" Con una distancia de: "+str(i[1])+"KM")
                #jk="d"+str(cn)
                tt=str(xx[i[0]])
                d1=tk.Button(v3,text=str(xx[cer[0][0]])).grid(column=3,row=3)
                d2=tk.Button(v3,text=str(xx[cer[1][0]])).grid(column=3,row=3)
                d3=tk.Button(v3,text=str(xx[cer[2][0]])).grid(column=3,row=3)
                if(op==1):
                    return p2(xx[cer[op-1][0]])
                    print("===============================")
                elif(op==2):
                    return p2(xx[cer[op-1][0]])
                    print("===============================")
                elif(op==3):
                    return p2(xx[cer[op-1][0]])
                    print("===============================")
                else:
                    print("xxx")
                    print("===============================")
                cn=cn+1
            op=int(input("Cual opcion desea tomar: "))
            if(op==1):
                return p2(xx[cer[op-1][0]])
                print("===============================")
            elif(op==2):
                return p2(xx[cer[op-1][0]])
                print("===============================")
            elif(op==3):
                return p2(xx[cer[op-1][0]])
                print("===============================")
            else:
                print("xxx")
                print("===============================")"""
        b3=tkinter.Button(v3,text="Calcular ruta",command=lambda: p2(list.get()))
        b3.grid(column=2,row=2)
b1=tkinter.Button(v2,image=im2,command=uno)
b1.place(x=5,y=120)
b2=tkinter.Button(v2,image=im3,command=dos)
b2.place(x=175,y=485)




    




v.mainloop()
