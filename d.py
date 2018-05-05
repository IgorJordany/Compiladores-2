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
		print("17---Erro-esperado-<programa>")
		return False

def programa():
	global token
	if token[2] == "program":
		print("23---OK-program")
		token = proxToken()
		if token[1] == "identificador":
			print("26---OK-identificador")
			token = proxToken()
			if corpo():
				if token[2] == ".":
					print("30---OK-.")
					return True
				else:
					print("33---Erro-esperado-.")
					return False
			else:
				print("36---Errro-esperado-<corpo>")
				return False
		else:
			print("39---Erro-esperado-identificador")
			return False
	else:
		print("42---Erro-esperado-program")
		return False

def corpo():
	global token
	if dc():
		if token[2] == "begin":
			print("49---OK-begin")
			token = proxToken()
			if comandos():
				if token[2] == "end":
					print("53---OK-end")
					return True
				else:
					print("56---Erro-esperado-end")
					return False
			else:
				print("59---Erro-esperado-<comandos>")
				return False
		else:
			print("62---Erro-esperado-begin")
			return False
	else:
		print("65---Erro-esperado-<dc>")
		return False

def dc():
	global token
	if dc_v():
		if mais_dc():
			return True
		else:
			print("74---Erro-esperado-<mais_dc>")
			return False
	elif dc_p():
		if mais_dc():
			return True
		else:
			print("80---Erro-esperado-<mais_dc>")
			return False
	else:
		print("83---OK-<dc>-vazio")
		return True

def mais_dc():
	global token
	if token[2] == ";":
		print("89---OK-;")
		token = proxToken()
		if dc():
			return True
		else:
			print("94---Erro-esperado-<dc>")
			return False
	else:
		print("97---OK-<mais_dc>-vazio")
		return True

def dc_v():
	global token
	if token[2] == "var":
		print("103---OK-var")
		token = proxToken()
		if variaveis():
			if token[2] == ":":
				print("107---OK-:")
				token = proxToken()
				if tipo_var():
					return True
				else:
					print("112---Erro-esperado-<tipo_var>")
					return False
			else:
				print("115---Erro-esperado-:")
				return False
		else:
			print("118---Erro-esperado-<variaveis>")
			return False
	else:
		print("121---Erro-esperado-var")
		return False

def tipo_var():
	global token
	if token[2] == "real":
		print("127---OK-tipo-real")
		token = proxToken()
		return True
	elif token[2] == "integer":
		print("131---OK-tipo-inteiro")
		token = proxToken()
		return True
	else:
		print("135---Erro-esperado-real-ou-inteiro")
		return False

def variaveis():
	global token
	if token[1] == "identificador":
		print("141---OK-identificador")
		token = proxToken()
		if mais_var():
			return True
		else:
			print("146---Erro-esperado-<mais_var>")
			return False
	else:
		print("149---Erro-esperado-identificador")
		return False

def mais_var():
	global token
	if token[2] == ",":
		print("155---OK-,")
		token = proxToken()
		if variaveis():
			return True
		else:
			print("160---Erro-esperado-<variaveis>")
			return False
	else:
		print("163---OK-<mais_var>-vazio")
		return True

def dc_p():
	global token
	if token[2] == "procedure":
		print("169---OK-procedure")
		token = proxToken()
		if token[1] == "identificador":
			print("172---OK-identificador")
			token = proxToken()
			if parametros():
				if corpo_p():
					return True
				else:
					print("178---Erro-esperado-<corpo_p>")
					return False
			else:
				print("181---Erro-esperado-<parametros>")
				return False
		else:
			print("184---Erro-esperado-identificador")
			return False
	else:
		print("187---Erro-esperado-procedure")
		return False

def parametros():
	global token
	if token[2] == "(":
		print("193---OK-(")
		token = proxToken()
		if lista_par():
			if token[2] == ")":
				print("197---OK-)")
				token = proxToken()
				return True
			else:
				print("201---Erro-esperado-)")
				return False
		else:
			print("204---Erro-esperado-<lista_par>")
			return False
	else:
		print("207---OK-<parametros>-vazio")
		return True

def lista_par():
	global token
	if variaveis():
		if token[2] == ":":
			print("214---OK-:")
			token = proxToken()
			if tipo_var():
				if mais_par():
					return True
				else:
					print("220---Erro-esperado-<mais_par>")
					return False
			else:
				print("223---Erro-esperado-<tipo_var>")
				return False
		else:
			print("226---Erro-esperado-:")
			return False
	else:
		print("229---Erro-esperado-<variaveis>")
		return False

def mais_par():
	global token
	if token[2] == ";":
		print("235---OK-;")
		token = proxToken()
		if lista_par():
			return True
		else:
			print("240---Erro-esperado-<lista_par>")
			return False
	else:
		print("243---Ok-<mais_par>-vazio")
		return True

