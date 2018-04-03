#!/usr/bin/python3

import sys
import ply.lex as lex
import ply.yacc as yacc
import util

# counts for static,pointer and assignemnt statements
count_static=0
count_pointer=0
count_assign=0

node_list = []

tokens = (
		'NAME',
		'MAIN',
		'NUMBER',
		'INT',
		'NEWLINE',
		'VOID',
		'COMMA',
		'PLUS',
		'MINUS',
		'DIVIDE',
		'SEMICOLON',
		'PERCENTAGE',
		'LPAREN',
		'RPAREN',
		'EQUALS',
		'LTHAN',
		'GTHAN',
		'LBRACE',
		'RBRACE',
		'UMINUS',
		'EXCLAIM',
		'IF',
		'IFX',
		'ELSE',
		'WHILE',
		# 'LBRACKET',
		# 'RBRACKET',
		'ASTERISK',
		'AMPERSAND',
)

allotted_words = {
	'name' : 'NAME',
	'number' : 'NUMBER',
	'int' : 'INT',
	'void' : 'VOID'
}

t_ASTERISK = r'\*'
t_NUMBER = r'[0-9]+'
t_AMPERSAND = r'&'
t_LTHAN = r'<'
t_EXCLAIM = r'!'
t_GTHAN = r'>'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_COMMA = r','
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIVIDE = r'/'
t_LBRACE = r'{'
t_RBRACE = r'}'
t_SEMICOLON = r';'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQUALS = r'='
t_PERCENTAGE = r'%'
# t_LBRACKET = r'\['
# t_RBRACKET = r'\]'

lineno = 1

def t_IF(t):
	r'if | IF'
	t.value = 'if'
	return t

def t_ELSE(t):
	r'else | ELSE'
	t.value = 'else'
	return t

def t_WHILE(t):
	r'while | WHILE'
	t.value = 'while'
	return t

def t_NEWLINE(t):
	r'\n'
	global lineno
	lineno+=1
#    return t

t_ignore = " \t"

def t_MAIN(t):
	r'MAIN | main'
	t.value = 'main'
	return t

def t_VOID(t):
	r'VOID | void'
	t.value = 'void'
	return t

def t_INT(t):
	r'INT | int'
	t.value = 'int'
	return t

def t_error(t):
	print "Line %d." % (t.lineno,) + "",
	if t.value[0] == '"':
		print "Unterminated string literal."
		if t.value.count('\n') > 0:
			t.skip(t.value.index('\n'))
	elif t.value[0:2] == '/*':
		print "Unterminated comment."
	else:
		print "Illegal character '%s'" % t.value[0]
		t.skip(1)

precedence = (
		('left','PLUS','MINUS'),
		('left','ASTERISK','DIVIDE'),
		('right', 'UMINUS'),
		('nonassoc','IFX'),
		('nonassoc','ELSE'),   
)


def p_cprog(p):
	'''
	cprog : VOID MAIN arguments main_body
	'''
	global node_list
	for i in node_list:
		i.printTree(0)
		print ""
		

def p_arguments(p):
	'''
	arguments : LPAREN params RPAREN
			  | LPAREN RPAREN
	'''
	# print "jennie is in arguments"

def p_params(p):
	'''
	params : NAME varlist 
	'''
	# print "jennie is in params"


def p_main_body(p):
	'''
	main_body : LBRACE stmt_list RBRACE
	'''
	# print "jennie is in main_body"

def p_stmt_list(p):
	'''
	stmt_list : stmt stmt_list
			  | stmt
	'''
	# print "jennie is in stmt_list"

def p_decl_stmt(p):
	'''
	stmt : type varlist SEMICOLON
	'''
	# print "jennie in decl_stmt"

# assignlist -> assign comma assignlist semicolon | assign semicolon
# assign -> starname equals number | starname equals starname | name equals name | name equals andname

def p_stmt(p):
	'''
	stmt : assignlist SEMICOLON
	'''

def p_select_stmt(p):
	'''
	stmt : selection_stmt
	'''

def p_iterate_stmt(p):
	''' 
	stmt : iteration_stmt 
	'''
	
def p_assignlist(p):
	'''
	assignlist : assignstmt COMMA assignlist 
				| assignstmt
	'''

def p_assignstmt(p):
	'''
	assignstmt : starname EQUALS expression
				| name EQUALS expression
	'''
	node = util.Node()
	node.value = "ASGN"
	node.addChild(p[1])
	node.addChild(p[3])
	global count_assign
	count_assign+=1
	global node_list
	node_list.append(node)
	p[0]=node


def p_expression(p):
	'''
	expression : expression PLUS expression
				| expression MINUS expression
				| expression DIVIDE expression
				| expression ASTERISK expression
				| expression PERCENTAGE expression
	'''
	node = util.Node()
	if p[2] == '*':
		node.value = "MUL"
		node.addChild(p[1])
		node.addChild(p[3])
	if p[2] == '+':
		node.value = "PLUS"
		node.addChild(p[1])
		node.addChild(p[3])
	if p[2] == '/':
		node.value = "DIV"
		node.addChild(p[1])
		node.addChild(p[3])
	if p[2] == '-':
		node.value = "MINUS"
		node.addChild(p[1])
		node.addChild(p[3])
	p[0]=node


