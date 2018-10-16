#-*- coding: utf-8 -*-
#201411310006 - Igor Jordany Richtic Silva

from comp2AnalisadorLexico import *

def proxToken():
	if tokens:
		t = tokens.pop(0)
		return t.split(' ')
	else:
		return False

def S():
	r = programa()
	if r:
		print("Código valido")
		return True
	else:
		print("Erro sintatico")
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
				r = corpo()
				if r:
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
	r = dc()
	if r:
		if token[2] == "begin":
			print("----OK-begin")
			token = proxToken()
			r = comandos()
			if r:
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
		r = dc_v()
		if r:
			if token[2] == ";":
				r = mais_dc()
				if r:
					return True
				else:
					return False
			else:
				return True
		else:
			return False
	elif token[2] == "procedure":
		r = dc_p()
		if r:
			if token[2] == ";":
				r = mais_dc()
				if r:
					return True
				else:
					return False
			else:
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
		r = dc()
		if r:
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
					r = tipo_var()
					if r:
						return True
					else:
						return False
				else:
					return False
			else:
				print("----Erro-esperado-:")
				return False
		else:
			print("----Erro-esperado-identificador")
			return False
	else:
		print("----Erro-esperado-var")
		return False

def tipo_var():
	global token
	global listaux
	global parametro
	if parametro:
		cat = "parametro"
	else:
		cat = "var"
	if token[2] == "real":
		print("----OK-tipo-real")
		r = insereTabela(listaux,cat,token[2])
		listaux = []
		if not r:
			return False
		token = proxToken()
		return True
	elif token[2] == "integer":
		print("----OK-tipo-inteiro")
		r = insereTabela(listaux,cat,token[2])
		listaux = []
		if not r:
			return False
		token = proxToken()
		return True
	else:
		print("----Erro-esperado-real-ou-inteiro")
		return False

def variaveis():
	global token
	global listaux
	global read
	if token[1] == "identificador":
		print("----OK-identificador")
		if read:
			buscaEscopo()
			token = proxToken()
		else:
			listaux.append(token[2])
			token = proxToken()
		if token[2] == ",":
			r = mais_var()
			if r:
				return True
			else:
				return False
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
			r = variaveis()
			if r:
				return True
			else:
				return False
		else:
			return False
	else:
		return True

def dc_p():
	global token
	global procedimento
	global nomep
	if token[2] == "procedure":
		print("----OK-procedure")
		token = proxToken()
		procedimento = True
		if token[1] == "identificador":
			nomep = token[2]
			print("----OK-identificador")
			token = proxToken()
			r = parametros()
			if r:
				r = corpo_p()
				procedimento = False
				if r:
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
	global parametro
	if token[2] == "(":
		print("----OK-(")
		token = proxToken()
		parametro = True
		r = lista_par()
		parametro = False
		if r:
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
		r = lista_par()
		if r:
			return True
		else:
			return False
	else:
		return True

def corpo_p():
	global token
	r = dc_loc()
	if r:
		if token[2] == "begin":
			print("----OK-begin")
			token = proxToken()
			r = comandos()
			if r:
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
		r = dc_v()
		if r:
			r = mais_dcloc()
			if r:
				return True
			else:
				return False
		else:
			return False
	else:
		return True

def mais_dcloc():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		r = dc_loc()
		if r:
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
		buscaEscopo()
		token = proxToken()
		r = mais_ident()
		if r:
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
		r = argumentos()
		if r:
			return True
		else:
			return False
	else:
		return True

def comandos():
	global token
	if token[2] == "read" or token[2] == "write" or token[2] == "while" or token[2] == "if" or token[1] == "identificador" or token[2] == "$":
		r = comando()
		if r:
			if token[2] == ";":
				r = mais_comandos()
				if r:
					return True
				else:
					return False
			else:
				return True
		else:
			return False
	else:
		return False

def mais_comandos():
	global token
	if token[2] == ";":
		print("----OK-;")
		token = proxToken()
		r = comandos()
		if r:
			return True
		else:
			return False
	else:
		return True

def comando():
	global tipo
	global token
	global read
	if token[2] == "read":
		read = True
		print("----OK-read")
		token = proxToken()
		if token[2] == "(":
			print("----OK-(")
			token = proxToken()
			if token[1] == "identificador": 
				r = variaveis()
				read = False
				if r:
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
				read = True
				r = variaveis()
				read = False
				if r:
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
			r = condicao()
			if r:
				if token[2] == ")":
					print("----OK-)")
					token = proxToken()
					if token[2] == "do":
						print("----OK-do")
						token = proxToken()
						r = comandos()
						if r:
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
			r = condicao()
			if r:
				if token[2] == ")":
					print("----OK-)")
					token = proxToken()
					if token[2] == "then":
						print("----OK-then")
						token = proxToken()
						r = comandos()
						if r:
							r = pfalsa()
							if r:
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
		buscaEscopo()
		tipo = buscaEscopor()
		token = proxToken()
		r = restoIdent()
		if r:
			return True
		else:
			return False
	elif token[2] == "$":
		return True
	else:
		print("---Erro-esperado-read-ou-write-ou-while-ou-if-ou-ident")
		return False

