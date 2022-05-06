# problema 1.3 hewel.ochoa@utp.ac.pa

arg_cero = input(":")
arg_uno = input(":")
can_Conc = 0
#evalua cuantas letras se encuentra coinciden en las 2 palabras
for letra in arg_uno:
	if letra in arg_cero:
		can_Conc += 1
# verifico si la cantidad de conicidencia
# es mayor a la mitad del largo de cadena 
# enotonces puede ser un anagrama
if (can_Conc > len(arg_uno)/2):
	print(True)
else:
	print(False)