def corpo_p():
	global token
	if dc_loc():
		if token[2] == "begin":
			print("250---OK-begin")
			token = proxToken()
			if comandos():
				if token[2] == "end":
					print("254---Ok-end")
					token = proxToken()
					return True
				else:
					print("258---Erro-esperado-end")
					return False
			else:
				print("261---Erro-esperado-<comandos>")
				return False
		else:
			print("264---Erro-esperado-begin")
			return False
	else:
		print("267---Erro-esperado-<corpo_p>")
		return False

def dc_loc():
	global token
	if dc_v():
		if mais_dcloc():
			return True
		else:
			print("276---Erro-esperado-<mais_dcloc>")
			return False
	else:
		print("279---OK-<dc_loc>-vazio")
		return True

def mais_dcloc():
	global token
	if token[2] == ";":
		print("285---OK-;")
		token = proxToken()
		if dc_loc():
			return True
		else:
			print("290---Erro-esperado-<dc_loc>")
			return False
	else:
		print("293---OK-<mais_dcloc>-vazio")

def lista_arg():
	global token
	if token[2] == "(":
		print("298---OK-(")
		token = proxToken()
		if argumentos():
			if token[2] == ")":
				print("302---OK-)")
				token = proxToken()
				return True
			else:
				print("306---Erro-esperado-)")
				return False
		else:
			print("309---Erro-esperado-<argumentos>")
			return False
	else:
		print("312---OK-<lista_arg>-vazio")
		return True

def argumentos():
	global token
	if token[1] == "identificador":
		print("318---OK-identificador")
		token = proxToken()
		if mais_ident():
			return True
		else:
			print("323---Erro-esperado-<mais_ident>")
			return False
	else:
		print("326---Erro-esperado-identificador")
		return False

def mais_ident():
	global token
	if token[2] == ";":
		print("332---OK-;")
		token = proxToken()
		if argumentos():
			return True
		else:
			print("337---Erro-esperado-<argumentos>")
			return False
	else:
		print("340---OK-<mais_ident>-vazio")
		return True

def pfalsa():
	global token
	if token[2] == "else":
		print("346---OK-else")
		token = proxToken()
		if argumentos():
			return True
		else:
			print("351---Erro-esperado-<argumentos>")
			return False
	else:
		print("354---OK-<pfalsa>-vazio")
		return True

def comandos():
	global token
	if comando():
		if mais_comandos():
			return True
		else:
			print("363---Erro-esperado-<mais_comandos>")
			return False
	else:
		print("366---OK-<comandos>-vazio")
		return True

def mais_comandos():
	global token
	if token[2] == ";":
		print("372---OK-;")
		token = proxToken()
		if comandos():
			return True
		else:
			print("377---Erro-esperado-<comandos>")
			return False
	else:
		print("380---OK-<mais_comandos>-vazio")
		return True

def comando():
	global token
	if token[2] == "read":
		print("386---OK-read")
		token = proxToken()
		if token[2] == "(":
			print("389---OK-(")
			token = proxToken()
			if variaveis():
				if token[2] == ")":
					print("393---OK-)")
					token = proxToken()
					return True
				else:
					print("397---Erro-esperado-)")
					return False
			else:
				print("400---Erro-esperado-<variaveis>")
				return False
		else:
			print("403---Erro-esperado-(")
			return False
	elif token[2] == "write":
		print("406---OK-write")
		token = proxToken()
		if token[2] == "(":
			print("409---OK-(")
			token = proxToken()
			if variaveis():
				if token[2] == ")":
					print("413---OK-)")
					token = proxToken()
					return True
				else:
					print("417---Erro-esperado-)")
					return False
			else:
				print("420---Erro-esperado-<variaveis>")
				return False
		else:
			print("423---Erro-esperado-(")
			return False
	elif token[2] == "while":
		print("426---OK-while")
		token = proxToken()
		if condicao():
			if token[2] == "do":
				print("430---OK-do")
				token = proxToken()
				if comandos():
					if token[2] == "$":
						print("434---OK-$")
						token = proxToken()
						return True
					else:
						print("438---Erro-esperado-$")
						return False
				else:
					print("441---Erro-esperado-<comandos>")
					return False
			else:
				print("444---Erro-esperado-do")
				return False
		else:
			print("447---Erro-esperado-<condicao>")
			return False
	elif token[2] == "if":
		print("450---OK-if")
		token = proxToken()
		if condicao():
			if token[2] == "then":
				print("454---OK-then")
				token = proxToken()
				if comandos():
					if pfalsa():
						if token[2] == "$":
							print("459---OK-$")
							token = proxToken()
							return True
						else:
							print("463---Erro-esperado-$")
							return False
					else:
						print("466---Erro-esperado-<pfalsa>")
						return False
				else:
					print("469---Erro-esperado-<pfalsa>")
					return False
			else:
				print("472---Erro-esperado-then")
				return False
		else:
			print("475---Erro-esperado-<condicao>")
			return False
	elif token[1] == "identificador":
		print("478---OK-identificador")
		token = proxToken()
		if restoIdent():
			return True
		else:
			print("483---Erro-esperado-<restoIdent>")
			return False
	else:
		print("486--Erro-esperado-read-ou-write-ou-while-ou-if-ou-ident")
		return False

