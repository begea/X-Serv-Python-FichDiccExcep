#!/usr/bin/python
# -*- coding: utf-8 -*-

fd = open("/etc/passwd", "r")

lineas = fd.readlines()
diccionario_usuarios = {}
fd.close()

for linea in lineas:
	trozos = linea.split(':')
	usuario = trozos[0]
	shell = trozos[-1]
	diccionario_usuarios[usuario] = shell

nombre_usu1 = 'root'
nombre_usu2 = 'imaginario'

nombre_shell1 = diccionario_usuarios[nombre_usu1]
print "Usuario:" + nombre_usu1, " Shell:" + nombre_shell1[0:-1]

try:
	nombre_shell2 = diccionario_usuarios[nombre_usu2]
	print "Usuario:", nombre_usu2, " Shell:", nombre_shell2[0:-1]
	
except KeyError:
	print "No se ha podido encontrar el usuario: " + "'" + nombre_usu2 + "'"
