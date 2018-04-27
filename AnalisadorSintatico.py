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
		print("----Erro-esperado-<programa>")
		return False

def programa():
	global token
	if token[2] == "program":
		print("----OK-program")
		token = proxToken()
		if token[1] == "identificador":
			print("----OK-identificador")
			token = proxToken()
			if corpo():
				if token[2] == ".":
					print("----OK-.")
					return True
				else:
					print("----Erro-esperado-.")
					return False
			else:
				print("----Errro-esperado-<corpo>")
				return False
		else:
			print("----Erro-esperado-identificador")
			return False
	else:
		print("----Erro-esperado-program")
		return False

def corpo():
	global token
	if dc():
		if token[2] == "begin":
			print("----OK-begin")
			token = proxToken()
			if comandos():
				if token[2] == "end":
					print("----OK-end")
					return True
				else:
					print("----Erro-esperado-end")
					return False
			else:
				print("----Erro-esperado-<comandos>")
				return False
		else:
			print("----Erro-esperado-begin")
			return False
	else:
		print("----Erro-esperado-<dc>")
		return False

def dc():
	global token
	if dc_v():
		if mais_dc():
			return True
		else:
			print("----Erro-esperado-<mais_dc>")
			return False
	elif dc_p():
		if mais_dc():
			return True
		else:
			print("----Erro-esperado-<mais_dc>")
			return False
	else:
		print("----OK-<dc>-vazio")
		return True

def mais_dc():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if dc():
			return True
		else:
			print("----Erro-esperado-<dc>")
			return False
	else:
		print("----OK-<mais_dc>-vazio")
		return True

def dc_v():
	global token
	if token[2] == "var":
		print("----OK-var")
		token = proxToken()
		if variaveis():
			if token[2] == ":":
				print("----OK-:")
				token = proxToken()
				if tipo_var():
					return True
				else:
					print("----Erro-esperado-<tipo_var>")
					return False
			else:
				print("----Erro-esperado-:")
				return False
		else:
			print("----Erro-esperado-<variaveis>")
			return False
	else:
		print("----Erro-esperado-var")
		return False

def tipo_var():
	global token
	if token[1] == "nReal":
		print("----OK-número-real")
		token = proxToken()
		return True
	elif token[1] == "nInteger":
		print("----OK-número-inteiro")
		token = proxToken()
		return True
	else:
		print("----Erro-esperado-real-ou-inteiro")
		return False

def variaveis():
	global token
	if token[1] == "identificador":
		print("----OK-identificador")
		token = proxToken()
		if mais_var():
			return True
		else:
			print("----Erro-esperado-<mais_var>")
			return False
	else:
		print("----Erro-esperado-identificador")
		return False

def mais_var():
	global token
	if token[2] == ",":
		print("----OK-,")
		token = proxToken()
		if variaveis():
			return True
		else:
			print("----Erro-esperado-<variaveis>")
			return False
	else:
		print("----OK-<mais_var>-vazio")
		return True

def dc_p():
	global token
	if token[2] == "procedure":
		print("----OK-procedure")
		token = proxToken()
		if token[1] == "identificador":
			print("----OK-identificador")
			token = proxToken()
			if parametros():
				if corpo_p():
					return True
				else:
					print("----Erro-esperado-<corpo_p>")
					return False
			else:
				print("----Erro-esperado-<parametros>")
				return False
		else:
			print("----Erro-esperado-identificador")
			return False
	else:
		print("----Erro-esperado-procedure")
		return False

def parametros():
	global token
	if token[2] == "(":
		print("----OK-(")
		token = proxToken()
		if lista_par():
			if token[2] == ")":
				print("----OK-)")
				token = proxToken()
				return True
			else:
				print("----Erro-esperado-)")
				return False
		else:
			print("----Erro-esperado-<lista_par>")
			return False
	else:
		print("----OK-<parametros>-vazio")
		return True

def lista_par():
	global token
	if variaveis():
		if token[2] == ":":
			print("----OK-:")
			token = proxToken()
			if tipo_var():
				if mais_par():
					return True
				else:
					print("----Erro-esperado-<mais_par>")
					return False
			else:
				print("----Erro-esperado-<tipo_var>")
				return False
		else:
			print("----Erro-esperado-:")
			return False
	else:
		print("----Erro-esperado-<variaveis>")
		return False

def mais_par():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if lista_par():
			return True
		else:
			print("----Erro-esperado-<lista_par>")
			return False
	else:
		print("----Ok-<mais_par>-vazio")
		return True

def corpo_p():
	global token
	if dc_loc():
		if token[2] == "begin":
			print("----OK-begin")
			token = proxToken()
			if comandos():
				if token[2] == "end":
					print("----Ok-end")
					token = proxToken()
					return True
				else:
					print("----Erro-esperado-end")
					return False
			else:
				print("----Erro-esperado-<comandos>")
				return False
		else:
			print("----Erro-esperado-begin")
			return False
	else:
		print("----Erro-esperado-<corpo_p>")
		return False

def dc_loc():
	global token
	if dc_v():
		if mais_dcloc():
			return True
		else:
			print("----Erro-esperado-<mais_dcloc>")
			return False
	else:
		print("----OK-<dc_loc>-vazio")
		return True

def mais_dcloc():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if dc_loc():
			return True
		else:
			print("----Erro-esperado-<dc_loc>")
			return False
	else:
		print("----OK-<mais_dcloc>-vazio")

def lista_arg():
	global token
	if token[2] == "(":
		print("----OK-(")
		token = proxToken()
		if argumentos():
			if token[2] == ")":
				print("----OK-)")
				token = proxToken()
				return True
			else:
				print("----Erro-esperado-)")
				return False
		else:
			print("----Erro-esperado-<argumentos>")
			return False
	else:
		print("----OK-<lista_arg>-vazio")
		return True

def argumentos():
	global token
	if token[1] == "identificador":
		print("----OK-identificador")
		token = proxToken()
		if mais_ident():
			return True
		else:
			print("----Erro-esperado-<mais_ident>")
			return False
	else:
		print("----Erro-esperado-identificador")
		return False

def mais_ident():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if argumentos():
			return True
		else:
			print("----Erro-esperado-<argumentos>")
			return False
	else:
		print("----OK-<mais_ident>-vazio")
		return True

def pfalsa():
	global token
	if token[2] == "else":
		print("----OK-else")
		token = proxToken()
		if argumentos():
			return True
		else:
			print("----Erro-esperado-<argumentos>")
			return False
	else:
		print("----OK-<pfalsa>-vazio")
		return True

def comandos():
	

token = proxToken()
print(S())