
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftASTERISKDIVIDErightUMINUSnonassocIFXnonassocELSEleftLOGORleftLOGANDNAME NUMBER RPAREN LPAREN RBRACE LBRACE COMMA EQUAL INT FLOAT VOID MAIN ASTERISK SEMICOLON AMPERSAND PLUS MINUS DIVIDE WHILE IF EQUALS NOTEQUAL GREATER LESSER ELSE LOGOR LOGAND GREATEREQ LESSEREQ RETURN NUMBER2\n\tfinal_program : program_content\n\t\n\tprogram_content :  function_dec program_content\n\t\t\t\t\t| function_body program_content \n\t\t\t\t\t| program program_content\n\t\n\tprogram_content : function_dec \n\t\t\t\t\t| function_body  \n\t\t\t\t\t| program \n\t\n\tprogram_content : declaration\n\t\n\tprogram_content : declaration program_content\n\t\n\tfunction_dec : datatype pointer LPAREN arguments RPAREN SEMICOLON\n\t\t\t\t| VOID namevar LPAREN arguments RPAREN SEMICOLON\n\t\n\targuments : datatype pointer\n\t\t\t\t| datatype namevar\n\t\n\targuments : datatype pointer COMMA arguments \n\t\t\t\t| datatype namevar COMMA arguments\n\t\n\targuments : epsilon\n\t\n\tfunction_body : datatype pointer LPAREN arguments RPAREN LBRACE function_content return_stat RBRACE \n\t\t\t\t|  VOID namevar LPAREN arguments RPAREN LBRACE function_content return_stat2 RBRACE\n\t\n\treturn_stat : RETURN LEFT SEMICOLON\n\t\t\t\t| RETURN ID SEMICOLON\n\t\n\treturn_stat2 : RETURN SEMICOLON\n\t\t\t\t| epsilon\n\t\n\tfunction_call : NAME LPAREN arglist RPAREN SEMICOLON\n\t\n\tfunction_call : NAME LPAREN RPAREN SEMICOLON\n\t\n\targlist : LEFT\n\t\t\t| ID\n\t\n\targlist : LEFT COMMA arglist\n\t\t\t| ID COMMA arglist\n\t\n\tprogram : VOID MAIN LPAREN RPAREN LBRACE function_content RBRACE\n\t\n\tfunction_content :  assignment_statement\n\t\t\t\t| while_stat\n\t\t\t\t| if_stat\n\t\t\t\t| function_call\n\t\n\tfunction_content : assignment_statement function_content\n\t\t\t\t\t| while_stat function_content\n\t\t\t\t\t| if_stat function_content\n\t\t\t\t\t| function_call function_content\n\t\n\tfunction_content : declaration\n\t\n\tfunction_content :  declaration function_content\n\t\n\tfunction_content : epsilon\n\t\n\tdeclaration : datatype varlist SEMICOLON\n\t\n\tdatatype : INT\n\t\t\t | FLOAT\n\t\n\tnamevar : NAME\n\tvarlist : namevar COMMA varlist\n\t\t\t\t| pointer COMMA varlist\n\tvarlist : namevar\n\t\t\t\t| pointer\n\t\n\tpointer : ASTERISK pointer\n\t\t\t| ASTERISK namevar\n\tassignment_statement : ID EQUAL RIGHT SEMICOLON\n\t\t\t\t\t\t\t| LEFT EQUAL expression SEMICOLON\n\t\t\t\t\t\t\t| ID EQUAL function_call \n\t\t\t\t\t\t\t| LEFT EQUAL function_call \n\tID : NAMELEFT : ASTERISK varRIGHT : AMPERSAND var\n\texpression : expression PLUS expression\n\t\t\t\t| expression MINUS expression\n\t\t\t\t| expression ASTERISK expression\n\t\t\t\t| expression DIVIDE expression\n\t\n\texpression : var\n\t\t\t| NUMBERvar\n\t\n\texpression :  LPAREN expression RPAREN\n\t\n\tNUMBERvar : NUMBER\n\t\n\tNUMBERvar : NUMBER2\n\t\n\tvar : ASTERISK var\n\t\t| AMPERSAND var\n\t\t| NAME\n\n\texpression : MINUS expression %prec UMINUS\n\tcode_block :  if_stat\n\t\t\t\t| while_stat\n\t\t\t\t| assignment_statement\n\tcode_block : LBRACE function_content RBRACEwhile_stat : WHILE LPAREN b_expression RPAREN code_blockif_stat : IF LPAREN b_expression RPAREN code_block %prec IFX\n\tif_stat : IF LPAREN b_expression RPAREN code_block ELSE code_block\n\t\n\tb_expression : expression sign1 expression\n\t\n\tb_expression : b_expression sign2 b_expression \n\tb_expression : LPAREN b_expression RPAREN\n\tsign1 : EQUALS\n\t\t|  NOTEQUAL\n\t\t|  GREATER\n\t\t|  LESSER\n\t\t|\tGREATEREQ\n\t\t| LESSEREQ\n\t\n\tsign2 : LOGOR\n\t\t\t| LOGAND\n\tepsilon : '
    
