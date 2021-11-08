##proyecto inicio 05-11-2021
import requests
import pandas as pd
l1=pd.read_excel("esta.xlsx")
asd1=l1.columns.array
xx=[]
for j in asd1:
    xx.append(j)
print(xx)


#k1="AIzaSyD_VKKZ2ZyZIJ9DaBto4IpK2Z8lj2HInJ0"

#url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=Metro%Einstein&destinations=Metro%Zapadores&key=AIzaSyD_VKKZ2ZyZIJ9DaBto4IpK2Z8lj2HInJ0"


#response = requests.get(url)

#print(response.text)

import pandas as pd

MAX_value = 999999

l1=pd.read_excel("kk.xlsx")

asd1=l1.columns.array

xx=[]


for j in asd1:
    xx.append(j)

xx.pop(0)

grafo=[]
for k in xx:
    t1=l1[k]
    t2=[]
    for j in t1:
        t2.append(j)
    grafo.append(t2)
print(grafo)