def restoIdent():
	global token
	global exp
	if token[2] == ":=":
		print("----OK-:=")
		exp = True
		token = proxToken()
		r = expressao()
		exp = False
		if r:
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
	r = expressao()
	if r:
		if token[2] == "=" or token[2] == "<>" or token[2] == ">=" or token[2] == "<=" or token[2] == ">" or token[2] == "<":
			relacao()
			r = expressao()
			if r:
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
	r = termo()
	if r:
		r = outros_termos()
		if r:
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
		r = termo()
		if r:
			r = outros_termos()
			if r:
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
	r = op_un()
	if r:
		r = fator()
		if r:
			r = mais_fatores()
			if r:
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
		r = fator()
		if r:
			r = mais_fatores()
			if r:
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
	global exp
	global tipo
	if token[1] == "identificador":
		print("----OK-identificador")
		r = buscaEscopo()
		if r:
			if exp:
				tipo2 = buscaEscopor()
				if tipo == tipo2:
					token = proxToken()
					return True
				else:
					print("----Erro-operacao-com-tipos-diferentes")
					return False
			else:
				token = proxToken()
				return True
		else:
			return False
	elif token[1] == "nInteger":
		print("----OK-número-inteiro")
		if exp:
			if tipo == "integer":
				token = proxToken()
				return True
			else:
				print("----Erro-operacao-com-tipos-diferentes")
				print(tipo)
				return False
		else:
			token = proxToken()
			return True
	elif token[1] == "nReal":
		print("----OK-número-real")
		if exp:
			if tipo == "real":
				token = proxToken()
				return True
			else:
				print("----Erro-operacao-com-tipos-diferentes")
				print(tipo)
				return False
		else:
			token = proxToken()
			return True
	elif token[2] == "(":
		print("----OK-(")
		token = proxToken()
		r = expressao()
		if r:
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

def buscaGlobal(lex):
	global tabelaglobal
	if tabelaglobal == []:
		return True
	for lista in tabelaglobal:
		if not lex in lista:
			pass
		else:
			return False
	return True

def buscaLocal(lex,proc):
	global tabelaglobal
	global indice
	for lista in tabelaglobal:
		if proc in lista:
			indice = tabelaglobal.index(lista)
			for l in lista[2]:
				if not lex in l:
					pass
				else:
					return False
	return True

def buscaGlobalr(lex):
	global tabelaglobal
	if tabelaglobal == []:
		return True
	for lista in tabelaglobal:
		if not lex in lista:
			pass
		else:
			return lista[2]
	return True

def buscaLocalr(lex,proc):
	global tabelaglobal
	global indice
	for lista in tabelaglobal:
		if proc in lista:
			indice = tabelaglobal.index(lista)
			for l in lista[2]:
				if not lex in l:
					pass
				else:
					return l[2]
	return True

def buscaEscopo():
	global procedimento
	global token
	if procedimento:
		if not buscaLocal(token[2],nomep):
			print("----OK-variavel-esta-no-escopo-local")
			return True
		elif not buscaGlobal(token[2]):
			print("----OK-variavel-esta-no-escopo-global")
			return True
		else:
			print("----Erro-variavel-em-escopo-errado-ou-nao-declarada")
			return False
	else:
		if not buscaGlobal(token[2]):
			print("----OK-variavel-esta-no-escopo-global")
			return True
		else:
			print("----Erro-variavel-em-escopo-errado-ou-nao-declarada")
			return False

def buscaEscopor():
	global procedimento
	global token
	if procedimento:
		if buscaLocalr(token[2],nomep):
			return buscaLocalr(token[2],nomep)
		elif buscaGlobalr(token[2]):
			return buscaGlobalr(token[2])
	else:
		if buscaGlobalr(token[2]):
			return buscaGlobalr(token[2])

def insereTabela(listaux,cat,tipo):
	global tabelaglobal
	global indice
	global nomep
	if procedimento:
		if buscaGlobal(nomep):
			tabelaglobal.append([nomep,"procedimento",[]])
			for lex in listaux:
				if buscaLocal(lex,nomep):
					tabelaglobal[indice][2].append([lex,cat,tipo])
				else:
					print("----Erro-variavel-já-declarada")
					print(lex)
					return False
			return True
		else:
			for lex in listaux:
				if buscaLocal(lex,nomep):
					tabelaglobal[indice][2].append([lex,cat,tipo])
				else:
					print("----Erro-variavel-já-declarada")
					print(lex)
					return False
			return True
	else:
		for lex in listaux:
			if buscaGlobal(lex):
				tabelaglobal.append([lex,cat,tipo])
			else:
				print("----Erro-variavel-já-declarada")
				print(lex)
				return False
		return True

token = proxToken()
tabelaglobal = []
tabelalocal = []
parametro = False
procedimento = False
read = False
exp = False
nomep = ""
listaux = []
S()
print(tabelaglobal)