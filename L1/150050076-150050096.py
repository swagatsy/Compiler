
#Execute the compiler as python 150050076-150050096.py <cfilename>.c



import sys
import ply.lex as lex
import ply.yacc as yacc


stat = 0
point = 0
assign = 0


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
	'PLUS'
	
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
	print("error")
	t.lexer.skip(1)


# Parsing rules
precedence = (
		('left', 'NAME'),
		
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
	'declaration : INT statlist SEMICOLON'
	global stat
	stat += 1

def p_declaration1(p):
	'declaration : INT pointerlist SEMICOLON'
	global point
	point += 1

def p_statlist(p):
	'''statlist : statvar COMMA statlist
	'''
	global stat
	stat += 1
	# stat++
def p_statlist1(p):
	'statlist : statvar'



def p_pointerlist(p):
	'pointerlist : pointer COMMA pointerlist'
	global point
	point += 1

def p_pointerlist1(p):
	'pointerlist : pointer'

def p_pointer(p):
	'''
	pointer : ASTERISK NAME
	'''
	# p[0]=p[2]

def p_statvar(p):
	'statvar : NAME'



def p_assignment_statement(p):
	'assignment_statement : assignmentlist SEMICOLON'

def p_assignmentlist(p):
	'''assignmentlist : singleAssignment COMMA assignmentlist
					| singleAssignment
	'''

def p_singleAssignment(p):
	'''singleAssignment : NAME EQUAL AMPERSAND NAME
						| NAME EQUAL pointer
						| NAME EQUAL NAME

	'''
	global assign
	assign += 1
def p_singleAssignment1(p):
	'''singleAssignment : pointer EQUAL NAME
					| pointer EQUAL AMPERSAND NAME
					| pointer EQUAL pointer
					| pointer EQUAL NUMBER
	'''
	global assign
	assign += 1


# def p_declaration_stat(p):
# 	'''
# 	staticdec : INT NAME SEMICOLON
# 	'''
# 	global stat
# 	stat += 1
# 	p[0] = p[1]+' '+p[2]+p[3]
# 	# print(p[0])


# def p_declaration_point(p):
# 	'''
# 	pointerdec : INT pointer SEMICOLON
# 	'''

# 	global point
# 	point += 1
# 	p[0] = p[1]+' '+p[2]+p[3]
# 	# print(p[2])


# def p_assign(p):
# 	'''
# 	assignment : NAME EQUAL NAME SEMICOLON
# 				| NAME EQUAL pointer SEMICOLON
# 	'''
# 	print('coming...')


def p_error(p):
	if p:
		print("syntax error at {0}".format(p.value))
	else:
		print("syntax error at EOF")	





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


	print(stat)
	print(point)
	print(assign)


