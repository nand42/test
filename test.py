### Test di minima comprensione matematica/informatica
### Test di compilazione minima di un file python

import random
import time
import os

clear = lambda: os.system("clear")

start = "via"

while start != "exit":

	clear()

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

	time.sleep(1)

	r = str(input( str(a) + " + " + str(b) + " = "))
	
	time.sleep(1)
	print("\n... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")
	time.sleep(1)

	if ( r == n ):
		print("------------------> Bene, sei una persona in gamba.")
	else:
		print("------------------> Sei una capra.")
		print("Soluzione: " + str(a) + " + " + str(b) + " = " + n)

	print("\n... ... ... ... ... ... ... ... .. .. .. .. .. .. . . . . . . .")

	commento = input("lascia un commento: ")

	if commento == "exit":
		break
	
	clear()
