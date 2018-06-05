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
	if token[2] == "program":
		programa()
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
			if token[2] == ";":
				print("29---OK-;")
				token = proxToken()
				if corpo():
					if token[2] == ".":
						print("33---OK-.")
						return True
					else:
						print("36---Erro-esperado-.")
						return False
				else:
					print("39---Errro-esperado-<corpo>")
					return False
			else:
				print("42---Erro-esperado-;")
				return False
		else:
			print("45---Erro-esperado-identificador")
			return False
	else:
		print("48---Erro-esperado-program")
		return False

def corpo():
	global token
	if dc():
		if token[2] == "begin":
			print("55---OK-begin")
			token = proxToken()
			if comandos():
				if token[2] == "end":
					print("59---OK-end")
					return True
				else:
					print("62---Erro-esperado-end")
					return False
			else:
				print("65---Erro-esperado-<comandos>")
				return False
		else:
			print("68---Erro-esperado-begin")
			return False
	else:
		print("71---Erro-esperado-<dc>")
		return False

def dc():
	global token
	if token[2] == "var":
		dc_v()
		if token[2] == ";":
			mais_dc()
		else:
			print("81---Erro-esperado-<mais_dc>")
			return False
	elif token[2] == "procedure":
		dc_p()
		if token[2] == ";":
			mais_dc()
		else:
			print("88---Erro-esperado-<mais_dc>")
			return False
	else:
		print("91---OK-<dc>-vazio")
		return True

def mais_dc():
	global token
	if token[2] == ";":
		print("97---OK-;")
		token = proxToken()
		if dc():
			return True
		else:
			print("102---Erro-esperado-<dc>")
			return False
	else:
		print("105---OK-<mais_dc>-vazio")
		return True

def dc_v():
	global token
	if token[2] == "var":
		print("111---OK-var")
		token = proxToken()
		if token[1] == "identificador":
			variaveis()
			if token[2] == ":":
				print("116---OK-:")
				token = proxToken()
				if token[2] == "real" or token[2] == "integer":
					tipo_var()
				else:
					print("121---Erro-esperado-<tipo_var>")
					return False
			else:
				print("124---Erro-esperado-:")
				return False
		else:
			print("127---Erro-esperado-<variaveis>")
			return False
	else:
		print("130---Erro-esperado-var")
		return False

def tipo_var():
	global token
	if token[2] == "real":
		print("136---OK-tipo-real")
		token = proxToken()
		return True
	elif token[2] == "integer":
		print("140---OK-tipo-inteiro")
		token = proxToken()
		return True
	else:
		print("144---Erro-esperado-real-ou-inteiro")
		return False

def variaveis():
	global token
	if token[1] == "identificador":
		print("150---OK-identificador")
		token = proxToken()
		if token[2] == ",":
			mais_var()
		else:
			print("155---OK-<mais_var>-vazio")
			return True
	else:
		print("158---Erro-esperado-identificador")
		return False

def mais_var():
	global token
	if token[2] == ",":
		print("164---OK-,")
		token = proxToken()
		if token[1] == "identificador":
			variaveis()
		else:
			print("169---Erro-esperado-<variaveis>")
			return False
	else:
		print("172---OK-<mais_var>-vazio")
		return True

def dc_p():
	global token
	if token[2] == "procedure":
		print("178---OK-procedure")
		token = proxToken()
		if token[1] == "identificador":
			print("181---OK-identificador")
			token = proxToken()
			if parametros():
				if corpo_p():
					return True
				else:
					print("187---Erro-esperado-<corpo_p>")
					return False
			else:
				print("190---Erro-esperado-<parametros>")
				return False
		else:
			print("193---Erro-esperado-identificador")
			return False
	else:
		print("196---Erro-esperado-procedure")
		return False

def parametros():
	global token
	if token[2] == "(":
		print("202---OK-(")
		token = proxToken()
		if lista_par():
			if token[2] == ")":
				print("206---OK-)")
				token = proxToken()
				return True
			else:
				print("210---Erro-esperado-)")
				return False
		else:
			print("213---Erro-esperado-<lista_par>")
			return False
	else:
		print("216---OK-<parametros>-vazio")
		return True

def lista_par():
	global token
	if token[1] == "identificador":
		variaveis()
		if token[2] == ":":
			print("224---OK-:")
			token = proxToken()
			if token[2] == "real" or token[2] == "integer":
				tipo_var()
				if token[2] == ";":
					mais_par()
					return True
				else:
					print("232---OK-<mais_par>-vazio")
					return True
			else:
				print("235---Erro-esperado-<tipo_var>")
				return False
		else:
			print("238---Erro-esperado-:")
			return False
	else:
		print("241---Erro-esperado-<variaveis>")
		return False

def mais_par():
	global token
	if token[2] == ";":
		print("247---OK-;")
		token = proxToken()
		if lista_par():
			return True
		else:
			print("252---Erro-esperado-<lista_par>")
			return False
	else:
		print("255---Ok-<mais_par>-vazio")
		return True

