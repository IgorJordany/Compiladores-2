#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva

def getCaracter():
	global indice, texto, linha, espacos
	if indice < len(texto):
		return texto[indice]
	else:
		return False

def ignoraComentarioA():
	global indice
	while getCaracter() != '*':
		indice += 1

def trataComentarioA():
	global indice, tokens, linha
	if getCaracter() == '/':
		indice += 1
		if getCaracter() == '*':
			indice += 1
			print("----Início comentário A")
			ignoraComentarioA()
			fimComentarioA()
		else:
			print("----Símbolo simples")
			tokens.append(str(linha) + " sSimples " + getCaracter())
			return True
	else:
		return False

def fimComentarioA():
	global indice
	if getCaracter() == '*':
		indice += 1
		if getCaracter() == '/':
			indice += 1
			print("----Fim comentário A")
			return True
		else:
			ignoraComentarioA()
			fimComentarioA()

def trataComentarioB():
	global indice
	if getCaracter() == '{':
		indice += 1
		print("----Início comentário B")
		while getCaracter() != '}':
			indice += 1
		if getCaracter() == '}':
			indice += 1
			print("----Fim comentário B")
			return True
	else:
		return False

def trataIdentificador():
	global indice, letra, digito, buf, tokens, linha
	if getCaracter() in letra:
		buf = buf + getCaracter()
		indice += 1
		while getCaracter() in letra or getCaracter() in digito:
			buf = buf + getCaracter()
			indice += 1
		if getCaracter() not in letra:
			if buf in pReservadas:
				print("----Palavra reservada")
				print(buf)
				tokens.append(str(linha) + " pReservada " + buf)
				buf = ""
				return True
			else:
				print("----IdentificadorA")
				print(buf)
				tokens.append(str(linha) + " identificador " + buf)
				buf = ""
				return True
		if getCaracter() in digito:
			buf = buf + getCaracter()
			indice += 1
			while getCaracter() in letra or getCaracter() in digito:
				buf = buf + getCaracter()
				indice += 1
				if getCaracter() not in letra or getCaracter() not in digito:
					print("----Identificador")
					print(buf)
					tokens.append(str(linha) + " identificador " + buf)
					buf = ""
					return True
	else:
		return False

def trataSimboloDuploeSimples():
	global indice, linha, tokens
	if getCaracter() in simbolo:
		if getCaracter() == ':':
			indice += 1
			if getCaracter() in simbolo:
				if getCaracter() == '=':
					print("----Símbolo duplo")
					print(":=")
					tokens.append(str(linha) + " sDuplo " + ":=")
					indice += 1
					return True
			else:
				print("----Símbolo simples")
				print(":")
				tokens.append(str(linha) + " sSimples " + ":")
		elif getCaracter() == '<':
			indice += 1
			if getCaracter() in simbolo:
				if getCaracter() == '=':
					print("----Símbolo duplo")
					print("<=")
					tokens.append(str(linha) + " sDuplo " + "<=")
					indice += 1
					return True
				elif getCaracter() == '>':
					print("----Símbolo duplo")
					print("<>")
					tokens.append(str(linha) + " sDuplo " + "<>")
					indice += 1
					return True
		elif getCaracter() == '>':
			indice += 1
			if getCaracter() in simbolo:
				if getCaracter() == '=': 
					print("----Símbolo duplo")
					print(">=")
					tokens.append(str(linha) + " sDuplo " + ">=")
					indice += 1
					return True
		else:
			print("----Símbolo simples")
			print(getCaracter())
			tokens.append(str(linha) + " sSimples " + getCaracter())
			indice += 1
			return True
	else:
		return False

def trataNumeroInteiroReal():
	global indice, digito, buffNumero, linha, tokens
	if getCaracter() in digito:
		buffNumero = buffNumero + getCaracter()
		indice += 1
		while getCaracter() in digito:
			buffNumero = buffNumero + getCaracter()
			indice += 1
		if getCaracter() == '.':
			buffNumero = buffNumero + getCaracter()
			indice += 1
			if getCaracter() in digito:
				buffNumero = buffNumero + getCaracter()
				indice += 1
				while getCaracter() in digito:
					buffNumero = buffNumero + getCaracter()
					indice += 1
				if getCaracter() not in digito:
					print("----Número real")
					print(buffNumero)
					tokens.append(str(linha) + " nReal " + buffNumero)
					buffNumero = ""
					return True
			else:
				print("----Erro léxico não se pode ter real sem número após o ponto, na linha " + str(linha))
				print(buffNumero)
				buffNumero = ""
				return True
		elif getCaracter() not in digito:
			print("----Número inteiro")
			print(buffNumero)
			tokens.append(str(linha) + " nInteger " + buffNumero)
			buffNumero = ""
			return True
	else:
		return False

def consomeEspacos():
	global indice, linha
	if indice < len(texto):
		while getCaracter() == ' ':
			indice += 1
			return True
		while getCaracter() == '\n':
			linha += 1
			indice += 1
			return True
		while getCaracter() == '\t':
			indice += 1
			return True
	else:
		return False

def analisadorLexico():
	global tokens, arqT
	while indice < len(texto):
		retorno1 = trataComentarioA()
		retorno2 = trataComentarioB()
		retorno3 = trataIdentificador()
		retorno4 = trataSimboloDuploeSimples()
		retorno5 = trataNumeroInteiroReal()
		retorno6 = consomeEspacos()
		if (retorno1 or retorno2 or retorno3 or retorno4 or retorno5 or retorno6) != True:
			print("----Erro léxico caracter não permitido para linguagem na linha " + str(linha) + " " + getCaracter())
			return False

#	arqT.writelines(tokens)

arqC = open('codigo.ij','r')
#arqT = open('tokens.ij','w')
texto = arqC.read()
letra = ['$','a','A','b','B','c','C','d','D','e','E','f','F','g','G','h','H','i','I','j','J','k','K','l','L','m','M','n','N','o','O','p','P','q','Q','r','R','s','S','t','T','u','U','v','V','x','X','w','W','y','Y','z','Z']
pReservadas = ['if','then','while','do','write','read','else','begin','end','integer','real','var','$','procedure','program']
digito = ['0','1','2','3','4','5','6','7','8','9']
simbolo = ['(',')','*','+','-',':','=','<','>','.',',',';']
tokens = []
buf = ""
buffNumero = ""
indice = 0
linha = 1

analisadorLexico()

arqC.close()
#arqT.close()