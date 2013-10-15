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
        f = open("EJEMPLO.ASC", "r")
        for i in f.readlines():
                lista_lineas.append(i.split(" "))
                archivo.append(i)
        for j in lista_lineas:
                        b.append(a)
                        a = []
                        for k in j:
                                if len(k)== 0:
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
		
				
			
		
		
	
def inh(i):
	global m
	if "$" in i[len(i)-1]:
		m = i[len(i)-1].split("$")[1]
		if i[0] in mne_inh:
			return True
	
		
def inmediato(operando):
	if "$" in operando:
		operando = operando.split("$")[1]
	if "#" in operando:
		pass
	return operando

def directo(operando):
	if "$" in operando:
		operando = operando.split("$")[1]
	operando = operando[:2]
	return operando
	
def ext(operando):
	if "$" in operando:
		operando = operando.split("$")[1]
	return operando
	
def ind(operando):
	global x, y
	if "$" in operando:
		operando = operando.split("$")[1]
	if "X" in operando:
		ox = operando.split(",")
		operando = ox[0]
		x = ox[1]
	elif "Y" in operando:
		oy = operando.split(",")
		operando = oy[0]
		y = ox[1]
	return operando

def rel(i):
	global m
	if "$" in i[len(i)-1]:
		m = i[len(i)-1].split("$")[1]
		if m in mne_rel:
			return True
def variables():
	global variables
	for i in archivo:
		if "EQU" in i:
			a = i.split(" ")
			dvariables[a[0]] = a[len(a)-1].split("\r")[0]
	
mn()
leerarchivo()
escribirarchivo()
variables()
mne_INH()
mne_REL()
	
def principal():
        count = 0
        inst = "    "
        memoria = ""
        contador_memoria = 0
        a = ""
        for i in range(0,len(archivo)):
                if lista_lineas[i][0] == reservadas[1] and count == 0:
                       a = (int((lista_lineas[i][len(lista_lineas[i])-1].split("$")[1]),16))#+ 0x8000
                       count = 1
                else:
                        if archivo[i][0] == "*":
                                f.write(str(i)+"A "+inst+"   "+archivo[i])
                                if a != "":
                                        a = a+8
                                
                        else:
                                if a != "":
                                        print a
                                        a = a+8
                                        f.write(str(i)+"A "+hex(a).split("x")[1].upper()+" "+ archivo[i])
                                else:
                                        f.write(str(i)+"A "+a+ archivo[i])
                
        f.close()
	
principal()

