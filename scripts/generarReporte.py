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

import os
import sys
import subprocess
import re

def getData(comand, n):
	subProcess = subprocess.Popen (comand,
			stdout=subprocess.PIPE,
			stderr=subprocess.PIPE,
			shell= True
			)
	subProcess.wait()

	info = subProcess.stdout.readlines()[n].decode()
	info = re.sub (" +", " ", info)
	return info



def addMemory(info):
	memory = []
	memory.append("Información de Disco Duro\n")
	memory.append("Se muestra Información del disco duro\n")
	memory.append("Nombre del disco\n")
	memory.append("Espacio\n")
	memory.append("Bar\n")
	memory.append("Espacio Total\n")
	memory.append(str(info[1])+"\n")
	memory.append("Espacio en Uso\n")
	memory.append(str(info[2])+"\n")
	memory.append("Espacio Libre\n")
	memory.append(str(info[6]))
	memory.append("fin\n")
	print(memory)
	return memory

def addProcess(info):
	process = []
	process.append("Recursos del proceso con PID " + str(info[0]) + "\n")
	process.append("Agujas\n")
	process.append("Memoria Virtual\n")
	process.append(str(info[4])+"\n")
	process.append("Memoria RAM\n")
	process.append(str(info[5])+"\n")
	process.append("Memoria Compartida\n")
	process.append(str(info[6])+"\n")
	process.append("Uso de CPU\n")
	process.append(str(info[8])+"\n")
	process.append("Espacio en DD\n")
	process.append(str(info[9])+"\n")
	process.append("fin\n")
	return process


def writeReport(data):
	report = open("./report.txt","w", encoding="utf-8")

	for line in data:
		report.write(line)
	report.close()

#-------------------------------------------------------------------------#

data = []
infoMem = getData("free -m", 1)
info = infoMem.split(" ")

data = addMemory(info)
writeReport(data)
"""
n=3
while (n>0):
	infoPro = getData("top -n1", n)
	info = infoPro.split(" ")

	data = addProcess(info)
	writeReport(data)
	n = n-1
"""
print("Se ejecutó con éxito")
