mn = []


def mn():
	global mn
	f = open("nmemonicos.txt",'r')
	for i in f.readlines():
		a = i.split("\n")
		mn.append(a[0])




		
mn()
		

		



		
