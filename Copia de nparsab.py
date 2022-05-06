# problema 1.1 hewel.ochoa@utp.ac.pa
import sys

def pares(arg):
	comp = int(arg[0])
	if(comp%2 != 0):
		comp += 1
	Nroot = comp
	goal = int(arg[1]) 
	while Nroot < goal:
		Nroot += 2
		print(Nroot)
	
arg_uno = sys.argv[1:]
arg_cero = arg_uno
print(arg_cero)
if (arg_cero[0]>arg_cero[1]):
	arg_cero.sort()
	print(arg_cero)
pares(arg_cero)