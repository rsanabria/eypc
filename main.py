mne = []


def mn():
	global mn
	f = open("nmemonicos.txt",'r')
	for i in f.readlines():
		a = i.split(",")
		a[7] = a[7].split("\n")[0]
		mne.append(a)




	
mn()
print len(mne[49][6])


		



		
