#Autor: Miguel Alejandro Juarez Gonzalez
#script para revisar en la paguina de la UANL

from bs4 import BeautifulSoup as bs
import requests
import re
from openpyxl import Workbook,load_workbook
patron_de_datos = re.compile(r'data-brand="(Samsung|LG)(.+)" data-name="(.+)" data-price="(.+)" hd')

contador = 1
marca=[]
modelo=[]
precio=[]
for paguina in range(11):
	print("\n paguina"+str(paguina)+"\n")
	url = "https://pcel.com/monitores?sucursal=0&page="+str(paguina)
	buscar = requests.get(url)
	if buscar.status_code == 200:
		html_total = bs(buscar.content,"html.parser")
		info = html_total.find_all("div",{"class":"name"})
		for dato in info:
			#print(contador)
			#print(dato)
			#contador=contador+1
			validar_dato = patron_de_datos.search(str(dato))
			if validar_dato is not None:
				
				marca.append(validar_dato.group(1))
				modelo.append(validar_dato.group(3))
				precio.append(validar_dato.group(4))


				

				libro = Workbook()
				hoja = libro["Sheet"]
				hoja.title = "Monitores"
				hoja["B1"].value = "Marca"
				hoja["C1"].value = "Modelo"
				hoja["D1"].value = "Costo"

				hoja["B"+str(contador+1)].value = "hola"
				libro.save(filename="Conferencias_pag_confiable.xlsx")



				"""
				hoja["B"+str(contador+1)].value = str(validar_dato.group(1))
				hoja["C"+str(contador+1)].value = str(validar_dato.group(3))
				hoja["D"+str(contador+1)].value = str(validar_dato.group(4))
				"""


				contador=contador+1



