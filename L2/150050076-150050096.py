
#Execute the compiler as python 150050076-150050096.py <cfilename>.c



import sys
import ply.lex as lex
import ply.yacc as yacc


stat = 0
point = 0
assign = 0
err=0

final = ""

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
	'DIVIDE'
	)

t_ignore = " \t\n"

t_RPAREN = r'\)'
t_LPAREN = r'\('
t_RBRACE = r'\}'
t_LBRACE = r'\{'
t_ASTERISK = r'\*'
t_SEMICOLON = r'\;'
t_AMPERSAND = r'\&'
t_EQUAL = r'='
t_COMMA = r','
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'


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

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_error(t):
	print("error "+t.value )
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





def p_function_content(p):
	'''
	function_content : declaration 
				| assignment_statement
				| declaration function_content
				| assignment_statement function_content
	'''

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
	p[0] = "ASGN\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"

	global final
	final += p[0] + "\n\n"

def p_id(p):
	'''ID : NAME'''
	p[0] = "VAR("+p[1]+")"

def p_left(p):
	'''LEFT : ASTERISK var'''
	p[0] = "DEREF\n(\n\t"+"\t".join(p[2].splitlines(True))+"\n)"

def p_expression(p):
	'''
	expression : expression PLUS expression
				| expression MINUS expression
				| expression ASTERISK expression
				| expression DIVIDE expression
	'''
	if p[2]=="+":
		p[0] = "PLUS\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"
	elif p[2] == "-":
		p[0] = "MINUS\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"
	elif p[2] == "*":
		p[0] = "MUL\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"
	else:
		p[0] = "DIV\n(\n\t"+"\t".join(p[1].splitlines(True))+"\n\t,\n\t"+"\t".join(p[3].splitlines(True))+"\n)"

	

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
	p[0] = "CONST("+str(p[1])+")"

def p_var(p):
	'''
	var : ASTERISK var
		| AMPERSAND var
		| NAME

	'''
	if p[1] == "*":
		p[0] = "DEREF\n(\n\t"+"\t".join(p[2].splitlines(True))+"\n)"
	elif p[1] == "&":
		p[0] = "ADDR\n(\n\t"+"\t".join(p[2].splitlines(True))+"\n)"
	else:
		p[0] = "VAR("+p[1]+")"
		


def p_expression_uminus(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = "UMINUS\n(\n\t"+"\t".join(p[2].splitlines(True))+"\n)"
      





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



