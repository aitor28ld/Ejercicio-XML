#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
import utm
import os

arbol = etree.parse("camping.xml")

raiz = arbol.getroot()

print "1.- Listar los servicios que ofrecen los campings."
print "2.- ¿Cuantos servicios ofrecen los campings?"
print "3.- Pide por teclado una cadena y muestra la descripción y precio del camping que contiene dicha cadena."
print "4.- Pide por teclado un camping y muestra las coordenadas así como un enlace a Open Street Map de su ubicación."
print "5.- Pedir por teclado el código postal del camping además de una fecha. Deberá decir si el camping está cerrado y muestra el nombre del camping con la fecha de inicio y fin."

op = int(raw_input("Elige una opción de las indicadas arriba: "))

#Ejercicio 1
if op == 1:
	servicios = raiz.findall("objRegistral/serveis")
	for x in servicios:
		print x.find("servei/descripcio").text

#Ejercicio 2
if op == 2:
	servicios = raiz.findall("objRegistral")
	for x in servicios:
		print len(x.findall("serveis/servei"))

#Ejercicio 3
if op == 3:
	camping = raw_input("Escribe una cadena a buscar: ")
	campings = raiz.findall("objRegistral")
	for x in campings:
		if camping in x.find("dades_generals/retol").text:
			precio = raiz.findall("objRegistral/preus/any/preu")
			for n in precio:
				print n.find("descripcio").text
				print n.find("orientatiu").text

#Ejercicio 4
if op == 4:
	camping = raw_input("Escribe el nombre de un camping: ")
	campings = raiz.findall("objRegistral")
	for x in campings:
		if camping == x.find("dades_generals/retol").text:
			longitud = x.find("dades_generals/adreca/utm_x").text
			latitud = x.find("dades_generals/adreca/utm_y").text
			medidas = str(utm.to_latlon(int(longitud), int(latitud), 31, 'U')).split(",")
			print "http://www.openstreetmap.org/way/109089302#map=15/"+medidas[0][1:]+"/"+medidas[1][1:-1]
			
#Ejercicio 5
if op == 5:
	cod = raw_input("Escribe el código postal de un camping: ")
	fecha = raw_input("Escribe una fecha valida (DD-MM-YYYY)(Sólo anyo 2014): ")
	campings = raiz.findall("objRegistral")
	fechas = raiz.findall("objRegistral/periodes_tancament/tancament")
	for x in campings:
		if cod == x.find("dades_generals/adreca/cp").text:
			print x.find("dades_generals/retol").text
			for n in fechas:
				if fecha >= n.find("data_inici").text and fecha <= n.find("data_fi").text:
					print "Camping Cerrado"
					print "Fechas de cierre:", n.find("data_inici").text+" hasta "+n.find("data_fi").text
					break
#Ejercicio 6
if op == 6:
	provincia = raw_input("Escribe una provincia: ").upper()
	provincias = raiz.findall("objRegistral")
	for x in provincias:
		if provincia in x.find("dades_generals/adreca/provincia").text:
			try:
				os.system("echo '<h1>"+x.find("dades_generals/retol").text.encode("utf-8")+"</h1>' >> index.html")
				os.system("echo '<p>"+x.find("dades_generals/adreca/no_normalitzada").text.encode("utf-8")+"</p>' >> index.html")
				os.system("echo '<a href=http://"+x.find("dades_generals/web").text+">Información</a>' >> index.html")
			except:
				pass
