
#Execute the compiler as python 150050076-150050096.py <cfilename>.c



import sys
import ply.lex as lex
import ply.yacc as yacc


class Tree:
	def __init__(self):
		self.childlist = None
		self.data = None
		self.code = None

class TreeVdec:
	def __init__(self):
		self.name = None
		self.scope = None
		self.type = None
		self.dertype = None

class TreeFdec:
	def __init__(self):
		self.name = None
		self.returntype = None
		self.param = None

class cfgTree:
	def __init__(self):
		self.childlist = []
		self.type = None
		self.strValue = ""
		self.isTerminal = True

root = []
final = ""
loop = 0
cfgstr = ""
tcounter = -1
bb_counter = 1
def getnextt():
	global tcounter
	tcounter += 1
	return "t"+ str(tcounter)

def getnextbb():
	global bb_counter
	bb_counter += 1
	return "<bb "+str(bb_counter)+">\n"

def getcurrentbb():
	global bb_counter
	return "<bb "+str(bb_counter)+">\n"

def ast(roottree):

	global final
	# print roottree.childlist
	for child in roottree.childlist :
		final += print_ast(child)
		final += "\n"



def print_ast(tree):
	strret = ""
	if tree.data == "function_content_list" :
		for child in tree.childlist:
			strret += print_ast(child)
		return strret
	strret += tree.data 

	# if tree.data == "IF" or tree.data == "WHILE":

	# 	strret += "\n(\n"
	# 	for child in tree.childlist:
	# 		strret += "\t"+"\t".join(print_ast(child).splitlines(True))
	# 	strret += ")\n"
	# 	return strret
	if len(tree.childlist)>0:
		l = len(tree.childlist)
		strret += "\n(\n"
		for c in tree.childlist:
			strret += "\t"+"\t".join(print_ast(c).splitlines(True))
			if l>1:
				strret += "\t,\n"
				l-=1

		strret += ")\n"
	else:
		strret += "\n"
	return strret

def cfgmain(root):
	if len(root.childlist) ==0:
		return None
	cfgroot = cfg(root)
	lastchild = cfgTree()
	lastchild.type = "END"
	lastchild.strValue = getnextbb()
	lastchild.strValue += "END\n"
	gotoCFG(cfgroot,getcurrentbb())
	cfgroot.childlist.append(lastchild)
	return cfgroot

def cfg(root):
	i = 1
	childlen = len(root.childlist)
	cfgroot = cfgTree()
	cfgroot.type = "list"
	cfgroot.childlist = []
	currentchild = cfgTree()
	currentchild.strValue = getcurrentbb()
	currentchild.childlist = []
	currentchild.type = root.childlist[0].data
	for child in root.childlist:
		if child.data =="IF" :
			currentchild.strValue += cfgasgn(child.childlist[0])
			currentchild.strValue += "if("+child.childlist[0].code+") goto "+getnextbb()
			currentchild.childlist.append(cfg(child.childlist[1]))
			if len(child.childlist) == 3:
				currentchild.strValue += "else goto "+getnextbb()
				currentchild.childlist.append(cfg(child.childlist[2]))

			if i<childlen:
				bb = getnextbb()
				gotoCFG(currentchild,bb)
				# currentchild.strValue += "goto "+bb
				cfgroot.childlist.append(currentchild)
				currentchild = cfgTree()
				currentchild.type = root.childlist[i].data
				currentchild.strValue = bb

			else:
				cfgroot.childlist.append(currentchild)

			 	
			
		elif child.data =="WHILE":
			bb = getcurrentbb()
			currentchild.strValue += cfgasgn(child.childlist[0])
			currentchild.strValue += "if("+child.childlist[0].code+") goto "+getnextbb()
			currentchild.childlist.append(cfg(child.childlist[1]))
			gotoCFG(currentchild.childlist[0],bb)
			

			if i<childlen:
				bb = getnextbb()
				gotoCFG(currentchild,bb)
				# currentchild.strValue += "goto "+bb
				cfgroot.childlist.append(currentchild)
				currentchild = cfgTree()
				currentchild.type = root.childlist[i].data
				currentchild.strValue = bb

			else:
				cfgroot.childlist.append(currentchild)

		elif child.data =="ASGN":
			rightStr = cfgasgn(child.childlist[1])
			currentchild.strValue += rightStr
			cfgasgn(child.childlist[0])
			currentchild.strValue +=  child.childlist[0].code+" = "+ child.childlist[1].code +"\n"

			if i<childlen:
				if root.childlist[i].data =="IF" or root.childlist[i].data =="WHILE":
					bb = getnextbb()
					currentchild.strValue += "goto "+bb
					cfgroot.childlist.append(currentchild)
					currentchild = cfgTree()
					currentchild.type = root.childlist[i].data
					currentchild.strValue = bb
			else:
				cfgroot.childlist.append(currentchild)


		i += 1
	return cfgroot



