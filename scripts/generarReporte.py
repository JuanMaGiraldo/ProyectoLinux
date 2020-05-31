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



def addMemoryRAM(info):
	memory = []
	memory.append("Información general de Memoria RAM\n")
	memory.append("Se muestra Información del disco duro\n")
	memory.append("Magnitud\n")
	memory.append("Valor en MB\n")
	memory.append("Bar\n")
	memory.append("Espacio Total\n")
	memory.append(str(info[1])+"\n")
	memory.append("Espacio en Uso\n")
	memory.append(str(info[2])+"\n")
	memory.append("Espacio Libre\n")
	memory.append(str(info[6]))
	memory.append("fin\n")
	return memory


def addMemoryRAM_2(info):
	memory = []
	memory.append("Información detallada de Memoria RAM\n")
	memory.append("Se muestra Información de la memoria RAM\n")
	memory.append("Magnitud\n")
	memory.append("Valor en KB\n")
	memory.append("Area\n")
	for i in info:
		memory.append(str(i)+"\n")
	memory.append("fin\n")
	return memory


def addMemoryHDD(info):
	memory =[]
	memory.append("Información general del Disco Duro\n")
	memory.append("Se muestra infromación del Disco Duro\n")
	memory.append("Magnitud\n")
	memory.append("Valor en MB\n")
	memory.append("Bar\n")
	memory.append("Tamaño total\n")
	memory.append(str(info[1])+"\n")
	memory.append("Usado\n")
	memory.append(str(info[2])+"\n")
	memory.append("Disponible")
	memory.append(str(info[3])+"\n")
	memory.append("fin\n")
	return memory

def addMemoryHDD_2(info):
	memory = []
	memory.append("Información detallada del Disco Duro\n")
	memory.append("Se muestra información de "+str(info[0]+"\n"))
	memory.append("Magnitud\n")
	memory.append("Valor en MB\n")
	memory.append("Area\n")
	memory.append("Tamaño\n")
	memory.append(str(info[1])+"\n")
	memory.append("Usado\n")
	memory.append(str(info[2])+"\n")
	memory.append("Disponible")
	memory.append(str(info[3])+"\n")
	memory.append("fin\n")
	return memory


def addProcess(info):
	process = []
	process.append("Información de consumo de recursos del proceso "+ info[11] +"\n")
	process.append("Se muestra información del proceso con PID " + str(info[0]) +"\n")
	process.append("Recurso\n")
	process.append("Valor en kb\n")
	process.append("Pie\n")
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
	i=0
	while(i<len(data)):
		for line in data[i]:
			report.write(line)
		i=i+1
	report.close()


def escape_ansi(line):
    ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', line)


#-------------------------------------------------------------------------#

data = []

infoHDD = getData("df --total -m |tail -1", 0)
info = infoHDD.split(" ")
data.append(addMemoryHDD(info))


for n in range(0, 5):
        infoHDD = getData("df -m |grep ^/dev",n)
        info = infoHDD.split(" ")
        data.append(addMemoryHDD_2(info))


infoMem = getData("free -m", 1)
info = infoMem.split(" ")
data.append(addMemoryRAM(info))

n=15
info2 = []
while (n>0):
	infoRAM = getData("cat /proc/meminfo", n)
	info = infoRAM.split(" ")
	info2.append(info[0])
	info2.append(info[1])
	n = n-1
data.append(addMemoryRAM_2(info2))


n=3
while (n>0):
        infoPro = getData("top -n1", n+6)
        infoPro = escape_ansi(infoPro)
        info = infoPro.split(" ")
        info.pop(0)
        info.pop(len(info) -1)
        data.append(addProcess(info))
        n = n-1


writeReport(data)
