### Test di minima comprensione matematica/informatica
### Test di compilazione minima di un file python

import random
import time
import os
import json
import io
import csv

FILENAME = "test_risposte.csv"


clear = lambda: os.system("clear")


# aggiungere funzione di controllo del file .csv


def writefile(new_data, filename=FILENAME):
	with open(filename, 'a', newline='') as file:
		wr = csv.writer(file, dialect='excel')
		wr.writerow(new_data)		


start = "via"
i = 0
list_risp = []

while start != "exit":

	i += 1
	clear()

	list_risp = [str(i)]
	
	print("... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")
	print("Hello!")
	start = input("Premi INVIO per iniziare")
	clear()
	print("... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")
	print("Rispondi al seguente quesito per sapere chi sei \n")
	print("... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")

	a = random.randrange(0,100,1)
	b = a
	while a == b:
		b = random.randrange(0,100,1)

	n = str( a + b )

	addizione = str(a) + " + " + str(b) + " = "
	
	list_risp.append(addizione + str(n))
	
	time.sleep(1)

	risp = str(input( addizione ))

	list_risp.append(risp)
	
	if risp == "exit":
		writefile(list_risp)
		break
        	
	time.sleep(1)
	print("\n... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")
	time.sleep(1)

	if ( risp == n ):
		list_risp.append("gauss")
		print("------------------> Bene, sei una persona in gamba.")
	else:
		list_risp.append("capra")
		print("------------------> Sei una capra.")
		print("Soluzione: " + str(a) + " + " + str(b) + " = " + n)

	print("\n... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")

	commento = input("lascia un commento: ")
	list_risp.append(commento)

	writefile(list_risp)
	
	if commento == "exit":
		break
	
	clear()

print("Grazie per aver giocato, presto nuove domande...")




