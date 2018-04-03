
#Execute the compiler as python 150050076-150050096.py <cfilename>.c



import sys
import ply.lex as lex
import ply.yacc as yacc


class Tree:
	def __init__(self):
		self.childlist = None
		self.data = None

root = Tree()
final = ""
loop = 0
def ast(roottree):

	global final
	# print roottree.childlist
	for child in roottree.childlist :
		final += print_ast(child)
		final += "\n"


def print_ast(tree):
	strret = ""
	strret += tree.data 
	if len(tree.childlist)>0:
		l = len(tree.childlist)
		strret += "\n(\n"
		for c in tree.childlist:
			strret += "\t"+"\t".join(print_ast(c).splitlines(True))
			if l>1:
				strret += "\t,\n"
				l-=1

		strret += "\n)\n"
	else:
		strret += "\n"
	return strret



listtrees = []

stat = 0
point = 0
assign = 0
err=0



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
	'LOGAND'
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
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_EQUALS = r'=='
t_NOTEQUAL = r'!='
t_GREATER = r'>'
t_LESSER = r'<'




def t_MAIN(p):
	r'MAIN | main'
	p.value = 'main'
	return p

def t_VOID(p):
	r'VOID | void'
	p.value= 'void'
	return p

def t_INT(p):
	r'INT | int'
	p.value = 'int'
	return p

def t_WHILE(p):
	r'while | WHILE'
	return p

def t_IF(p):
	r'if | IF'
	p.value = 'IF'
	return p


def t_ELSE(p):
	r'else | ELSE'
	p.value = 'ELSE'
	return p 

def t_NUMBER(t):
	r'\d+'
	try:
		t.value = int(t.value)
	except ValueError:
		print("Integer value too large %d", t.value)
		t.value = 0
	return t

def t_error(t):
	print("error")
	t.lexer.skip(1)


# Parsing rules
precedence = (
		('left','PLUS','MINUS'),
		('left','ASTERISK','DIVIDE'),
		('right', 'UMINUS'),
		
)




def p_program(p):
	'''
	program : VOID MAIN LPAREN RPAREN LBRACE function_content RBRACE
	'''
	# print(p[6])

	global root
	root.childlist = []
	root.childlist = p[6]
	root.data = "Main"

	ast(root)

def p_function_content(p):
	'''
	function_content :  assignment_statement
				| while_stat
				| if_stat
	'''
	p[0] = [p[1]]

def p_function_content2(p):
	'''
	function_content : assignment_statement function_content
					| while_stat function_content
					| if_stat function_content
	'''
	p[0] = []
	p[0].append(p[1])
	p[0] += p[2]


def p_function_content3(p):
	'''
	function_content : declaration
	'''
	p[0] = []

def p_function_content4(p):
	'''
	function_content :  declaration function_content
	'''
	p[0] = []
	p[0] += p[2]

def p_declaration(p):
	'declaration : INT varlist SEMICOLON'
	# global stat
	# stat += 1

# def p_declaration1(p):
# 	'declaration : INT pointerlist SEMICOLON'
# 	global point
# 	point += 1

def p_statlist(p):
	'''varlist : NAME COMMA varlist
				| NAME
	'''
	global stat
	stat += 1

def p_pointerlist(p):
	'''varlist : pointer COMMA varlist
				| pointer
	'''
	global point
	point += 1

def p_pointer(p):
	'''
	pointer : ASTERISK pointer
			| ASTERISK NAME
	'''
	

def p_assignment_statement(p):
	'''assignment_statement : ID EQUAL expression SEMICOLON
							| LEFT EQUAL expression SEMICOLON
	'''
	# p[0] = "ASGN\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"
	p[0] = Tree()
	p[0].data = "ASGN"
	# p[0].left = p[1]
	# p[0].right = p[3]
	p[0].childlist = []
	p[0].childlist.append(p[1])
	p[0].childlist.append(p[3])
	# p[0].code = "ASGN\n(\n\t"+"\t".join(p[1].code.splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].code.splitlines(True))+"\n)"
	# global loop
	# if loop == 0:
	# 	global listtrees
	# 	listtrees.append(p[0])
	# global final
	# final += p[0] + "\n\n"

def p_id(p):
	'''ID : NAME'''
	# p[0] = "VAR("+p[1]+")"
	p[0] = Tree()
	p[0].childlist = []
	p[0].data = "VAR("+p[1]+")"
	# p[0].code = "VAR("+p[1]+")"

def p_left(p):
	'''LEFT : ASTERISK var'''
	# p[0] = "DEREF\n(\n\t"+"\t".join(p[2].splitlines(True))+"\n)"
	p[0] = Tree()
	p[0].data = "DEREF"
	p[0].childlist = []
	p[0].childlist.append(p[2])
	# p[0].code = "DEREF\n(\n\t"+"\t".join(p[2].code.splitlines(True))+"\n)"

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
	# p[0].code = "CONST("+str(p[1])+")"