def cfgasgn(root):
	childlen = len(root.childlist)
	if childlen ==2:
		
		left = cfgasgn(root.childlist[0])
		right = cfgasgn(root.childlist[1])
		t = getnextt()
		result = ""
		result += left
		result += right
		result += t + " = " +root.childlist[0].code +" "+ root.code +" " + root.childlist[1].code +"\n"
		root.code = t
		return result

	if childlen == 1:
		if root.code == "*" or root.code == "&" :
			cfgasgn(root.childlist[0])
			root.code = root.code + root.childlist[0].code
			return ""

		childresult = cfgasgn(root.childlist[0])
		result = ""
		result += childresult
		t = getnextt()
		result += t + " = " + root.code + root.childlist[0].code +"\n"
		root.code = t
		return result

	if childlen == 0:
		return ""

def gotoCFG(root , bb):
	if root.type =="IF":
		if len(root.childlist) ==2:
			gotoCFG(root.childlist[0],bb)
			gotoCFG(root.childlist[1],bb)
		else:
			root.strValue += "else goto "+bb
			gotoCFG(root.childlist[0],bb)

	elif root.type =="list":
		l = len(root.childlist)
		gotoCFG(root.childlist[l-1],bb)
	elif root.type =="ASGN":
		root.strValue += "goto " + bb
	elif root.type =="WHILE":
		root.strValue += "else goto "+bb




def cfgprint(root):
	if root == None:
		return ""
	result = ""
	if len(root.childlist) == 0:
		return root.strValue +"\n"
		
	if root.type != "list":
		result += root.strValue +"\n"
	for child in root.childlist:
		result += cfgprint(child)
	return result

def symbolprintv(var_dec):
	stri = "Variable Table :- \n"
	stri += "----------------------------------------------------------------\n"
	stri += "Name \t | Scope \t | Base Type | Derived Type \n"
	for a in var_dec:
		stri +=  a.name + " \t | "+a.scope+ "\t |  "  + a.type + "\t | " + a.dertype + "\n" 
		# print a.type

	return stri

def symbolprintf(func_dec):
	stri = "Procedure Table :-\n"
	stri += "----------------------------------------------------------------\n"
	stri += "Name \t | Return Type \t | Parameter list \n"
	for a in func_dec:
		stri +=  a.name + "\t | "+a.returntype+ "\t \t | "
		for b in a.param:
			stri += b.type + " " + b.dertype + b.name + " ,"
		stri += "\n"
		# print a.type

	return stri


listtrees = []

stat = 0
point = 0
assign = 0
err=0

var_dec = []
func_dec = []

point_var = {}
stat_var = {}

tokens = (
	'NAME',
	'NUMBER',
	'RPAREN',
	'LPAREN',
	'RBRACE',
	'LBRACE',
	'COMMA',
	'EQUAL',
	'INT',
	'FLOAT',
	'VOID',
	'MAIN',
	'ASTERISK',
	'SEMICOLON',
	'AMPERSAND',
	'PLUS',
	'MINUS',
	'DIVIDE',
	'WHILE',
	'IF',
	'EQUALS',
	'NOTEQUAL',
	'GREATER',
	'LESSER',
	'ELSE',
	'LOGOR',
	'LOGAND',
	'GREATEREQ',
	'LESSEREQ',
	'RETURN',
	'NUMBER2'
)

t_ignore = " \t\n"