def restoIdent():
	global token
	if token[2] == ":=":
		print("492---OK-:=")
		token = proxToken()
		if expressao():
			return True
		else:
			print("497--Erro-esperado-<expressao>")
			return False
	elif lista_arg():
		return True
	else:
		print("502---Erro-esperado-:=-ou-<lista_arg>")
		return False

def condicao():
	global token
	if expressao():
		if relacao():
			if expressao():
				return True
			else:
				print("512---Erro-esperado-<expressao>")
				return False
		else:
			print("515---Erro-esperado-<relacao>")
			return False
	else:
		print("518---Erro-esperado-<expressao>")
		return False

def relacao():
	global token
	if token[2] == "=":
		print("524---OK-=")
		token = proxToken()
		return True
	elif token[2] == "<":
		print("528---OK-<")
		token = proxToken()
		if token[2] == ">":
			print("531---OK->")
			token = proxToken()
			return True
		elif token[2] == "=":
			print("535---OK-=")
			token = proxToken()
			return True
		else:
			print("539---OK-pode-ser-só-<")
			return True
	elif token[2] == ">":
		print("542---OK->")
		token = proxToken()
		if token[2] == "=":
			print("545---OK-=")
			token = proxToken()
			return True
		else:
			print("549---OK-pode-ser-só->")
			return True
	else:
		print("552---Erro-esperado-=-ou-<-ou->-ou-<=-ou->=-ou-<>")
		return False

def expressao():
	global token
	if termo():
		if outros_termos():
			return True
		else:
			print("561---Erro-esperado-<outros_termos>")
			return False
	else:
		print("564---Erro-esperado-<termo>")
		return False

def op_un():
	global token
	if token[2] == "+":
		print("570---OK-+")
		token = proxToken()
		return True
	elif token[2] == "-":
		print("574---OK--")
		token = proxToken()
		return True
	else:
		print("578---OK-<op_un>-vazio")
		return True

def outros_termos():
	global token
	if op_ad():
		if termo():
			if outros_termos():
				return True
			else:
				print("588---Erro-esperado-<outros_termos>")
				return False
		else:
			print("591---Erro-esperado-<termo>")
			return False
	else:
		print("594---Ok-<outros_termos>-vazio")
		return True

def op_ad():
	global token
	if token[2] == "+":
		print("600---OK-+")
		token = proxToken()
		return True
	elif token[2] == "-":
		print("604---OK--")
		token = proxToken()
		return True
	else:
		print("608---Erro-esperado-+-ou--")
		return False

def termo():
	global token
	if op_un():
		if fator():
			if mais_fatores():
				return True
			else:
				print("618---Erro-esperado-<mais_fatores>")
				return False
		else:
			print("621---Erro-esperado-<fator>")
			return False
	else:
		print("624---Erro-esperado-<op_un>")
		return False

def mais_fatores():
	global token
	if op_mul():
		if fator():
			if mais_fatores():
				return True
			else:
				print("634---Erro-esperado-<mais_fatores>")
				return False
		else:
			print("637---Erro-esperado-<fator>")
			return False
	else:
		print("640---OK-<op_mul>-vazio")
		return True

def op_mul():
	global token
	if token[2] == "*":
		print("646---OK-*")
		token = proxToken()
		return True
	elif token[2] == "/":
		print("650---OK-/")
		token = proxToken()
		return True
	else:
		print("654---Erro-esperado-*-ou-/")
		return False

def fator():
	global token
	if token[1] == "identificador":
		print("660---OK-identificador")
		token = proxToken()
		return True
	elif token[1] == "nInteger":
		print("664---OK-número-inteiro")
		token = proxToken()
		return True
	elif token[1] == "nReal":
		print("668---OK-número-real")
		token = proxToken()
		return True
	elif token[2] == "(":
		print("672---OK-(")
		token = proxToken()
		if expressao():
			if token[2] == ")":
				print("676---OK-)")
				token = proxToken()
				return True
			else:
				print("680---Erro-esperado-)")
				return False
		else:
			print("683---Erro-esperado-<expressao>")
			return False
	else:
		print("686---Erro-esperado-identificador-ou-<numero_int>-ou-<numero_real>-ou-(")
		return False

token = proxToken()
S()