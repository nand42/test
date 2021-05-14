### Test di minima comprensione matematica/informatica
### Test di compilazione minima di un file python

import random
import time
import os
import json
import io
import csv

FILENAME = "test_risposte.csv"
PATH = ""
"""
def startupCheck():
    if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
        # checks if file exists
        print ("File exists and is readable")
    else:
        print ("Either file is missing or is not readable, creating file...")
        with io.open(os.path.join(FILENAME, 'w') as db_file:
            db_file.write(json.dumps({}))
"""

clear = lambda: os.system("clear")


def writefile(new_data, filename=FILENAME):
	with open(filename, 'r+b') as file:
		# header = next(csv.reader(file))
		dict_writer = csv.DictWriter(file, -999)
		dict_writer.writerow(new_data)
		
start = "via"
i = 0

while start != "exit":

	i += 1

	clear()

	list_risp = {'index:': i}
	
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
	
	list_risp["addizione"] = addizione + str(n)
	
	time.sleep(1)

	risp = str(input( addizione ))

	list_risp["risposta"] =  risp
	
	if risp == "exit":
		writefile(list_risp)
		break
        	
	time.sleep(1)
	print("\n... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")
	time.sleep(1)

	if ( risp == n ):
		list_risp["who"] = "gauss"
		print("------------------> Bene, sei una persona in gamba.")
	else:
		list_risp["who"] = "capra" 
		print("------------------> Sei una capra.")
		print("Soluzione: " + str(a) + " + " + str(b) + " = " + n)

	print("\n... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")

	commento = input("lascia un commento: ")
	list_risp["commento"] = commento

	writefile(list_risp)
	
	if commento == "exit":
		break
	
	clear()

print("Grazie per aver giocato, presto nuove domande...")




