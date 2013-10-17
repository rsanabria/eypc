import re
#Variables Y Constante
archivo = []
archivo_lineas = []
mne = []
mnemonicos =[]
mne_inh = []
mne_rel = []
reservadas = ["EQU", "ORG", "FCB", "END"]
dvariables = {}
valor_v = []
lista = []
def mn():
	global mne
	f = open("mnemonicos.txt",'r')
	for i in f.readlines():
		a = i.split(",")
		a[7] = a[7].split("\n")[0]
		mne.append(a)
	for i in mne:
		mnemonicos.append(i[0])
	
	f.close()

def escribirarchivo():
	global f
	f = open("compliado.lst", "w")
def mne_EXT():
	global mne_ext
	mne_ext = []
	for i in mne:
		if i[5] != "":
			mne_ext.append(i[0])
def mne_INH():
	global mne_inh
	for i in mne:
		if i[1] ==""and i[2]=="" and i[3] == "" and i[4]== "" and i[5] == "" and i[7] == "":
			mne_inh.append(i[0])

def mne_REL():
	global mne_rel
	for i in mne:
		if i[1] ==""and i[2]=="" and i[3] == "" and i[4]== "" and i[5] == "" and i[6] == "":
			mne_rel.append(i[0])
			
def leerarchivo():
        global lista, lista_lineas,f
        archivo_l = []
        a =[]
        b = []
        lista_lineas = []
        c = 0
        f = open("EJEMPLO.ASC", "r")
        for i in f.readlines():
                lista_lineas.append(i.split(" "))
                archivo.append(i)
                if c ==3:
                        print lista_lineas
                c += 1
        for j in lista_lineas:
                        b.append(a)
                        a = []
                        for k in j:
                                if len(k)== 0:
                                        #a.append(k)
                                       pass
                                elif "*" in k and j[0] != "*":
                                        break
                                else:
                                        if "\r\n" in k:
                                                k = k.split("\r\n")[0]
                                                a.append(k)
                                        elif "\r" in k:
                                                print k
                                                if len(k)== 1:
                                                        k = ""
                                                        a.append(k)
                                                else:
                                                        k = k.split("\r")[0]
                                                        a.append(k)
                                        else:
                                                a.append(k)
        lista_lineas = b
        count = 0
        for i in lista_lineas:
                if len(i) == 0:
                        lista_lineas[count] = [" "]
                count += 1

def variables():
	global variables
	for i in archivo:
		if "EQU" in i:
			a = i.split(" ")
			dvariables[a[0]] = a[len(a)-1].split("\r")[0]
	

def etiquetas():
	global etiq
	etiq = { }
	cont = 0
	for i in lista_lineas:
		if i[0] == "ORG":
			cont = int(i[-1].split("$")[1],16)
		if len(i) == 1 and len(i[0])>=4:
			etiq[i[0]] = hex(cont).split("x")[1].upper()
			
			
			
		cont += 8
	
mn()
leerarchivo()
escribirarchivo()
variables()
mne_INH()
mne_REL()
mne_EXT()
etiquetas()
	
def principal():
        count = 0
        inst = "    "
        memoria = ""
        contador_memoria = 0
        a = ""
	c = ""
        for i in range(0,len(archivo)):
                n = ""
                n_o = ""
                o = ""
		c = lista_lineas[i][-1]
		if "$" in c:
			c = c.split("$")[1]
		
		if c in dvariables.keys():
                        c = dvariables[c]
			if "$" in c:
				c = c.split("$")[1]
                if lista_lineas[i][0] == reservadas[1] :#nd count == 0:
                       a = (int((lista_lineas[i][len(lista_lineas[i])-1].split("$")[1]),16))#+ 0x8000
                       count = 1
                else:				
                        if archivo[i-1][0] == "*" or len(archivo[i].strip(" "))<2 :
                                f.write(str(i+1)+"A "+inst+"    "+archivo[i-1])
                                if a != "":
                                        a = a+8
                                
                        else:
				if "EQU" in archivo[i]:
					o = lista_lineas[i][-1]
					if "$" in o:
						o = o.split("$")[1]
				
					
                                elif lista_lineas[i][0] in mnemonicos:                                        
                                        if "#" in lista_lineas[i][-1] and lista_lineas[i][0] not in mne_inh and lista_lineas[i][0]:
						n = lista_lineas[i][0]
						o = lista_lineas[i][-1]
                                                o = o.split("#")[1]
                                                if "$" in o:
                                                        o = o.split("$")[1]
                                                if o in dvariables.keys():
                                                        o = dvariables[o]
							if "$" in o:
								o = o.split("$")[1]
						elif o in etiq.keys():
							o = etiq[o]
                                                for t in mne:
                                                        if t[0] == n:
                                                                n_o = t[1]
					elif lista_lineas[i][0] in mne_inh:
						n = lista_lineas[i][0]
						o = ""
						if o in etiq.keys():
							o = etiq[o]
						for r in mne:
							if r[0] == n:
								#print i,r, t[6]
								n_o = r[6]
					elif lista_lineas[i][0] in mne_rel:
						n = lista_lineas[i][0]
						if o in etiq.keys():
							o = etiq[o]
					elif c[0:2] == "00" and not "," in c and lista_lineas[i][0] not in mne_ext:
						n = lista_lineas[i][0]
						o = c[2:]
						for h in mne:
							if h[0] == n:
								n_o = h[2]
								if n_o == "":
									o = ""
					elif lista_lineas[i][0] in mne_ext:
						n = lista_lineas[i][0]
						o = c
						if o in etiq.keys():
							o = etiq[o]
					
						for d in mne:
							if d[0] == n:
								n_o = d[5]
							     
						
					
                                                                
                                                                
                                if a != "":
                                        a = a+8
                                        if n_o != "":
                                                f.write(str(i+1)+"A "+hex(a).split("x")[1].upper()+" "+n_o+o +"    "+ archivo[i-1])
                                        else:
                                                f.write(str(i+1)+"A "+hex(a).split("x")[1].upper()+" "+o+"    "+ archivo[i-1])
                                else:
                                        f.write(str(i+1)+"A "+a+" "+o+" "+ "    "+ archivo[i-1])
                
                
        f.close()
principal()


print etiq