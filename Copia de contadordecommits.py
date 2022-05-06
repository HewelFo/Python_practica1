import datetime
import json
import requests

def descargajson():
	Url_s = requests.get('https://api.github.com/repos/tensorflow/tensorflow/stats/commit_activity')
	Lectura_S = Url_s.json()
	print("todo ok")
	Week_Commits = 0
	Mayor_Commits = 0
	Mayor_Prueba = 0
	Mayor_Total = 0
	Dias = [0,0,0,0,0,0,0]
	D_Mayor_Commits = " "
	for row in Lectura_S:
		Mayor_Commits = row.get('total')

	for row in Lectura_S:
		Mayor_Prueba = row.get('total')
		temp_aux = row.get('days')
		for i in range(7):
			Dias[i] += temp_aux[i]
		if Mayor_Commits < Mayor_Prueba:
			Mayor_Commits = Mayor_Prueba
			Mayor_Total = row.get('total')
			Week_Commits = datetime.datetime.fromtimestamp(row.get('week'))

	print("La semana de mayor commit es ", Week_Commits, " con ", Mayor_Total)
	print("El dia de mayor commit es ",Dias.index(max(Dias)), " con ", max(Dias)," Commits")


descargajson()