_lr_action_items = {'LOGOR':([75,90,91,93,94,95,102,103,108,121,134,151,152,153,154,155,156,157,158,],[-69,-65,117,-63,-62,-66,-68,-67,117,117,-70,117,-80,-64,-61,-60,-58,-78,-59,]),'NOTEQUAL':([75,90,93,94,95,96,102,103,122,134,153,154,155,156,158,],[-69,-65,-63,-62,-66,123,-68,-67,123,-70,-64,-61,-60,-58,-59,]),'RETURN':([27,45,48,50,51,53,55,59,61,65,67,69,70,76,80,81,99,106,113,136,137,143,147,148,149,150,159,164,165,],[-41,-89,-33,-30,-32,-40,-38,-31,-89,83,-37,-34,-36,-39,-35,110,-54,-53,-24,-52,-51,-23,-73,-71,-75,-72,-76,-74,-77,]),'VOID':([0,2,3,5,6,27,46,62,79,112,140,],[1,1,1,1,1,-41,-11,-10,-29,-18,-17,]),'EQUAL':([47,52,56,72,75,86,102,103,],[-55,71,77,-56,-69,-55,-68,-67,]),'WHILE':([27,41,45,48,50,51,55,59,61,99,106,113,118,136,137,139,143,146,147,148,149,150,159,163,164,165,],[-41,49,49,49,49,49,49,49,49,-54,-53,-24,49,-52,-51,49,-23,49,-73,-71,-75,-72,-76,49,-74,-77,]),'GREATER':([75,90,93,94,95,96,102,103,122,134,153,154,155,156,158,],[-69,-65,-63,-62,-66,133,-68,-67,133,-70,-64,-61,-60,-58,-59,]),'MINUS':([68,71,75,78,90,92,93,94,95,96,97,98,100,101,102,103,117,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,153,154,155,156,157,158,],[97,97,-69,97,-65,97,-63,-62,-66,132,97,-69,97,132,-68,-67,-87,-88,97,132,-82,97,-86,97,-81,-84,-85,97,97,97,-83,-70,132,-64,-61,-60,-58,132,-59,]),'DIVIDE':([75,90,93,94,95,96,98,101,102,103,122,134,135,153,154,155,156,157,158,],[-69,-65,-63,-62,-66,124,-69,124,-68,-67,124,-70,124,-64,-61,-60,124,124,124,]),'RPAREN':([11,22,23,24,25,29,31,32,37,38,39,43,44,63,64,66,72,75,86,87,88,89,90,91,93,94,95,102,103,108,121,122,134,135,144,145,151,152,153,154,155,156,157,158,],[-44,-89,33,-49,-50,-89,-16,40,42,-13,-12,-89,-89,-15,-14,85,-56,-69,-55,114,-26,-25,-65,118,-63,-62,-66,-68,-67,139,152,153,-70,153,-28,-27,-79,-80,-64,-61,-60,-58,-78,-59,]),'SEMICOLON':([11,19,20,21,24,25,34,35,36,40,42,72,75,83,85,86,90,93,94,95,98,101,102,103,104,114,134,138,141,142,153,154,155,156,158,],[-44,-47,27,-48,-49,-50,-45,-48,-46,46,62,-56,-69,111,113,-55,-65,-63,-62,-66,-69,136,-68,-67,137,143,-70,-57,160,161,-64,-61,-60,-58,-59,]),'GREATEREQ':([75,90,93,94,95,96,102,103,122,134,153,154,155,156,158,],[-69,-65,-63,-62,-66,129,-68,-67,129,-70,-64,-61,-60,-58,-59,]),'COMMA':([11,19,21,24,25,35,38,39,72,75,86,88,89,102,103,],[-44,26,28,-49,-50,28,43,44,-56,-69,-55,115,116,-68,-67,]),'PLUS':([75,90,93,94,95,96,98,101,102,103,122,134,135,153,154,155,156,157,158,],[-69,-65,-63,-62,-66,130,-69,130,-68,-67,130,-70,130,-64,-61,-60,-58,130,-59,]),'$end':([2,3,4,5,6,7,14,15,16,17,27,46,62,79,112,140,],[-6,-7,0,-5,-8,-1,-3,-4,-2,-9,-41,-11,-10,-29,-18,-17,]),'RBRACE':([27,41,45,48,50,51,53,55,58,59,65,67,69,70,76,80,82,84,99,106,109,111,113,136,137,143,146,147,148,149,150,159,160,161,162,164,165,],[-41,-89,-89,-33,-30,-32,-40,-38,79,-31,-89,-37,-34,-36,-39,-35,-22,112,-54,-53,140,-21,-24,-52,-51,-23,-89,-73,-71,-75,-72,-76,-20,-19,164,-74,-77,]),'ASTERISK':([8,9,10,18,26,27,28,30,41,45,48,50,51,54,55,59,60,61,66,68,71,73,74,75,78,90,92,93,94,95,96,97,98,99,100,101,102,103,106,107,110,113,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,139,143,146,147,148,149,150,153,154,155,156,157,158,159,163,164,165,],[18,-43,-42,18,18,-41,18,18,54,54,54,54,54,74,54,54,18,54,54,74,74,74,74,-69,74,-65,74,-63,-62,-66,126,74,-69,-54,74,126,-68,-67,-53,74,54,-24,54,54,-87,54,-88,74,126,-82,74,-86,74,-81,-84,-85,74,74,74,-83,-70,126,-52,-51,54,-23,54,-73,-71,-75,-72,-64,-61,-60,126,126,126,-76,54,-74,-77,]),'EQUALS':([75,90,93,94,95,96,102,103,122,134,153,154,155,156,158,],[-69,-65,-63,-62,-66,127,-68,-67,127,-70,-64,-61,-60,-58,-59,]),'NUMBER':([68,71,78,92,97,100,117,119,120,123,124,125,126,127,128,129,130,131,132,133,],[90,90,90,90,90,90,-87,-88,90,-82,90,-86,90,-81,-84,-85,90,90,90,-83,]),'AMPERSAND':([54,68,71,73,74,77,78,92,97,100,107,117,119,120,123,124,125,126,127,128,129,130,131,132,133,],[73,73,73,73,73,107,73,73,73,73,73,-87,-88,73,-82,73,-86,73,-81,-84,-85,73,73,73,-83,]),'LPAREN':([11,12,13,21,24,25,47,49,57,68,71,78,92,97,98,100,105,117,119,120,123,124,125,126,127,128,129,130,131,132,133,],[-44,22,23,29,-49,-50,66,68,78,92,100,92,92,100,66,100,66,-87,-88,92,-82,100,-86,100,-81,-84,-85,100,100,100,-83,]),'ELSE':([99,106,113,136,137,143,147,148,149,150,159,164,165,],[-54,-53,-24,-52,-51,-23,-73,-71,-75,-72,163,-74,-77,]),'IF':([27,41,45,48,50,51,55,59,61,99,106,113,118,136,137,139,143,146,147,148,149,150,159,163,164,165,],[-41,57,57,57,57,57,57,57,57,-54,-53,-24,57,-52,-51,57,-23,57,-73,-71,-75,-72,-76,57,-74,-77,]),'LBRACE':([33,40,42,118,139,163,],[41,45,61,146,146,146,]),'NAME':([1,8,9,10,18,26,27,28,30,41,45,48,50,51,54,55,59,60,61,66,68,71,73,74,77,78,92,97,99,100,106,107,110,113,115,116,117,118,119,120,123,124,125,126,127,128,129,130,131,132,133,136,137,139,143,146,147,148,149,150,159,163,164,165,],[11,11,-43,-42,11,11,-41,11,11,47,47,47,47,47,75,47,47,11,47,86,75,98,75,75,105,75,75,75,-54,75,-53,75,86,-24,86,86,-87,86,-88,75,-82,75,-86,75,-81,-84,-85,75,75,75,-83,-52,-51,86,-23,47,-73,-71,-75,-72,-76,86,-74,-77,]),'LOGAND':([75,90,91,93,94,95,102,103,108,121,134,151,152,153,154,155,156,157,158,],[-69,-65,119,-63,-62,-66,-68,-67,119,119,-70,119,-80,-64,-61,-60,-58,-78,-59,]),'INT':([0,2,3,5,6,22,27,29,41,43,44,45,46,48,50,51,55,59,61,62,79,99,106,112,113,136,137,140,143,146,147,148,149,150,159,164,165,],[10,10,10,10,10,10,-41,10,10,10,10,10,-11,10,10,10,10,10,10,-10,-29,-54,-53,-18,-24,-52,-51,-17,-23,10,-73,-71,-75,-72,-76,-74,-77,]),'FLOAT':([0,2,3,5,6,22,27,29,41,43,44,45,46,48,50,51,55,59,61,62,79,99,106,112,113,136,137,140,143,146,147,148,149,150,159,164,165,],[9,9,9,9,9,9,-41,9,9,9,9,9,-11,9,9,9,9,9,9,-10,-29,-54,-53,-18,-24,-52,-51,-17,-23,9,-73,-71,-75,-72,-76,-74,-77,]),'LESSEREQ':([75,90,93,94,95,96,102,103,122,134,153,154,155,156,158,],[-69,-65,-63,-62,-66,125,-68,-67,125,-70,-64,-61,-60,-58,-59,]),'LESSER':([75,90,93,94,95,96,102,103,122,134,153,154,155,156,158,],[-69,-65,-63,-62,-66,128,-68,-67,128,-70,-64,-61,-60,-58,-59,]),'NUMBER2':([68,71,78,92,97,100,117,119,120,123,124,125,126,127,128,129,130,131,132,133,],[95,95,95,95,95,95,-87,-88,95,-82,95,-86,95,-81,-84,-85,95,95,95,-83,]),'MAIN':([1,],[13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'NUMBERvar':([68,71,78,92,97,100,120,124,126,130,131,132,],[93,93,93,93,93,93,93,93,93,93,93,93,]),'function_call':([41,45,48,50,51,55,59,61,71,77,146,],[48,48,48,48,48,48,48,48,99,106,48,]),'function_body':([0,2,3,5,6,],[2,2,2,2,2,]),'arglist':([66,115,116,],[87,144,145,]),'pointer':([8,18,26,28,30,60,],[21,24,35,35,39,35,]),'return_stat':([81,],[109,]),'varlist':([8,26,28,60,],[20,34,36,20,]),'assignment_statement':([41,45,48,50,51,55,59,61,118,139,146,163,],[50,50,50,50,50,50,50,50,147,147,50,147,]),'namevar':([1,8,18,26,28,30,60,],[12,19,25,19,19,38,19,]),'program':([0,2,3,5,6,],[3,3,3,3,3,]),'arguments':([22,29,43,44,],[32,37,63,64,]),'if_stat':([41,45,48,50,51,55,59,61,118,139,146,163,],[51,51,51,51,51,51,51,51,148,148,51,148,]),'var':([54,68,71,73,74,78,92,97,100,107,120,124,126,130,131,132,],[72,94,94,102,103,94,94,94,94,138,94,94,94,94,94,94,]),'function_content':([41,45,48,50,51,55,59,61,146,],[58,65,67,69,70,76,80,81,162,]),'LEFT':([41,45,48,50,51,55,59,61,66,110,115,116,118,139,146,163,],[52,52,52,52,52,52,52,52,89,142,89,89,52,52,52,52,]),'final_program':([0,],[4,]),'epsilon':([22,29,41,43,44,45,48,50,51,55,59,61,65,146,],[31,31,53,31,31,53,53,53,53,53,53,53,82,53,]),'function_dec':([0,2,3,5,6,],[5,5,5,5,5,]),'code_block':([118,139,163,],[149,159,165,]),'sign1':([96,122,],[131,131,]),'sign2':([91,108,121,151,],[120,120,120,120,]),'declaration':([0,2,3,5,6,41,45,48,50,51,55,59,61,146,],[6,6,6,6,6,55,55,55,55,55,55,55,55,55,]),'ID':([41,45,48,50,51,55,59,61,66,110,115,116,118,139,146,163,],[56,56,56,56,56,56,56,56,88,141,88,88,56,56,56,56,]),'RIGHT':([77,],[104,]),'program_content':([0,2,3,5,6,],[7,14,15,16,17,]),'while_stat':([41,45,48,50,51,55,59,61,118,139,146,163,],[59,59,59,59,59,59,59,59,150,150,59,150,]),'datatype':([0,2,3,5,6,22,29,41,43,44,45,48,50,51,55,59,61,146,],[8,8,8,8,8,30,30,60,30,30,60,60,60,60,60,60,60,60,]),'b_expression':([68,78,92,120,],[91,108,121,151,]),'expression':([68,71,78,92,97,100,120,124,126,130,131,132,],[96,101,96,122,134,135,96,154,155,156,157,158,]),'return_stat2':([65,],[84,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> final_program","S'",1,None,None,None),
  ('final_program -> program_content','final_program',1,'p_final_prog','bittu1.py',462),
  ('program_content -> function_dec program_content','program_content',2,'p_program_content','bittu1.py',468),
  ('program_content -> function_body program_content','program_content',2,'p_program_content','bittu1.py',469),
  ('program_content -> program program_content','program_content',2,'p_program_content','bittu1.py',470),
  ('program_content -> function_dec','program_content',1,'p_program_content2','bittu1.py',476),
  ('program_content -> function_body','program_content',1,'p_program_content2','bittu1.py',477),
  ('program_content -> program','program_content',1,'p_program_content2','bittu1.py',478),
  ('program_content -> declaration','program_content',1,'p_program_content3','bittu1.py',485),
  ('program_content -> declaration program_content','program_content',2,'p_program_content4','bittu1.py',497),
  ('function_dec -> datatype pointer LPAREN arguments RPAREN SEMICOLON','function_dec',6,'p_function_dec','bittu1.py',510),
  ('function_dec -> VOID namevar LPAREN arguments RPAREN SEMICOLON','function_dec',6,'p_function_dec','bittu1.py',511),
  ('arguments -> datatype pointer','arguments',2,'p_arguments','bittu1.py',522),
  ('arguments -> datatype namevar','arguments',2,'p_arguments','bittu1.py',523),
  ('arguments -> datatype pointer COMMA arguments','arguments',4,'p_arguments2','bittu1.py',530),
  ('arguments -> datatype namevar COMMA arguments','arguments',4,'p_arguments2','bittu1.py',531),
  ('arguments -> epsilon','arguments',1,'p_arguments3','bittu1.py',539),
  ('function_body -> datatype pointer LPAREN arguments RPAREN LBRACE function_content return_stat RBRACE','function_body',9,'p_function_body','bittu1.py',545),
  ('function_body -> VOID namevar LPAREN arguments RPAREN LBRACE function_content return_stat2 RBRACE','function_body',9,'p_function_body','bittu1.py',546),
  ('return_stat -> RETURN LEFT SEMICOLON','return_stat',3,'p_return','bittu1.py',584),
  ('return_stat -> RETURN ID SEMICOLON','return_stat',3,'p_return','bittu1.py',585),
  ('return_stat2 -> RETURN SEMICOLON','return_stat2',2,'p_return2','bittu1.py',593),
  ('return_stat2 -> epsilon','return_stat2',1,'p_return2','bittu1.py',594),
  ('function_call -> NAME LPAREN arglist RPAREN SEMICOLON','function_call',5,'p_func_call','bittu1.py',602),
  ('function_call -> NAME LPAREN RPAREN SEMICOLON','function_call',4,'p_func_call2','bittu1.py',611),
  ('arglist -> LEFT','arglist',1,'p_arglist','bittu1.py',621),
  ('arglist -> ID','arglist',1,'p_arglist','bittu1.py',622),
  ('arglist -> LEFT COMMA arglist','arglist',3,'p_arglist2','bittu1.py',627),
  ('arglist -> ID COMMA arglist','arglist',3,'p_arglist2','bittu1.py',628),
  ('program -> VOID MAIN LPAREN RPAREN LBRACE function_content RBRACE','program',7,'p_program','bittu1.py',636),
  ('function_content -> assignment_statement','function_content',1,'p_function_content','bittu1.py',673),
  ('function_content -> while_stat','function_content',1,'p_function_content','bittu1.py',674),
  ('function_content -> if_stat','function_content',1,'p_function_content','bittu1.py',675),
  ('function_content -> function_call','function_content',1,'p_function_content','bittu1.py',676),
  ('function_content -> assignment_statement function_content','function_content',2,'p_function_content2','bittu1.py',686),
  ('function_content -> while_stat function_content','function_content',2,'p_function_content2','bittu1.py',687),
  ('function_content -> if_stat function_content','function_content',2,'p_function_content2','bittu1.py',688),
  ('function_content -> function_call function_content','function_content',2,'p_function_content2','bittu1.py',689),
  ('function_content -> declaration','function_content',1,'p_function_content3','bittu1.py',701),
  ('function_content -> declaration function_content','function_content',2,'p_function_content4','bittu1.py',713),
  ('function_content -> epsilon','function_content',1,'p_function_content5','bittu1.py',725),
  ('declaration -> datatype varlist SEMICOLON','declaration',3,'p_declaration','bittu1.py',731),
  ('datatype -> INT','datatype',1,'p_datatype','bittu1.py',747),
  ('datatype -> FLOAT','datatype',1,'p_datatype','bittu1.py',748),
  ('namevar -> NAME','namevar',1,'p_namevar','bittu1.py',754),
  ('varlist -> namevar COMMA varlist','varlist',3,'p_varlist1','bittu1.py',761),
  ('varlist -> pointer COMMA varlist','varlist',3,'p_varlist1','bittu1.py',762),
  ('varlist -> namevar','varlist',1,'p_varlist2','bittu1.py',770),
  ('varlist -> pointer','varlist',1,'p_varlist2','bittu1.py',771),
  ('pointer -> ASTERISK pointer','pointer',2,'p_pointer','bittu1.py',779),
  ('pointer -> ASTERISK namevar','pointer',2,'p_pointer','bittu1.py',780),
  ('assignment_statement -> ID EQUAL RIGHT SEMICOLON','assignment_statement',4,'p_assignment_statement','bittu1.py',787),
  ('assignment_statement -> LEFT EQUAL expression SEMICOLON','assignment_statement',4,'p_assignment_statement','bittu1.py',788),
  ('assignment_statement -> ID EQUAL function_call','assignment_statement',3,'p_assignment_statement','bittu1.py',789),
  ('assignment_statement -> LEFT EQUAL function_call','assignment_statement',3,'p_assignment_statement','bittu1.py',790),
  ('ID -> NAME','ID',1,'p_id','bittu1.py',801),
  ('LEFT -> ASTERISK var','LEFT',2,'p_left','bittu1.py',809),
  ('RIGHT -> AMPERSAND var','RIGHT',2,'p_right','bittu1.py',817),
  ('expression -> expression PLUS expression','expression',3,'p_expression','bittu1.py',827),
  ('expression -> expression MINUS expression','expression',3,'p_expression','bittu1.py',828),
  ('expression -> expression ASTERISK expression','expression',3,'p_expression','bittu1.py',829),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','bittu1.py',830),
  ('expression -> var','expression',1,'p_expression2','bittu1.py',873),
  ('expression -> NUMBERvar','expression',1,'p_expression2','bittu1.py',874),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression3','bittu1.py',881),
  ('NUMBERvar -> NUMBER','NUMBERvar',1,'p_numvar','bittu1.py',887),
  ('NUMBERvar -> NUMBER2','NUMBERvar',1,'p_numvar2','bittu1.py',897),
  ('var -> ASTERISK var','var',2,'p_var','bittu1.py',907),
  ('var -> AMPERSAND var','var',2,'p_var','bittu1.py',908),
  ('var -> NAME','var',1,'p_var','bittu1.py',909),
  ('expression -> MINUS expression','expression',2,'p_expression_uminus','bittu1.py',936),
  ('code_block -> if_stat','code_block',1,'p_code_block','bittu1.py',948),
  ('code_block -> while_stat','code_block',1,'p_code_block','bittu1.py',949),
  ('code_block -> assignment_statement','code_block',1,'p_code_block','bittu1.py',950),
  ('code_block -> LBRACE function_content RBRACE','code_block',3,'p_code_block2','bittu1.py',958),
  ('while_stat -> WHILE LPAREN b_expression RPAREN code_block','while_stat',5,'p_while','bittu1.py',964),
  ('if_stat -> IF LPAREN b_expression RPAREN code_block','if_stat',5,'p_if1','bittu1.py',973),
  ('if_stat -> IF LPAREN b_expression RPAREN code_block ELSE code_block','if_stat',7,'p_if2','bittu1.py',983),
  ('b_expression -> expression sign1 expression','b_expression',3,'p_bool','bittu1.py',994),
  ('b_expression -> b_expression sign2 b_expression','b_expression',3,'p_bool2','bittu1.py',1018),
  ('b_expression -> LPAREN b_expression RPAREN','b_expression',3,'p_bool_paren1','bittu1.py',1034),
  ('sign1 -> EQUALS','sign1',1,'p_sign','bittu1.py',1040),
  ('sign1 -> NOTEQUAL','sign1',1,'p_sign','bittu1.py',1041),
  ('sign1 -> GREATER','sign1',1,'p_sign','bittu1.py',1042),
  ('sign1 -> LESSER','sign1',1,'p_sign','bittu1.py',1043),
  ('sign1 -> GREATEREQ','sign1',1,'p_sign','bittu1.py',1044),
  ('sign1 -> LESSEREQ','sign1',1,'p_sign','bittu1.py',1045),
  ('sign2 -> LOGOR','sign2',1,'p_sign1','bittu1.py',1052),
  ('sign2 -> LOGAND','sign2',1,'p_sign1','bittu1.py',1053),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','bittu1.py',1058),
]