t_RPAREN = r'\)'
t_LPAREN = r'\('
t_RBRACE = r'\}'
t_LBRACE = r'\{'
t_ASTERISK = r'\*'
t_SEMICOLON = r'\;'
t_AMPERSAND = r'\&'
t_LOGAND = r'\&\&'
t_LOGOR = r'\|\|'
t_EQUAL = r'='
t_COMMA = r','
t_NUMBER2 = r'\d+\.\d+'
t_NUMBER = r'\d+'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_EQUALS = r'=='
t_NOTEQUAL = r'!='
t_GREATER = r'>'
t_LESSER = r'<'
t_LESSEREQ = r'<='
t_GREATEREQ = r'>='




def t_NAME(p):
	r'[a-zA-Z_][a-zA-Z0-9_]*'

	if p.value == "if" or p.value == "IF":
		p.type = 'IF'

	elif p.value == "else" or p.value == "ELSE":
		p.type = 'ELSE'

	elif p.value == "main" or p.value == "MAIN":
		p.type = 'MAIN'

	elif p.value == "int" or p.value == "INT":
		p.type = 'INT'

	elif p.value == "void" or p.value == "VOID":
		p.type = 'VOID'

	elif p.value == "WHILE" or p.value == "while":
		p.type = 'WHILE'

	elif p.value == "float" or p.value == "FLOAT":
		p.type = 'FLOAT'

	elif p.value == "return" or p.value == "RETURN":
		p.type = 'RETURN'

	else:
		p.type = 'NAME'
	
	return p

# def t_NUMBER(t):
# 	r'\d+'
# 	try:
# 		t.value = int(t.value)
# 	except ValueError:
# 		print("Integer value too large %d", t.value)
# 		t.value = 0
# 	return t

# def t_NUMBER2(t):
# 	r'[0-9]+\.[0-9]+'
# 	return t

def t_error(t):
	print("error")
	t.lexer.skip(1)


# Parsing rules
precedence = (
		('left','PLUS','MINUS'),
		('left','ASTERISK','DIVIDE'),
		('right', 'UMINUS'),
		('nonassoc','IFX'),
		('nonassoc','ELSE'),
		('left','LOGOR'),
		('left','LOGAND'),
		# ('left','EQUALS','NOTEQUAL'),
		# ('left','LESSER','LESSEREQ','GREATER','GREATEREQ'),
)

# def p_epsilon(p):
# 	'''epsilon : '''
# 	pass


def p_final_prog(p):
	'''
	final_program : program_content
	'''


def p_program_content(p):
	'''
	program_content :  function_dec program_content
					| function_body program_content 
					| program program_content
	'''
	# needs some editing yet

def p_program_content2(p):
	'''
	program_content : function_dec 
					| function_body  
					| program 
	'''

	# needs some editing yet

def p_program_content3(p):
	'''
	program_content : declaration
	'''
	empty = []
	for a in p[1]:
		a.scope = "Global"
		empty.append(a)
	p[1] = empty
	global var_dec
	var_dec += p[1]

def p_program_content4(p):
	'''
	program_content : declaration program_content
	'''

	empty = []
	for a in p[1]:
		a.scope = "Global"
		empty.append(a)
	p[1] = empty
	global var_dec
	var_dec += p[1]

def p_function_dec(p):
	'''
	function_dec : datatype pointer LPAREN arguments RPAREN SEMICOLON
				| VOID namevar LPAREN arguments RPAREN SEMICOLON
	'''
	global func_dec
	p[0] = TreeFdec()
	p[0].name = p[2].name
	p[0].returntype = p[1]
	p[0].param = p[4]
	func_dec.append(p[0])

def p_function_dec2(p):
	'''
	function_dec : datatype pointer LPAREN  RPAREN SEMICOLON
			| VOID namevar LPAREN  RPAREN SEMICOLON
	'''
	global func_dec
	p[0] = TreeFdec()
	p[0].name = p[2].name
	p[0].returntype = p[1]
	p[0].param = []
	func_dec.append(p[0])

	# print 'without arg'

def p_arguments(p):
	'''
	arguments : datatype pointer
				| datatype namevar
	'''
	p[2].type = p[1]
	p[0] = [p[2]]

def p_arguments2(p):
	'''
	arguments : datatype pointer COMMA arguments 
				| datatype namevar COMMA arguments
	'''
	p[2].type = p[1]
	p[0] = p[4] 
	p[0].append(p[2])

