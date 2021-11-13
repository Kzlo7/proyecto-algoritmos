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

    if nrows==0 and ncols==0:#si el largo de la fila y columna es 0
        if origen==destino:#en el caso  que el origen y el destino sean iguales
            sheet.write(nrows,nrows,"NA")#Se agrega un NA valor nulo a la celda 0,0
            sheet.write(nrows+1,nrows,origen)#columna
            sheet.write(nrows,nrows+1,destino)#Fila
            sheet.write(nrows+1,nrows+1,distancia)#Agrega la distancia
            documento.save("Grafo.xls")
            
    else:
        
        for i in range(0,nrows):#se recorre hasta el largo de la fila
            for j in range(0,ncols):#hasta el largo de la columna
                vertice.append(sh.cell_value(i,j))#se extrae los valores con sus vertices para ser agregadas al grafo
                if "" in vertice:#en el caso que no exista un valor en la celda y es agregada a la lista
                    vertice.remove("")#esta se borra 
            grafo.append(vertice)#Toma la lista vertice y lo agrega al grafo 
            vertice = []#Se resetea el vertice para agrega los siguentes

        n = 0
        seguir = True
        if origen!=destino:#en el caso que sean distintos el origen y el destino
            largo = len(grafo)#se toma el largo del grafo
            while seguir:#seguir hasta que sea Falso
                n +=1#contador 
                if origen in grafo[n] and destino in grafo[0]:#si el origen existe en el grafo y el destino en la posicion 0
                    grafo[n].append(distancia)#se agrega al grafo su distancia 
                    seguir = False
                elif origen in grafo[n] and destino not in grafo[0]:#en el caso que no exista el destino en la posicion 0 y si el origen
                    grafo[0].append(destino)#se agrega el destino
                    grafo[n].append(distancia)#y su distancia
                    seguir = False
                elif origen not in grafo[largo-1]:#en el caso que el origen no exista en el grafo en la ultima posicion en la cual se va agregando
                    grafo.append([origen])#se agrega el origen
                    grafo[largo].append(distancia)#y su distancia ya que el destino ya existe
                    seguir = False
        else:#en la caso que el destino y el origen sean iguales
            seguir = True
            n = 0
            while seguir:
                n +=1
                if origen in grafo[n]:#se busca el origen el grafo
                    grafo[n].append(distancia)#y se agraga su distancia ya que el destino ya existe
                    seguir = False

    for i in range(0,len(grafo)):#se recorre el grafo
        for j in range(0,len(grafo[i])):
            sheet.write(i,j,grafo[i][j])#y se agrega al archivo excel 
    documento.save("Grafo.xls")


