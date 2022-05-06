# problema #2 hewel.ochoa@uto.ac.pa
import random

numero_secreto	=	random.randint(0, 100)
prueba	=	-1
juagadas = 0
while juagadas != 9:
	prueba	=	int(input("adivina el numero: "))
	if	prueba	<	numero_secreto :
		print("Su	numero	es	muy	bajo")
	elif prueba	>	numero_secreto :
		print("Su	numero	es	muy	alto")
	else:
		print("Acertaste,	el	numero	correcto	era	",numero_secreto)
		break
	juagadas += 1