def p_function_body(p):
	'''
	function_body : datatype pointer LPAREN arguments RPAREN LBRACE function_content return_stat RBRACE 
				|  VOID namevar LPAREN arguments RPAREN LBRACE function_content return_stat RBRACE
	'''
	global root
	temp = Tree()
	temp.childlist = []
	
	empty = []
	for a in p[7][1]:
		a.scope = p[2].name
		empty.append(a)
	p[7][1] = empty	

	global var_dec
	var_dec += p[7][1]

	temp.childlist = p[7]
	temp.data = p[2].name
	p[0] = temp
	
	root.append(p[0])

def p_function_body2(p):
	'''
	function_body : datatype pointer LPAREN  RPAREN LBRACE function_content return_stat RBRACE
				| VOID namevar LPAREN  RPAREN LBRACE function_content return_stat RBRACE 
	'''
	global root
	temp = Tree()
	temp.childlist = []
	
	empty = []
	for a in p[6][1]:
		a.scope = p[2].name
		empty.append(a)
	p[6][1] = empty	


	global var_dec
	var_dec += p[6][1]
	

	temp.childlist = p[6]
	temp.data = p[2].name
	p[0] = temp
	
	root.append(p[0])

def p_return(p):
	'''
	return_stat : RETURN pointer SEMICOLON
				| RETURN NAME SEMICOLON
				| RETURN SEMICOLON
	'''

def p_func_call(p):
	'''
	function_call : NAME LPAREN varlist RPAREN SEMICOLON
					| NAME LPAREN RPAREN SEMICOLON

	'''


def p_program(p):
	'''
	program : VOID MAIN LPAREN RPAREN LBRACE function_content RBRACE
	'''
	# print(p[6])
	global root
	temp = Tree()
	global cfgstr
	temp.childlist = []
	
	temp.data = "Main"
	# print(root)

	empty = []
	for a in p[6][1]:
		a.scope = "Main"
		empty.append(a)
	p[6][1] = empty	

	# print empty

	global var_dec
	var_dec += p[6][1]

	temp.childlist = p[6]
	p[0] = temp
	
	root.append(p[0])

	# ast(root)
	# cfgroot = cfgmain(root)
	# cfgstr = cfgprint(cfgroot)

def p_function_content(p):
	'''
	function_content :  assignment_statement
				| while_stat
				| if_stat
				| function_call
	'''
	if p[0]==None:
		p[0] = [[],[]]
	
	p[0][0] = [p[1]]
	

def p_function_content2(p):
	'''
	function_content : assignment_statement function_content
					| while_stat function_content
					| if_stat function_content
					| function_call function_content
	'''
	if p[0]==None:

		p[0] = [[],[]]
	
	p[0][0].append(p[1])
	p[0][0] += p[2][0]
	p[0][1] += p[2][1]

def p_function_content3(p):
	'''
	function_content : declaration
	'''
	if p[0]==None:
		p[0] = [[],[]]

	p[0][1] += p[1]
	# global var_dec
	# var_dec += p[1]


def p_function_content4(p):
	'''
	function_content :  declaration function_content
	'''
	if p[0]==None:
		p[0] = [[],[]]

	p[0][1] += p[1]
	p[0][0] += p[2][0]
	p[0][1] += p[2][1]
	# global var_dec
	# var_dec += p[1]

def p_declaration(p):
	'''
	declaration : datatype varlist SEMICOLON
	'''
	emptylist = []
	for a in p[2]:
		# print a
		# print "yes it does"
		a.type = p[1]
		# print p[1]
		emptylist.append(a)

	p[2] = emptylist
	p[0] = p[2] 
	

def p_datatype(p):
	'''
	datatype : INT
			 | FLOAT
			 | VOID
	'''
	p[0] = p[1]

def p_namevar(p):
	'''
	namevar : NAME
	'''
	p[0] = TreeVdec()
	p[0].name = p[1]
	p[0].dertype = ""

def p_varlist1(p):
	'''varlist : namevar COMMA varlist
				| pointer COMMA varlist
	'''
	p[0]=[]
	
	p[0].append(p[1])
	p[0]+=p[3]
	
def p_varlist2(p):
	'''varlist : namevar
				| pointer
	'''
	p[0] = []
	p[0].append(p[1])


def p_pointer(p):
	'''
	pointer : ASTERISK pointer
			| ASTERISK namevar
	'''
	p[0] = p[2]
	p[0].dertype += "*"
	

