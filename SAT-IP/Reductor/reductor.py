#! /usr/bin/env python3
import string
import os

def hacerVariables(variables):
	vari = ""
	for a in range(1,int(variables) + 1):
		vari = vari + "var 0..1: " + "V" + str(a) + "; var 0..1 : n_" + "V" + str(a) + ";" + "\n"
	vari =vari + "\n" + "% " + "Valores asociados a los literales"
	for a in range(1,int(variables) + 1):
		vari = vari + "\n" + "constraint " + "V" + str(a) + " + " + "n_" + "V" + str(a) + " = 1;" 
	vari =  vari + "\n" + "% Clausulas" + "\n"
	return vari
		
def hacerClausulas(info):
	clausula = "constraint "
	cantidad = len(info) - 1
	for a in range (0,len(info)):
		if cantidad != 1:
			clausula = clausula + literalesClausulas(info[a]) + " + "
			cantidad = cantidad - 1
		else:
		 	clausula = clausula + literalesClausulas(info[a])
	return clausula

def literalesClausulas(numero):
	literal = ""
	if int(numero) == 0:
			literal = " >= 1;" + "\n"
	elif int(numero) > 0:
		literal = "V" + numero
	else:
		literal = "n_" + "V" + str(-1 * int(numero))
	return literal

def adiccional():
	clausula = "\n" + "solve satisfy;" + "%" + "solve maximize primer variable" + "\n"
	return clausula

def escribir(texto,nom):
	f = open("/home/juancho270/Proyecto_Complejidad/SAT-IP/InstanciasMiniZinc/" + nom + ".mzn",'w')
	f.write(texto)
	f.close()
	
def leer():
	carpeta = "/home/juancho270/Proyecto_Complejidad/SAT-IP/InstanciasSAT"
	g = ""
	contador = 0
	nombre = ""
	comentarios = ""
	variables = ""
	for archivo in os.listdir(carpeta):
		clausulas = ""
		g = open(os.path.join(carpeta,archivo) , "r")
		nombre = g.name.split("/")[len(g.name.split("/")) - 1].split(".")[0]
		for linea in g.readlines():
			vector = linea.split()
			if vector[0] == 'c':
				""
			elif vector[0] == 'p':
				variables = vector[2]
				print(variables)
				print(variables)
				print(nombre)
				variables = hacerVariables(variables)
			else:
				clausulas = clausulas + hacerClausulas(vector)
		escribir(comentarios + variables + clausulas,nombre)		
		g.close()
	
leer()
