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
		print("Código valido")
		return True
	else:
		return False

def programa():
	global token
	if token[2] == "program":
		print("----OK-program")
		token = proxToken()
		if token[1] == "identificador":
			print("----OK-identificador")
			token = proxToken()
			if token[2] == ";":
				print("----OK-;")
				token = proxToken()
				if corpo():
					if token[2] == ".":
						print("----OK-.")
						return True
					else:
						print("----Erro-esperado-.")
						return False
				else:
					return False
			else:
				print("----Erro-esperado-;")
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
					token = proxToken()
					return True
				else:
					print("----Erro-esperado-end")
					return False
			else:
				return False
		else:
			print("----Erro-esperado-begin")
			return False
	else:
		return False

def dc():
	global token
	if token[2] == "var":
		dc_v()
		if mais_dc():
			return True
		else:
			return False
	elif token[2] == "procedure":
		dc_p()
		if mais_dc():
			return True
		else:
			return False
	else:
		return True

def mais_dc():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if dc():
			return True
		else:
			return False
	else:
		return True

def dc_v():
	global token
	if token[2] == "var":
		print("----OK-var")
		token = proxToken()
		if token[1] == "identificador":
			variaveis()
			if token[2] == ":":
				print("----OK-:")
				token = proxToken()
				if token[2] == "real" or token[2] == "integer":
					tipo_var()
				else:
					return False
			else:
				print("----Erro-esperado-:")
				return False
		else:
			return False
	else:
		print("----Erro-esperado-var")
		return False

def tipo_var():
	global token
	if token[2] == "real":
		print("----OK-tipo-real")
		token = proxToken()
		return True
	elif token[2] == "integer":
		print("----OK-tipo-inteiro")
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
		if token[2] == ",":
			mais_var()
		else:
			return True
	else:
		print("----Erro-esperado-identificador")
		return False

def mais_var():
	global token
	if token[2] == ",":
		print("----OK-,")
		token = proxToken()
		if token[1] == "identificador":
			variaveis()
		else:
			return False
	else:
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
					return False
			else:
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
			return False
	else:
		return True

def lista_par():
	global token
	if token[1] == "identificador":
		variaveis()
		if token[2] == ":":
			print("----OK-:")
			token = proxToken()
			if token[2] == "real" or token[2] == "integer":
				tipo_var()
				if token[2] == ";":
					mais_par()
					return True
				else:
					return True
			else:
				return False
		else:
			print("----Erro-esperado-:")
			return False
	else:
		return False

def mais_par():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if lista_par():
			return True
		else:
			return False
	else:
		return True

def corpo_p():
	global token
	if dc_loc():
		if token[2] == "begin":
			print("----OK-begin")
			token = proxToken()
			if comandos():
				if token[2] == "end":
					print("----OK-end")
					token = proxToken()
					return True
				else:
					print("----Erro-esperado-end")
					return False
			else:
				return False
		else:
			print("----Erro-esperado-begin")
			return False
	else:
		return False

def dc_loc():
	global token
	if token[2] == "var":
		dc_v()
		if token[2] == ";":
			mais_dcloc()
			return True
		else:
			return False
	else:
		return True

def mais_dcloc():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if dc_loc():
			return True
		else:
			return False
	else:
		return True

def lista_arg():
	global token
	if token[2] == "(":
		print("----OK-(")
		token = proxToken()
		if token[1] == "identificador":
			argumentos()
			if token[2] == ")":
				print("----OK-)")
				token = proxToken()
				return True
			else:
				print("----Erro-esperado-)")
				return False
		else:
			return False
	else:
		return True

def argumentos():
	global token
	if token[1] == "identificador":
		print("----OK-identificador")
		token = proxToken()
		if mais_ident():
			return True
		else:
			return False
	else:
		print("----Erro-esperado-identificador")
		return False

def mais_ident():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if token[1] == "identificador":
			argumentos()
			return True
		else:
			return False
	else:
		return True

def pfalsa():
	global token
	if token[2] == "else":
		print("----OK-else")
		token = proxToken()
		if argumentos():
			return True
		else:
			return False
	else:
		return True

def comandos():
	global token
	if token[2] == "read" or token[2] == "write" or token[2] == "while" or token[2] == "if" or token[1] == "identificador":
		comando()
		if token[2] == ";":
			mais_comandos()
			return True
		else:
			return True
	else:
		return True

def mais_comandos():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		if comandos():
			return True
		else:
			return False
	else:
		return True