def p_var(p):
	'''
	var : ASTERISK var
		| AMPERSAND var
		| NAME

	'''
	if p[1] == "*":
		p[0] = Tree()
		# p[0].data = "DEREF\n(\n\t"+"\t".join(p[2].data)+"\n)"
		p[0].data = "DEREF"
		p[0].childlist = []
		p[0].childlist.append(p[2])
		# p[0].code = "DEREF\n(\n\t"+"\t".join(p[2].code.splitlines(True))+"\n)"
	elif p[1] == "&":
		p[0] = Tree()
		# p[0].data = "ADDR\n(\n\t"+"\t".join(p[2].data)+"\n)"
		p[0].data = "ADDR"
		p[0].childlist = []
		p[0].childlist.append(p[2])
		# p[0].code = "ADDR\n(\n\t"+"\t".join(p[2].code.splitlines(True))+"\n)"
	else:
		p[0] = Tree()
		p[0].data = "VAR("+p[1]+")"
		p[0].childlist = []
		# p[0].code = "VAR("+p[1]+")"
		


def p_expression_uminus(p):
	'expression : MINUS expression %prec UMINUS'
	p[0] = Tree()
	# p[0].data = "UMINUS\n(\n\t"+"\t".join(p[2].data)+"\n)"
	p[0].data = "UMINUS"
	p[0].childlist = []
	p[0].childlist.append(p[2])
	# p[0].code = "UMINUS\n(\n\t"+"\t".join(p[2].code.splitlines(True))+"\n)"
	  


def p_while1(p):
	'while_stat : WHILE LPAREN b_expression RPAREN LBRACE function_content RBRACE'
	p[0] = Tree()
	p[0].data = "WHILE"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist += p[6]
	# p[0].childlist.append(None)

def p_while2(p):
	'while_stat : WHILE LPAREN b_expression RPAREN  assignment_statement '
	p[0] = Tree()
	p[0].data = "WHILE"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist.append(p[5])
	# p[0].childlist.append(None)


def p_if1(p):
	'''
	if_stat : IF LPAREN b_expression RPAREN LBRACE function_content RBRACE 
	'''
	p[0] = Tree()
	p[0].data = "IF"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist += p[6]
	# p[0].childlist.append(None)

def p_if12(p):
	'''
	if_stat : IF LPAREN b_expression RPAREN LBRACE function_content RBRACE elsepart
	'''
	p[0] = Tree()
	p[0].data = "IF"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist += p[6]
	if type(p[8]) == list:
		p[0].childlist += p[8]
	else:
		p[0].childlist.append(p[8])
	# print p[0].childlist , "Heeeee"



def p_if2(p):
	'''
	if_stat : IF LPAREN b_expression RPAREN  assignment_statement 
	'''
	p[0] = Tree()
	p[0].data = "IF"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist.append(p[5])
	# p[0].childlist.append(None)

def p_if22(p):
	'''
	if_stat : IF LPAREN b_expression RPAREN  assignment_statement elsepart
	'''
	p[0] = Tree()
	p[0].data = "IF"
	p[0].childlist = []
	p[0].childlist.append(p[3])
	p[0].childlist.append(p[5])
	if type(p[6]) == list:
		p[0].childlist += p[6]
	else:
		p[0].childlist.append(p[6])



def p_elsep2(p):
	'''
	elsepart :  elif 
			| else
	'''
	p[0] = p[1] 
	# p[1].childlist.append(p[2])

def p_elif(p):
	'''
	elif : ELSE if_stat
	'''
	p[0] = p[2]
	


def p_else(p):
	
	'''
	else : ELSE  assignment_statement 
	'''
	p[0] = p[2]
	# p[0].data = "ELSE"
	# p[0].childlist.append(p[2])

def p_else2(p):
	'''
	else :  ELSE LBRACE function_content RBRACE 
	'''
	p[0] = p[3]
	# p[0].data = "ELSE"
	# p[0].childlist.append(p[3])

def p_bool(p):
	'''
	b_expression : expression sign1 expression
	'''
	p[0] = Tree()
	p[0].data = p[2]
	p[0].childlist = []
	p[0].childlist.append(p[1])
	p[0].childlist.append(p[3])

def p_bool2(p):
	'''
	b_expression : b_expression sign2 b_expression 
	'''
	p[0] = Tree()
	p[0].data = p[2]
	p[0].childlist = []
	p[0].childlist.append(p[1])
	p[0].childlist.append(p[3])

def p_sign(p):
	'''
	sign1 : EQUALS
		|  NOTEQUAL
		|  GREATER
		|  LESSER
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
		with open("Parser_ast_"+file_name+".txt",'w') as f:
			print >> f , final

	# print(stat)
	# print(point)
	# print(assign)



