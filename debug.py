#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva
def getCaracter():
	global indice, texto
	if indice < len(texto):
		return texto[indice]
	else:
		return False

def consomeEspacos():
	global indice, linha, texto, texto2
	if indice < len(texto):
		while getCaracter() == '\n':
			texto2 = texto2 + getCaracter()
			linha += 1
			indice += 1
			return True
		while getCaracter() != 'p':
			texto2 = texto2 + getCaracter()
			indice += 1
			return True
	else:
		return False

def procuraPrint():
	global indice, linha, texto2
	if getCaracter() == 'p':
		indice += 1
		if getCaracter() == 'r':
			indice += 1
			if getCaracter() == 'i':
				indice += 1
				if getCaracter() == 'n':
					indice += 1
					if getCaracter() == 't':
						indice += 1
						if getCaracter() == '(':
							indice += 1
							if getCaracter() == '"':
								indice += 1
								if getCaracter() == '-':
									indice += 1
									if getCaracter() == '-':
										print(indice)
										texto2 = texto2 + "print(" + '"' + str(linha)
										print("print linha " + str(linha))
										return True
									else:
										return False
								else:
									return False
							else:
								return False
						else:
							return False
					else:
						return False
				else:
					return False
			else:
				texto2 = texto2 + 'p' + 'r'
				return False
		else:
			texto2 = texto2 + 'p'
			return False
	else:
		return False		

arqC = open('c.ij','r')
texto = arqC.read()
arqC.close()
arqD = open('d.ij','w')

texto2 = ""
indice = 0
linha = 1

while indice < len(texto):
	consomeEspacos()
	procuraPrint()

arqD.write(texto2)
arqD.close()

