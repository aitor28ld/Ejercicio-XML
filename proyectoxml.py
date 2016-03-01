#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree

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

#Ejercicio 5