def p_assignment_statement(p):
	'''assignment_statement : ID EQUAL RIGHT SEMICOLON
							| LEFT EQUAL expression SEMICOLON
							| ID EQUAL function_call 
							| LEFT EQUAL function_call 
	'''
	p[0] = Tree()
	p[0].data = "ASGN"
	p[0].code = "="
	p[0].childlist = []
	p[0].childlist.append(p[1])
	p[0].childlist.append(p[3])
	

def p_id(p):
	'''ID : NAME'''
	p[0] = Tree()
	p[0].code = p[1]
	p[0].childlist = []
	p[0].data = "VAR("+p[1]+")"
	# p[0].code = "VAR("+p[1]+")"

def p_left(p):
	'''LEFT : ASTERISK var'''
	p[0] = Tree()
	p[0].data = "DEREF"
	p[0].code = p[1]
	p[0].childlist = []
	p[0].childlist.append(p[2])

def p_right(p):
	'''RIGHT : AMPERSAND var'''
	p[0] = Tree()
	p[0].data = "ADDR"
	p[0].code = p[1]
	p[0].childlist = []
	p[0].childlist.append(p[2])


def p_expression(p):
	'''
	expression : expression PLUS expression
				| expression MINUS expression
				| expression ASTERISK expression
				| expression DIVIDE expression
	'''
	if p[2]=="+":
		# p[0] = "PLUS\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"
		p[0]=Tree()
		p[0].data = "PLUS"
		p[0].childlist = []
		p[0].childlist.append(p[1])
		p[0].childlist.append(p[3])
		# p[0].code = "PLUS\n(\n\t"+"\t".join(p[1].code.splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].code.splitlines(True))+"\n)" 

	elif p[2] == "-":
		# p[0] = "MINUS\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"
		p[0]=Tree()
		p[0].data = "MINUS"
		p[0].childlist = []
		p[0].childlist.append(p[1])
		p[0].childlist.append(p[3])
		# p[0].code = "MINUS\n(\n\t"+"\t".join(p[1].code.splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].code.splitlines(True))+"\n)"
	elif p[2] == "*":
		# p[0] = "MUL\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"
		p[0]=Tree()
		p[0].data = "MUL"
		p[0].childlist = []
		p[0].childlist.append(p[1])
		p[0].childlist.append(p[3])
		# p[0].code = "MUL\n(\n\t"+"\t".join(p[1].code.splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].code.splitlines(True))+"\n)"
	else:
		# p[0] = "DIV\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"
		p[0]=Tree()
		p[0].data = "DIV"
		p[0].childlist = []
		p[0].childlist.append(p[1])
		p[0].childlist.append(p[3])
		# p[0].code = "DIV\n(\n\t"+"\t".join(p[1].code.splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].code.splitlines(True))+"\n)"

	p[0].code = p[2]
		

	

def p_expression2(p):
	'''
	expression : var
			| NUMBERvar
	'''
	p[0] = p[1]


def p_expression3(p):
	'''
	expression :  LPAREN expression RPAREN
	'''
	p[0] = p[2]

def p_numvar(p):
	'''
	NUMBERvar : NUMBER
	'''
	p[0] = Tree()
	p[0].data = "CONST("+str(p[1])+")"
	p[0].childlist = []
	p[0].code = str(p[1])
	# p[0].code = "CONST("+str(p[1])+")"

def p_numvar2(p):
	'''
	NUMBERvar : NUMBER2
	'''
	p[0] = Tree()
	p[0].data = "CONST("+str(p[1])+")"
	p[0].childlist = []
	p[0].code = str(p[1])
	# p[0].code = "CONST("+str(p[1])+")"

def p_var(p):
	'''
	var : ASTERISK var
		| AMPERSAND var
		| NAME

	'''
	if p[1] == "*":
		p[0] = Tree()
		p[0].data = "DEREF"
		p[0].code = p[1]
		p[0].childlist = []
		p[0].childlist.append(p[2])
	elif p[1] == "&":
		p[0] = Tree()
		# p[0].data = "ADDR\n(\n\t"+"\t".join(p[2].data)+"\n)"
		p[0].data = "ADDR"
		p[0].code = p[1]
		p[0].childlist = []
		p[0].childlist.append(p[2])
		# p[0].code = "ADDR\n(\n\t"+"\t".join(p[2].code.splitlines(True))+"\n)"
	else:
		p[0] = Tree()
		p[0].data = "VAR("+p[1]+")"
		p[0].code = p[1]
		p[0].childlist = []
		# p[0].code = "VAR("+p[1]+")"
		


