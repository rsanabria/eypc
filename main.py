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
        f = open("EXEMPLO.ASC", "r")
        for i in f.readlines():
                lista_lineas.append(i.split(" "))
                archivo.append(i)
                #if c ==3:
                 #       print lista_lineas
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
	for i in lista_lineas:
		if "EQU" in i:
			dvariables[i[0]] = i[-1]
	# for i in archivo:
	# 	if "EQU" in i:
	# 		a = i.split(" ")
	# 		dvariables[a[0]] = a[len(a)-1].split("\r")[0]
	

def etiquetas():
	global etiq
	etiq = { }
	cont = 0
	for i in lista_lineas:
		if i[0] == "ORG":
			cont = int(i[-1].split("$")[1],16)
		if len(i) == 1 and len(i[0])>=2:
			etiq[i[0].split(" ")[0]] = hex(cont).split("x")[1].upper()
			
			
			
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
        lon = []
        for i in range(1,len(archivo)):
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
                if len(lista_lineas[i][0]) >= 2 :

                		if lista_lineas[i][0] not in mnemonicos and lista_lineas[i][0] != "RESET" and lista_lineas[i][0] not in reservadas and lista_lineas[i][0] not in etiq.keys() and lista_lineas[i][0] not in dvariables.keys() and " " not in lista_lineas[i][0] :
                				print "error en la linea", i, lista_lineas[i][0], ": el mnemonico no esta definido"
                				break
                		if len(lista_lineas[i][-1]) >=2 and len(lista_lineas[i]) >1:
                			if "#" in lista_lineas[i][-1] :
                				b = lista_lineas[i][-1].split("#")[1]
                			else:
                				b = lista_lineas[i][-1]
                			if b not in dvariables.keys() and "$" not in lista_lineas[i][-1] and lista_lineas[i][-1] not in etiq.keys():
                				print "error en la linea", i, lista_lineas[i][-1], ": no esta definida"
                				break
                if lista_lineas[i][0] == "END":
                		f.write(str(i)+"A"+n_o+o +"         "+archivo[i-1])
                		break
                if lista_lineas[i][0] == reservadas[1] :#nd count == 0:
                       a = (int((lista_lineas[i][len(lista_lineas[i])-1].split("$")[1]),16))#+ 0x8000
                       f.write(str(i)+"A"+n_o+o +"         "+archivo[i-1])
                       a = a-8
                else:                           
                        if archivo[i-1][0] == "*"or len(archivo[i-1].strip(" "))<2 or lista_lineas[i] == [''] :
                                f.write(str(i)+"A"+n_o+o +"         "+archivo[i-1])
                                if a != "":
                                	# if lista_lineas[i] == ['']:
                                	# 	pass
                                	# else:
                                	# 	pass #a = a+8
                                	
                                
                        else:
                                if "EQU" in archivo[i-1]:
                                        o = lista_lineas[i][-1]
                                        if "$" in o:
                                                o = o.split("$")[1]
                                
                                        
                                elif lista_lineas[i][0] in mnemonicos:                                        
                                        if "#" in lista_lineas[i][-1] and lista_lineas[i][0] not in mne_inh and "," not in lista_lineas[i][-1]:
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
                                                if lista_lineas[i-1][0] == "ORG":
                                                	a = a
                                                else:
                                                	a = a +len(o)
                                        elif lista_lineas[i][0] in mne_inh and "," not in lista_lineas[i][-1]:   #modo inherente
                                                n = lista_lineas[i][0]
                                                o = ""
                                                if o in etiq.keys():
                                                        o = etiq[o]
                                                for r in mne:
                                                        if r[0] == n:
                                                                #print i,r, t[6]
                                                                n_o = r[6]

                                                a = a +len(o)
                                        elif lista_lineas[i][0] in mne_rel and "," not in lista_lineas[i][-1]:   #modo relativo
                                                n = lista_lineas[i][0]
                                                o = lista_lineas[i][-1]
                                                if "$" in o:
                                                        o = o.split("$")[1]
                                                if o in etiq.keys():
                                                        o = etiq[o]
                                                for u in mne:
                                                        if lista_lineas[i][0] == u:
                                                                n_o = u[7]
                                                a = a +len(o)
                                        elif c[0:2] == "00" and "," not in lista_lineas[i][-1] and lista_lineas[i][0] not in mne_ext:  #modo directo
                                                n = lista_lineas[i][0]
                                                o = c[2:]
                                                for h in mne:
                                                        if h[0] == n:
                                                                n_o = h[2]
                                                                if n_o == "":
                                                                        o = ""
                                                a = a +len(o)
                                        elif lista_lineas[i][0] in mne_ext and lista_lineas[i][0] not in mne_rel and "," not in lista_lineas[i][-1]: #ext 
                                                n = lista_lineas[i][0]
                                                o = c
                                                if o in etiq.keys():
                                                        o = etiq[o]
                                        
                                                for d in mne:
                                                        if d[0] == n:
                                                                n_o = d[5]
                                                a = a +len(o)
                                        elif "," in lista_lineas[i][-1]:
                                                if "X" in lista_lineas[i][-1]:
                                                        n = lista_lineas[i][0]
                                                        operandos = lista_lineas[i][-1].split(',')
                                                        o = operandos[0] #+ operandos[1]
                                                        if "$" in o:
                                                                o = o.split("$")[1]
                                                        if "" in o :
                                                        	pass

                                                        if o in etiq:
                                                                o = etiq[o]
                                                        for v in mne:
                                                                if v[0] == n:
                                                                        n_o = v[3]
                                                elif "Y" in lista_lineas[i][-1]:
                                                        n = lista_lineas[i][0]
                                                        operandos = lista_lineas[i][-1].split(',')
                                                        o = operandos[0]
                                                        if "$" in o:
                                                                o = o.split("$")[1]
                                                        if o in etiq:
                                                                o = etiq[o]
                                                        for z in mne:
                                                                if z[0] == n:
                                                                        n_o = z[4]
                                                a = a +len(o)
                                        elif "," in lista_lineas[i][-3]:
                                                if "X" in lista_lineas[i][-3]:
                                                        n = lista_lineas[i][0]
                                                        operandos = lista_lineas[i][-3].split(',')
                                                        if "$" in operandos[0]:
                                                                operandos[0] = operandos[0].split("$")[1]
                                                        if "$" in operandos[2]:
                                                                operandos[2] = operandos[2].split("$")[1]
                                                        o = operandos[0] +operandos[2]
                                                        if lista_lineas[i][-2] in etiq.keys():
                                                                o = o + etiq[lista_lineas[i][-2]]
                                                        else:
                                                                o = o+lista_lineas[i][-2]
                                                        for q in mne:
                                                                if q[0] == n:
                                                                        n_o = q[3]
                                                if "Y" in lista_lineas[i][-3]:
                                                        n = lista_lineas[i][0]
                                                        operandos = lista_lineas[i][-3].split(',')
                                                        if "$" in operandos[0]:
                                                                operandos[0].split("$")[1]
                                                        o = operandos[0] +operandos[2]
                                                        if lista_lineas[i][-2] in etiq.keys():
                                                                o = o + etiq[lista_lineas[i][-2]]
                                                                        
                                                        o = o +lista_lineas[i][-2]
                                                        for w in mne:
                                                                if w[0] == n:
                                                                        n_o = w[4]
                                                a = a +len(o)
                                
                                if not len(n_o+o) in lon:
                                	lon.append(len(n_o+o))
                                if len(o)> 4:
                                	espacio = ((len(o)+len(n_o))-4)*" "
                                else:
                                	espacio = "    "
                                if n_o != "":
                                	if a != "":
                                		a = a+8
                                		if i+1 > 100:
                                			f.write(str(i)+ "A "+hex(a).split("x")[1].upper()+" "+n_o+o+((10-len(n_o+o))*" ")+archivo[i-1])
                                		elif i+1 > 10:
                                			f.write(str(i)+ "A  "+hex(a).split("x")[1].upper()+" "+n_o+o+((10-len(n_o+o))*" ")+archivo[i-1])
                                		else:
                                			f.write(str(i)+ "A   "+hex(a).split("x")[1].upper()+" "+n_o+o+((10-len(n_o+o))*" ")+archivo[i-1])
                                	else:
                                 		if i+1 > 100:
                                			f.write(str(i)+ "A " +n_o+o+((10-len(n_o+o))*" ")+archivo[i-1])
                                		elif i+1 > 10:
                                			f.write(str(i)+ "A  " +n_o+o+((10-len(n_o+o))*" ")+archivo[i-1])
                                		else:
                                			f.write(str(i)+ "A   " +n_o+o+((10-len(n_o+o))*" ")+archivo[i-1])
                                else:
                                	if a != "":
                                		a = a+8
                                		if i+1 > 100:
                                			f.write(str(i)+ "A "+hex(a).split("x")[1].upper()+"          "+o+archivo[i-1])
                                		elif i+1 > 10:
                                			f.write(str(i)+ "A  "+hex(a).split("x")[1].upper()+"          "+o+archivo[i-1])
                                		else:
                                			f.write(str(i)+ "A   "+hex(a).split("x")[1].upper()+"          "+o+archivo[i-1])
                                	else:
                                 		if i+1 > 100:
                                			f.write(str(i)+ "A "+o+"          "+archivo[i-1])
                                		elif i+1 > 10:
                                			f.write(str(i)+ "A  "+o+"          "+archivo[i-1])
                                		else:
                                			f.write(str(i)+ "A   "+o+"          "+archivo[i-1])

                
                
        f.close()
principal()
print lista_lineas[102] == ['']

