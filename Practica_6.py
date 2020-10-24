#Autor: Miguel Alejandro Juarez Gonzalez
#script para revisar paguina de computo y verificar precios

from bs4 import BeautifulSoup as bs
import requests
import re
from openpyxl import Workbook,load_workbook
patron_de_datos = re.compile(r'data-brand="(Samsung|LG)(.+)" data-name="(.+)" data-price="(.+)" hd')
marca=[]
modelo=[]
precio=[]


def Guardar_en_excel():
	libro = Workbook()
	hoja = libro["Sheet"]
	hoja.title = "Monitores"
	hoja["B1"].value = "Marca"
	hoja["C1"].value = "Modelo"
	hoja["D1"].value = "Costo"

	for contador in range(2,len(marca)+2):
		hoja["B"+str(contador)].value = marca[contador-2]
		hoja["C"+str(contador)].value = modelo[contador-2]
		hoja["D"+str(contador)].value = precio[contador-2]

	libro.save(filename="Monitores.xlsx")

for paguina in range(11):
	url = "https://pcel.com/monitores?sucursal=0&page="+str(paguina)
	buscar = requests.get(url)
	if buscar.status_code == 200:
		html_total = bs(buscar.content,"html.parser")
		info = html_total.find_all("div",{"class":"name"})
		for dato in info:
			validar_dato = patron_de_datos.search(str(dato))
			if validar_dato is not None:
				marca.append(validar_dato.group(1))
				modelo.append(validar_dato.group(3))
				precio.append(validar_dato.group(4))

Guardar_en_excel()