def p_expression_uminus(p):
	'expression : MINUS expression %prec UMINUS'
	p[0] = Tree()
	# p[0].data = "UMINUS\n(\n\t"+"\t".join(p[2].data)+"\n)"
	p[0].data = "UMINUS"
	p[0].code = "-"
	p[0].childlist = []
	p[0].childlist.append(p[2])
	# p[0].code = "UMINUS\n(\n\t"+"\t".join(p[2].code.splitlines(True))+"\n)"
	  

def p_code_block(p):
	'''
	code_block :  if_stat
				| while_stat
				| assignment_statement
	'''
	p[0] = Tree()
	p[0].data = "function_content_list"
	p[0].childlist = []
	p[0].childlist.append(p[1])

def p_code_block2(p):
	'code_block : LBRACE function_content RBRACE'
	p[0] = Tree()
	p[0].data = "function_content_list"
	p[0].childlist = p[2]

def p_while(p):
	'while_stat : WHILE LPAREN b_expression RPAREN code_block'
	p[0] = Tree()
	p[0].data = "WHILE"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist.append(p[5])
	# p[0].childlist.append(None)

def p_if1(p):
	'if_stat : IF LPAREN b_expression RPAREN code_block %prec IFX'
	p[0] = Tree()
	p[0].data = "IF"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist.append(p[5])
	# p[0].childlist.append(None)

def p_if2(p):
	'''
	if_stat : IF LPAREN b_expression RPAREN code_block ELSE code_block
	'''
	p[0] = Tree()
	p[0].data = "IF"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist.append(p[5])
	p[0].childlist.append(p[7])

def p_bool(p):
	'''
	b_expression : expression sign1 expression
	'''
	p[0] = Tree()
	if p[2] == ">":
		p[0].data = "GT"
	if p[2] == "<":
		p[0].data = "LT"
	if p[2] == "==":
		p[0].data = "EQ"
	if p[2] == "!=":
		p[0].data = "NE"
	if p[2] == ">=":
		p[0].data = "GE"
	if p[2] == "<=":
		p[0].data = "LE"
	p[0].code = p[2]
	p[0].childlist = []
	p[0].childlist.append(p[1])
	p[0].childlist.append(p[3])



def p_bool2(p):
	'''
	b_expression : b_expression sign2 b_expression 
	'''
	p[0] = Tree()

	if p[2] == "&&":
		p[0].data = "AND"
	if p[2] == "||":
		p[0].data = "OR"

	p[0].code = p[2]

	p[0].childlist = []
	p[0].childlist.append(p[1])
	p[0].childlist.append(p[3])

def p_bool_paren1(p):
	'b_expression : LPAREN b_expression RPAREN'

	p[0] = p[1]

def p_sign(p):
	'''
	sign1 : EQUALS
		|  NOTEQUAL
		|  GREATER
		|  LESSER
		|	GREATEREQ
		| LESSEREQ
	'''
	p[0] = p[1]
	# print p[1] , "ENCORE"

def p_sign1(p):
	'''
	sign2 : LOGOR
			| LOGAND
	'''
	p[0] = p[1]



def p_error(p):
	if p:
		print("syntax error at {0}".format(p.value))
	else:
		print("syntax error at EOF")	
	global err
	err=1




def process(data):
	lexer =lex.lex()
	yacc.yacc()
	yacc.parse(data)

if __name__ == "__main__":
	file_name = sys.argv[1]
	file = open(file_name)
	lines = file.readlines()
	data =""
	for line in lines:
		data += line

	process(data)
	if err==0:
	
		print 'Successfully Parsed'

		with open(file_name+".ast",'w') as f:
			print >> f , final

		with open(file_name+".cfg",'w') as f:
			print >> f , cfgstr

		symstr = symbolprintv(var_dec)
		symstr2 = symbolprintf(func_dec)
		with open(file_name+".sym",'w') as f:
			print >> f , symstr2 + "\n" + symstr


	# print(stat)
	# print(point)
	# print(assign)