def comando():
	global token
	if token[2] == "read":
		print("----OK-read")
		token = proxToken()
		if token[2] == "(":
			print("----OK-(")
			token = proxToken()
			if token[1] == "identificador":
				variaveis()
				if token[2] == ")":
					print("----OK-)")
					token = proxToken()
					return True
				else:
					print("----Erro-esperado-)")
					return False
			else:
				return False
		else:
			print("----Erro-esperado-(")
			return False
	elif token[2] == "write":
		print("----OK-write")
		token = proxToken()
		if token[2] == "(":
			print("----OK-(")
			token = proxToken()
			if token[1] == "identificador":
				variaveis()
				if token[2] == ")":
					print("----OK-)")
					token = proxToken()
					return True
				else:
					print("----Erro-esperado-)")
					return False
			else:
				return False
		else:
			print("----Erro-esperado-(")
			return False
	elif token[2] == "while":
		print("----OK-while")
		token = proxToken()
		if token[2] == "(":
			print("----OK-(")
			token = proxToken()
			if condicao():
				if token[2] == ")":
					print("----OK-)")
					token = proxToken()
					if token[2] == "do":
						print("----OK-do")
						token = proxToken()
						if comandos():
							if token[2] == "$":
								print("----OK-$")
								token = proxToken()
								return True
							else:
								print("----Erro-esperado-$")
								return False
						else:
							return False
					else:
						print("----Erro-esperado-do")
						return False
				else:
					print("----Erro-esperado-)")
					return False
			else:
				return False
		else:
			print("----Erro-esperado-(")
			return False
	elif token[2] == "if":
		print("----OK-if")
		token = proxToken()
		if token[2] == "(":
			print("----OK-(")
			token = proxToken()
			if condicao():
				if token[2] == ")":
					print("----OK-)")
					token = proxToken()
					if token[2] == "then":
						print("----OK-then")
						token = proxToken()
						if comandos():
							if pfalsa():
								if token[2] == "$":
									print("----OK-$")
									token = proxToken()
									return True
								else:
									print("----Erro-esperado-$")
									return False
							else:
								return False
						else:
							return False
					else:
						print("----Erro-esperado-then")
						return False
				else:
					print("----Erro-esperado-)")
					return False
			else:
				return False
		else:
			print("----Erro-esperado-(")
			return False
	elif token[1] == "identificador":
		print("----OK-identificador")
		token = proxToken()
		if restoIdent():
			return True
		else:
			return False
	else:
		print("---Erro-esperado-read-ou-write-ou-while-ou-if-ou-ident")
		return False

def restoIdent():
	global token
	if token[2] == ":=":
		print("----OK-:=")
		token = proxToken()
		if expressao():
			return True
		else:
			return False
	elif token[2] == "(":
		lista_arg()
		return True
	else:
		return False

def condicao():
	global token
	if expressao():
		if token[2] == "=" or token[2] == "<>" or token[2] == ">=" or token[2] == "<=" or token[2] == ">" or token[2] == "<":
			relacao()
			if expressao():
				return True
			else:
				return False
		else:
			return False
	else:
		return False

def relacao():
	global token
	if token[2] == "=":
		print("----OK-=")
		token = proxToken()
		return True
	elif token[2] == "<>":
		print("----OK-<>")
		token = proxToken()
		return True
	elif token[2] == ">=":
		print("----OK->=")
		token = proxToken()
		return True
	elif token[2] == "<=":
		print("----OK-<=")
		token = proxToken()
		return True
	elif token[2] == ">":
		print("----OK->")
		token = proxToken()
		return True
	elif token[2] == "<":
		print("----OK-<")
		token = proxToken()
		return True
	else:
		print("----Erro-esperado-=-ou-<-ou->-ou-<=-ou->=-ou-<>")
		print(token)
		return False

def expressao():
	global token
	if termo():
		if outros_termos():
			return True
		else:
			return False
	else:
		return False

def op_un():
	global token
	if token[2] == "+":
		print("----OK-+")
		token = proxToken()
		return True
	elif token[2] == "-":
		print("----OK--")
		token = proxToken()
		return True
	else:
		return True

def outros_termos():
	global token
	if token[2] == "+" or token[2] == "-":
		op_ad()
		if termo():
			if outros_termos():
				return True
			else:
				return False
		else:
			return False
	else:
		return True

def op_ad():
	global token
	if token[2] == "+":
		print("----OK-+")
		token = proxToken()
		return True
	elif token[2] == "-":
		print("----OK--")
		token = proxToken()
		return True
	else:
		print("----Erro-esperado-+-ou--")
		return False

def termo():
	global token
	if op_un():
		if fator():
			if mais_fatores():
				return True
			else:
				return True
		else:
			return False
	else:
		return False

def mais_fatores():
	global token
	if token[2] == "*" or token[2] == "/":
		op_mul()
		if fator():
			if mais_fatores():
				return True
			else:
				return False
		else:
			return False
	else:
		return True

def op_mul():
	global token
	if token[2] == "*":
		print("----OK-*")
		token = proxToken()
		return True
	elif token[2] == "/":
		print("----OK-/")
		token = proxToken()
		return True
	else:
		print("----Erro-esperado-*-ou-/")
		return False

def fator():
	global token
	if token[1] == "identificador":
		print("----OK-identificador")
		token = proxToken()
		return True
	elif token[1] == "nInteger":
		print("----OK-número-inteiro")
		token = proxToken()
		return True
	elif token[1] == "nReal":
		print("----OK-número-real")
		token = proxToken()
		return True
	elif token[2] == "(":
		print("----OK-(")
		token = proxToken()
		if expressao():
			if token[2] == ")":
				print("----OK-)")
				token = proxToken()
				return True
			else:
				print("----Erro-esperado-)")
				return False
		else:
			return False
	else:
		print("----Erro-esperado-identificador-ou-<numero_int>-ou-<numero_real>-ou-(")
		return False

token = proxToken()
S()