def corpo_p():
	global token
	if dc_loc():
		if token[2] == "begin":
			print("262---OK-begin")
			token = proxToken()
			if comandos():
				if token[2] == "end":
					print("266---Ok-end")
					token = proxToken()
					return True
				else:
					print("270---Erro-esperado-end")
					return False
			else:
				print("273---Erro-esperado-<comandos>")
				return False
		else:
			print("276---Erro-esperado-begin")
			return False
	else:
		print("279---Erro-esperado-<corpo_p>")
		return False

def dc_loc():
	global token
	if token[2] == "var":
		dc_v()
		if token[2] == ";":
			mais_dcloc()
			return True
		else:
			print("290---Erro-esperado-<mais_dcloc>")
			return False
	else:
		print("293---OK-<dc_loc>-vazio")
		return True

def mais_dcloc():
	global token
	if token[2] == ";":
		print("299---OK-;")
		token = proxToken()
		if dc_loc():
			return True
		else:
			print("304---Erro-esperado-<dc_loc>")
			return False
	else:
		print("307---OK-<mais_dcloc>-vazio")

def lista_arg():
	global token
	if token[2] == "(":
		print("312---OK-(")
		token = proxToken()
		if token[1] == "identificador":
			argumentos()
			if token[2] == ")":
				print("317---OK-)")
				token = proxToken()
				return True
			else:
				print("321---Erro-esperado-)")
				return False
		else:
			print("324---Erro-esperado-<argumentos>")
			return False
	else:
		print("327---OK-<lista_arg>-vazio")
		return True

def argumentos():
	global token
	if token[1] == "identificador":
		print("333---OK-identificador")
		token = proxToken()
		if token[2] == ";":
			mais_ident()
			return True
		else:
			print("339---Erro-esperado-<mais_ident>")
			return False
	else:
		print("342---Erro-esperado-identificador")
		return False

def mais_ident():
	global token
	if token[2] == ";":
		print("348---OK-;")
		token = proxToken()
		if token[1] == "identificador":
			argumentos()
			return True
		else:
			print("354---Erro-esperado-<argumentos>")
			return False
	else:
		print("357---OK-<mais_ident>-vazio")
		return True

def pfalsa():
	global token
	if token[2] == "else":
		print("363---OK-else")
		token = proxToken()
		if argumentos():
			return True
		else:
			print("368---Erro-esperado-<argumentos>")
			return False
	else:
		print("371---OK-<pfalsa>-vazio")
		return True

def comandos():
	global token
	if token[2] == "read" or token[2] == "write" or token[2] == "while" or token[2] == "if" or token[1] == "identificador":
		comando()
		if token[2] == ";":
			mais_comandos()
			return True
		else:
			print("382---Erro-esperado-<mais_comandos>")
			return False
	else:
		print("385---OK-<comandos>-vazio")
		return True

def mais_comandos():
	global token
	if token[2] == ";":
		print("391---OK-;")
		token = proxToken()
		if comandos():
			return True
		else:
			print("396---Erro-esperado-<comandos>")
			return False
	else:
		print("399---OK-<mais_comandos>-vazio")
		return True

def comando():
	global token
	if token[2] == "read":
		print("405---OK-read")
		token = proxToken()
		if token[2] == "(":
			print("408---OK-(")
			token = proxToken()
			if token[1] == "identificador":
				variaveis()
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
	elif token[2] == "write":
		print("426---OK-write")
		token = proxToken()
		if token[2] == "(":
			print("429---OK-(")
			token = proxToken()
			if token[1] == "identificador":
				variaveis()
				if token[2] == ")":
					print("434---OK-)")
					token = proxToken()
					return True
				else:
					print("438---Erro-esperado-)")
					return False
			else:
				print("441---Erro-esperado-<variaveis>")
				return False
		else:
			print("444---Erro-esperado-(")
			return False
	elif token[2] == "while":
		print("447---OK-while")
		token = proxToken()
		if condicao():
			if token[2] == "do":
				print("451---OK-do")
				token = proxToken()
				if comandos():
					if token[2] == "$":
						print("455---OK-$")
						token = proxToken()
						return True
					else:
						print("459---Erro-esperado-$")
						return False
				else:
					print("462---Erro-esperado-<comandos>")
					return False
			else:
				print("465---Erro-esperado-do")
				return False
		else:
			print("468---Erro-esperado-<condicao>")
			return False
	elif token[2] == "if":
		print("471---OK-if")
		token = proxToken()
		if condicao():
			if token[2] == "then":
				print("475---OK-then")
				token = proxToken()
				if comandos():
					if pfalsa():
						if token[2] == "$":
							print("480---OK-$")
							token = proxToken()
							return True
						else:
							print("484---Erro-esperado-$")
							return False
					else:
						print("487---Erro-esperado-<pfalsa>")
						return False
				else:
					print("490---Erro-esperado-<pfalsa>")
					return False
			else:
				print("493---Erro-esperado-then")
				return False
		else:
			print("496---Erro-esperado-<condicao>")
			return False
	elif token[1] == "identificador":
		print("499---OK-identificador")
		token = proxToken()
		if token[2] == ":=":
			restoIdent()
			return True
		else:
			print("505---Erro-esperado-<restoIdent>")
			return False
	else:
		print("508--Erro-esperado-read-ou-write-ou-while-ou-if-ou-ident")
		return False

