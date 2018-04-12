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

arqC = open('codigo.igor','r')
#arqT = open('tokens.igor','w')
texto = arqC.read()
indice = 0
espacos = 0
linha = 1

while indice < len(texto):
	trataComentarioA()
	trataComentarioB()

print(espacos)
print(len(texto)-espacos)
arqC.close()
#arqT.close()