import xlwt
import xlrd

def Grafo(origen,destino,distancia):
    documento = xlwt.Workbook(encoding="uft-8")
    sheet = documento.add_sheet("Distancia",cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    libro = xlrd.open_workbook("Grafo.xls")
    sh = libro.sheet_by_name("Distancia")
    nrows = sh.nrows#largo filas
    ncols = sh.ncols#largo columna
    vertice = []
    grafo = []

    if nrows==0 and ncols==0:
        if origen==destino:
            sheet.write(nrows,nrows,"NA")
            sheet.write(nrows+1,nrows,origen)#columna
            sheet.write(nrows,nrows+1,destino)#Fila
            sheet.write(nrows+1,nrows+1,distancia)#Agrega la distancia
            documento.save("Grafo.xls")
            
    else:
        
        for i in range(0,nrows):
            for j in range(0,ncols):
                vertice.append(sh.cell_value(i,j))
                if "" in vertice:
                    vertice.remove("")
            grafo.append(vertice)
            vertice = []

            n = 0
            seguir = True
        if origen!=destino:
            largo = len(grafo)
            while seguir:
                n +=1
                if origen in grafo[n] and destino in grafo[0]:
                    grafo[n].append(distancia)
                    seguir = False
                elif origen in grafo[n] and destino not in grafo[0]:
                    grafo[0].append(destino)
                    grafo[n].append(distancia)
                    seguir = False
                elif origen not in grafo[largo-1]:
                    grafo.append([origen])
                    grafo[largo].append(distancia)
                    seguir = False
        else:
            seguir = True
            n = 0
            while seguir:
                n +=1
                if origen in grafo[n]:
                    print(grafo[n])
                    grafo[n].append(distancia)
                    seguir = False

    for i in range(0,len(grafo)):
        for j in range(0,len(grafo[i])):
            sheet.write(i,j,grafo[i][j])
    documento.save("Grafo.xls")