def p_term_expression(p):
	'''
	expression : starname
				| andname
				| name
				| number
	'''
	p[0]=p[1]

def p_paren_expression(p):
	'''
	expression : LPAREN expression RPAREN
	'''
	p[0]=p[2]

def p_type(p):
	'''
	type : INT
	'''
	# print "jennie is in p_type"

def p_starname(p):
	'''
	starname : ASTERISK name
	'''
	node = util.Node()
	node.value = "DEREF"
	node.addChild(p[2])
	p[0] = node

def p_andname(p):
	'''
	andname : AMPERSAND name
	'''
	node = util.Node()
	node.value = "ADDR"
	node.addChild(p[2])
	p[0] = node

def p_num(p):
	'''
	number : NUMBER
	'''
	node = util.Node()
	node.value = "CONST("+str(p[1])+")"
	p[0]=node
 
def p_name(p):
	'''
	name : NAME
	'''
	node = util.Node()
	node.value = "VAR("+p[1]+")"
	p[0]=node

# varlist-> var COMMA varlist | var
# var -> name | starname

def p_var(p):
	'''
	var : NAME
	'''
	global count_static
	count_static+=1

def p_var1(p):
	'''
	var1 : starname
	'''
	global count_pointer
	count_pointer+=1

def p_var2(p):
	'''
	var1 : ASTERISK var1
	'''

def p_varlist(p):
	'''
	varlist : var COMMA varlist
			| var1 COMMA varlist
			| var
			| var1
	'''
	# print "jennie is in varlist"

def p_uminus(p):
	'''
	expression : MINUS expression %prec UMINUS
	'''
	node = util.Node()
	node.value = "UMINUS"
	node.addChild(p[2])
	p[0] = node

# selection-stmt -> if lparen cond_expr rparen stmt ;
# cond_expr -> logical-or-expr
# logical-or-expr -> logical-and-expr | logical-or || logical-and
# logical-and-expr -> inclusive-or | logical-and && inclusive-or


def p_iteration_stmt(p):
	'''
	iteration_stmt : WHILE LPAREN condition_expression RPAREN brace_stmt
	'''

def p_brace_stmt(p):
	'''
	brace_stmt : stmt
				| LBRACE stmt_list RBRACE
	'''

def p_selection_stmt(p):
	'''
	selection_stmt : IF LPAREN condition_expression RPAREN brace_stmt %prec IFX
					| IF LPAREN condition_expression RPAREN brace_stmt ELSE brace_stmt
	'''

def p_condition_expression(p):
	'''
	condition_expression : assign_expr
	'''

def p_assign_expr(p):
	'''
	assign_expr : cond_expr
	'''

def p_cond_expr(p):
	'''
	cond_expr : log_or_expr
	'''

def p_log_or_expr(p):
	'''
	log_or_expr : log_and_expr
	'''

def p_log_and_expr(p):
	'''
	log_and_expr : incl_or_expr
				 | log_and_expr AMPERSAND AMPERSAND incl_or_expr
				 | log_and_expr EQUALS EQUALS incl_or_expr
	'''

def p_incl_or_expr(p):
	'''
	incl_or_expr : excl_or_expr
	'''

def p_excl_or_expr(p):
	'''
	excl_or_expr : and_expr
	'''

def p_and_expr(p):
	'''
	and_expr : eq_expr
	'''

def p_eq_expr(p):
	'''
	eq_expr : rel_expr
	'''

def p_rel_expr(p):
	'''
	rel_expr : shift_expr
			 | rel_expr EXCLAIM EQUALS shift_expr
			 | rel_expr LTHAN shift_expr
			 | rel_expr GTHAN shift_expr
			 | rel_expr lthanequal shift_expr
			 | rel_expr gthanequal shift_expr
	'''

def p_lthanequal(p):
	'''
	lthanequal : LTHAN EQUALS
	'''

def p_gthanequal(p):
	'''
	gthanequal : GTHAN EQUALS
	'''

def p_shift_expr(p):
	'''
	shift_expr : additive_expr
	'''

def p_additive_expr(p):
	'''
	additive_expr : multiplicative_expr
				  | additive_expr PLUS multiplicative_expr
				  | additive_expr MINUS multiplicative_expr
	'''

def p_multiplicative_expr(p):
	'''
	multiplicative_expr : cast_expr
	'''

def p_cast_expr(p):
	'''
	cast_expr : expression
	'''

# http://www.lysator.liu.se/c/ANSI-C-grammar-y.html

def p_error(t):
	# print "You've got a syntax error somewhere in your code."
	# print "It could be around line %d." % t.lineno
	# print "Good luck finding it."
	# raise ParseError()
	if t:
		print("syntax error at lineno {1} at {0}".format(t.value,lineno))
	else:
		print("syntax error at EOF")

def call_lex():
	file = open(sys.argv[1])
	lines = file.readlines()
	file.close()
	strings = ""
	for i in lines:
		strings += i
	lex.input(strings)
	# while 1:
	#     token = lex.token()       # Get a token
	#     if not token: break        # No more tokens
	#     print "(%s,'%s',%d, %d)" % (token.type, token.value, token.lineno, token.lexpos)
	yacc.yacc()
	yacc.parse(strings)
	global count_assign
	global count_pointer
	global count_static
#    print count_static
#    print count_pointer
#    print count_assign


lex.lex()

if __name__ == '__main__':
	call_lex()
