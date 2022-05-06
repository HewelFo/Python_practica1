import csv

Cant_trans = 0
Cant_trans_espec = 0
sujeto = True
with open('planilla.csv', "r", encoding='UTF-8') as F :
	reader = csv.reader(F, delimiter=',')
	for row in reader:
		Cant_trans += 1
		if '4-807-1659' in row:
			print("sujeto de prueba numero 4-807-1659 encontrado")
		else:
			sujeto = False

		if '2019' in row:
			Cant_trans_espec += 1

print(sujeto)
print("cantidad de transacciones totales: ",Cant_trans)
print("cantidad de trnsacciones en 2019: ",Cant_trans_espec)