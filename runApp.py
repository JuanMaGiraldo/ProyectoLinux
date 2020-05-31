#!/usr/bin/python3
#-*- coding: utf-8-*-
#23/05/2020
#Proyecto Final Linux 1
#=======================================
#Ingenieria de sistemas y computación
#Universidad del Quindío
#Juan Manuel Giraldo Rios
#Ivan Santiago Castañeda Henao
#Jhon Nicolay Mejia
#Diego Armando
#Licencia GNU
#======================================

import subprocess

def ejecutarComando ( comando ):
	p = subprocess.Popen ( comando,
							stdout = subprocess.PIPE,
							stderr = subprocess.PIPE,
							shell  = True
						)
	p.wait()

	return [ p.stdout.read().decode(), p.stderr.read().decode() ]

ejecutarComando("cd scripts && ./generarReporte.py")
print("ejecutado")
ejecutarComando("cd page && wkhtmltopdf index.html reporte.pdf")
filename="page/reporte.pdf"
plot = subprocess.Popen("evince '%s'" % filename, shell=True)
