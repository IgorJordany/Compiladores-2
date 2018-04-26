#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva

from AnalisadorLexico import *

def proxToken():
	if tokens:
		t = tokens.pop(0)
		return t.split(' ')
	else:
		return False

def S():
	if programa():
		return True
	else:
		return False

def programa():
	global token
	if token[2] == "program":
		print("----ok-program")
		token = proxToken()
		if token[1] == "identificador":
			print("----ok-identificador")
			token = proxToken()
			if corpo():
				return True
			else:
				return False


def corpo():
	return True


token = proxToken()
print(S())