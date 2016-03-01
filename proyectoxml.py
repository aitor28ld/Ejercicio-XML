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

#Ejercicio 3

#Ejercicio 4

#Ejercicio 5