def restoIdent():
	global token
	if token[2] == ":=":
		print("514---OK-:=")
		token = proxToken()
		if expressao():
			return True
		else:
			print("519--Erro-esperado-<expressao>")
			return False
	elif token[2] == "(":
		lista_arg()
		return True
	else:
		print("525---Erro-esperado-:=-ou-<lista_arg>")
		return False

def condicao():
	global token
	if expressao():
		if token[2] == "=" or token[2] == "<>" or token[2] == ">=" or token[2] == "<=" or token[2] == ">" or token[2] == "<":
			relacao()
			if expressao():
				return True
			else:
				print("536---Erro-esperado-<expressao>")
				return False
		else:
			print("539---Erro-esperado-<relacao>")
			return False
	else:
		print("542---Erro-esperado-<expressao>")
		return False

def relacao():
	global token
	if token[2] == "=":
		print("548---OK-=")
		token = proxToken()
		return True
	elif token[2] == "<":
		print("552---OK-<")
		token = proxToken()
		if token[2] == ">":
			print("555---OK->")
			token = proxToken()
			return True
		elif token[2] == "=":
			print("559---OK-=")
			token = proxToken()
			return True
		else:
			print("563---OK-pode-ser-só-<")
			return True
	elif token[2] == ">":
		print("566---OK->")
		token = proxToken()
		if token[2] == "=":
			print("569---OK-=")
			token = proxToken()
			return True
		else:
			print("573---OK-pode-ser-só->")
			return True
	else:
		print("576---Erro-esperado-=-ou-<-ou->-ou-<=-ou->=-ou-<>")
		return False

def expressao():
	global token
	if termo():
		if outros_termos():
			return True
		else:
			print("585---Erro-esperado-<outros_termos>")
			return False
	else:
		print("588---Erro-esperado-<termo>")
		return False

def op_un():
	global token
	if token[2] == "+":
		print("594---OK-+")
		token = proxToken()
		return True
	elif token[2] == "-":
		print("598---OK--")
		token = proxToken()
		return True
	else:
		print("602---OK-<op_un>-vazio")
		return True

def outros_termos():
	global token
	if token[2] == "+" or token[2] == "-":
		op_ad()
		if termo():
			if outros_termos():
				return True
			else:
				print("613---Erro-esperado-<outros_termos>")
				return False
		else:
			print("616---Erro-esperado-<termo>")
			return False
	else:
		print("619---Ok-<outros_termos>-vazio")
		return True

def op_ad():
	global token
	if token[2] == "+":
		print("625---OK-+")
		token = proxToken()
		return True
	elif token[2] == "-":
		print("629---OK--")
		token = proxToken()
		return True
	else:
		print("633---Erro-esperado-+-ou--")
		return False

def termo():
	global token
	if op_un():
		if token[1] == "identificador":
			fator()
			if mais_fatores():
				return True
			else:
				print("644---Erro-esperado-<mais_fatores>")
				return False
		else:
			print("647---Erro-esperado-<fator>")
			return False
	else:
		print("650---Erro-esperado-<op_un>")
		return False

def mais_fatores():
	global token
	if op_mul():
		if fator():
			if mais_fatores():
				return True
			else:
				print("660---Erro-esperado-<mais_fatores>")
				return False
		else:
			print("663---Erro-esperado-<fator>")
			return False
	else:
		print("666---OK-<op_mul>-vazio")
		return True

def op_mul():
	global token
	if token[2] == "*":
		print("672---OK-*")
		token = proxToken()
		return True
	elif token[2] == "/":
		print("676---OK-/")
		token = proxToken()
		return True
	else:
		print("680---Erro-esperado-*-ou-/")
		return False

def fator():
	global token
	if token[1] == "identificador":
		print("686---OK-identificador")
		token = proxToken()
		return True
	elif token[1] == "nInteger":
		print("690---OK-número-inteiro")
		token = proxToken()
		return True
	elif token[1] == "nReal":
		print("694---OK-número-real")
		token = proxToken()
		return True
	elif token[2] == "(":
		print("698---OK-(")
		token = proxToken()
		if expressao():
			if token[2] == ")":
				print("702---OK-)")
				token = proxToken()
				return True
			else:
				print("706---Erro-esperado-)")
				return False
		else:
			print("709---Erro-esperado-<expressao>")
			return False
	else:
		print("712---Erro-esperado-identificador-ou-<numero_int>-ou-<numero_real>-ou-(")
		return False

token = proxToken()
S()