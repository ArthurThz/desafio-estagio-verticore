lista_sigla_estados =["AC","AL","AP","AM","BA","CE","DF","ES","GO","MA","MT","MS","MG","PA","PB","PR","PE","PI","RJ","RN","RS","RO","RR","SC","SP","SE","TO"]

import openpyxl

book = openpyxl.Workbook()

print(book.sheetnames)

pagina = book['Sheet']

pagina.append(["Gentilico","Capital","Governador","População","IDH"])

book.save("planilha.xlsx")

lista = []

lista.append('teste')
lista.append('teste2')
print(lista)