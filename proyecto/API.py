#!/usr/bin/env python
# -*- coding: utf-8 -*-
##proyecto inicio 05-11-2021

import requests
import SaveExcel as SE


archivo = open("estaciones.txt",encoding ="utf8")

datos = archivo.read().replace(" ","+")
datos = datos.lower().split("\n")


for i in range(0,len(datos)):
    for j in range(0,len(datos)):
        if datos[i]==datos[j]:#en el caso que las estaciones sean iguales se ingrese cero
            SE.Grafo(datos[i],datos[j],0)
        else:#en el caso que sean distintas
            url = ("https://maps.googleapis.com/maps/api/distancematrix/json?origins=Metro%metro+"
                   +str(datos[i])+",region+metropolitana"+"&destinations=Metro%metro+"
                   +str(datos[j])+",region+metropolitana"+"&key=AIzaSyD_VKKZ2ZyZIJ9DaBto4IpK2Z8lj2HInJ0")
            response = requests.get(url)
            json_response = response.json()
            distancia = json_response["rows"][0]["elements"][0]["distance"]["text"]
            distancia = distancia.replace(" km","")
            SE.Grafo(datos[i],datos[j],distancia)



            
            















