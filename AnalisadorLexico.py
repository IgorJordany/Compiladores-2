#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva

def getCaracter():
	global indice, texto, linha, espacos
	if indice < len(texto):
		while texto[indice] == ' ':
			indice += 1
			espacos += 1
		if texto[indice] == '\n':
			linha += 1
			indice += 1
		return texto[indice]
	elif indice == len(texto):
		return "$"
	else:
		return False

def ignoraComentarioA():
	global indice
	while getCaracter() != '*':
		indice += 1

def trataComentarioA():
	global indice
	if getCaracter() == '/':
		indice += 1
		if getCaracter() == '*':
			indice += 1
			print("comecou comentario A")
			ignoraComentarioA()
			fimComentarioA()
		else:
			print("A0 - Reconhece simbolo simples")
	else:
		return False

def fimComentarioA():
	global indice
	if getCaracter() == '*':
		indice += 1
		if getCaracter() == '/':
			indice += 1
			print("acabou comentario A")
		else:
			ignoraComentarioA()
			fimComentarioA()

def trataComentarioB():
	global indice
	if getCaracter() == '{':
		indice += 1
		print("comecou comentario B")
		while getCaracter() != '}':
			indice += 1
		if getCaracter() == '}':
			indice += 1
			print("acabou comentario B")
	else:
		return False

def trataIdentificador():
	global indice, letra, digito, buf
	if getCaracter() in letra:
		buf = buf + getCaracter()
		indice += 1
		while getCaracter() in letra:
			buf = buf + getCaracter()
			indice += 1
		if getCaracter() not in letra:
			if buf in pReservadas:
				print("saporra é palavra reservada")
				print(buf)
				buf = ""
			else:
				print("saporra é identificadorA")
				print(buf)
				buf = ""
		if getCaracter() in digito:
			buf = buf + getCaracter()
			indice += 1
			while getCaracter() in letra or getCaracter() in digito:
				buf = buf + getCaracter()
				indice += 1
				if getCaracter() not in letra or getCaracter() not in digito:
					print("saporra é identificadorB")
					print(buf)
					buf = ""
	else:
		return False


arqC = open('codigo.ij','r')
#arqT = open('tokens.ij','w')
texto = arqC.read()
letra = ['a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','x','X','w','W','y','Y','z','Z']
pReservadas = ['if','then','while','do','write','read','else','begin','end']
digito = ['0','1','2','3','4','5','6','7','8','9']
buf = ""
indice = 0
espacos = 0
linha = 1

while indice < len(texto):
	trataComentarioA()
	trataComentarioB()
	trataIdentificador()

arqC.close()
#arqT.close()