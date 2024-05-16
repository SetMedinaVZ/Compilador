
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOL COMA DIVIDE ELSE EQ FALSE FLOAT FOR GT GTE ID IF INT LBRACE LBRACKET LPAREN LT LTE MINUS MINUSMINUS NE NOT OR PLUS PLUSPLUS PROGRAM RBRACE RBRACKET RPAREN SEMICOLON STRING TIMES TRUE VAR_BOOL VAR_FLOAT VAR_INT WHILE WRITE WRITELNprogram : PROGRAM ID LBRACE statement_list RBRACE\n        statement_list : statement\n                       | statement_list statement\n        \n        statement : expression_statement \n                  | declaration_statement\n                  | assignment_statement\n                  | print_statement\n                  | if_statement\n                  | while_statement\n                  | for_statement\n        \n        declaration_statement : type declaration_list SEMICOLON\n        \n        declaration_list : declaration_item\n                        | declaration_list COMA declaration_item\n        \n        declaration_item : ID\n                        | ID ASSIGN expression\n                        | ID LBRACKET expression RBRACKET ASSIGN array_initialization\n                        | ID LBRACKET expression RBRACKET\n                        | ID ASSIGN array_initialization\n        \n        array_initialization : LBRACKET int_list RBRACKET\n        \n        int_list : VAR_INT\n                 | int_list COMA VAR_INT\n        \n        expression_list : expression\n                        | expression_list COMA expression\n        \n        assignment_statement : ID ASSIGN expression SEMICOLON\n                             | ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLON\n        expression_statement : expression SEMICOLON\n        print_statement : WRITELN LPAREN expression RPAREN SEMICOLON \n                        | WRITE LPAREN expression RPAREN SEMICOLON\n        \n        if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE\n                     | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE\n        while_statement : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACEfor_statement : FOR LPAREN assignment_statement expression SEMICOLON expression RPAREN LBRACE statement_list RBRACE\n        expression : expression PLUSPLUS\n                | expression MINUSMINUS\n                | PLUSPLUS expression\n                | MINUSMINUS expression\n                | expression PLUS expression\n                | expression MINUS expression\n                | expression TIMES expression\n                | expression DIVIDE expression\n                | expression LT expression\n                | expression GT expression\n                | expression LTE expression\n                | expression GTE expression\n                | expression EQ expression\n                | expression NE expression\n                | expression AND expression\n                | expression OR expression\n                | NOT expression\n                | LPAREN expression RPAREN\n                | VAR_INT\n                | VAR_FLOAT\n                | STRING\n                | ID\n                | TRUE\n                | FALSE\n        \n        type : INT\n             | FLOAT\n             | BOOL\n             | STRING\n             | INT LBRACKET RBRACKET\n        '
    
_lr_action_items = {'PROGRAM':([0,],[2,]),'$end':([1,36,],[0,-1,]),'ID':([2,4,6,7,8,9,10,11,12,13,14,16,18,23,24,25,28,31,32,33,34,35,37,38,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,63,82,83,84,85,91,93,94,106,110,111,112,113,114,119,120,122,125,126,129,130,131,132,133,134,],[3,5,5,-2,-4,-5,-6,-7,-8,-9,-10,55,59,59,59,59,-60,-57,-58,-59,59,59,-3,-26,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,92,-11,55,59,59,59,-61,-24,59,-27,-28,5,5,59,5,5,-25,-29,-31,5,5,5,5,-32,-30,]),'LBRACE':([3,103,104,127,128,],[4,112,113,129,130,]),'WRITELN':([4,6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,112,113,119,120,122,125,126,129,130,131,132,133,134,],[17,17,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,17,17,17,17,-25,-29,-31,17,17,17,17,-32,-30,]),'WRITE':([4,6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,112,113,119,120,122,125,126,129,130,131,132,133,134,],[19,19,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,19,19,19,19,-25,-29,-31,19,19,19,19,-32,-30,]),'IF':([4,6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,112,113,119,120,122,125,126,129,130,131,132,133,134,],[20,20,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,20,20,20,20,-25,-29,-31,20,20,20,20,-32,-30,]),'WHILE':([4,6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,112,113,119,120,122,125,126,129,130,131,132,133,134,],[21,21,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,21,21,21,21,-25,-29,-31,21,21,21,21,-32,-30,]),'FOR':([4,6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,112,113,119,120,122,125,126,129,130,131,132,133,134,],[22,22,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,22,22,22,22,-25,-29,-31,22,22,22,22,-32,-30,]),'PLUSPLUS':([4,5,6,7,8,9,10,11,12,13,14,15,18,23,24,25,26,27,28,29,30,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,62,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,91,94,97,100,105,106,110,111,112,113,114,115,119,120,121,122,125,126,129,130,131,132,133,134,],[23,-54,23,-2,-4,-5,-6,-7,-8,-9,-10,39,23,23,23,23,-51,-52,-53,-55,-56,23,23,-3,-26,-33,-34,23,23,23,23,23,23,23,23,23,23,23,23,23,39,-53,-54,23,23,23,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-11,23,23,39,-50,39,39,39,23,-24,39,39,39,23,-27,-28,23,23,23,39,23,23,39,-25,-29,-31,23,23,23,23,-32,-30,]),'MINUSMINUS':([4,5,6,7,8,9,10,11,12,13,14,15,18,23,24,25,26,27,28,29,30,34,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,56,57,58,59,60,61,62,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,91,94,97,100,105,106,110,111,112,113,114,115,119,120,121,122,125,126,129,130,131,132,133,134,],[24,-54,24,-2,-4,-5,-6,-7,-8,-9,-10,40,24,24,24,24,-51,-52,-53,-55,-56,24,24,-3,-26,-33,-34,24,24,24,24,24,24,24,24,24,24,24,24,24,40,-53,-54,24,24,24,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-11,24,24,40,-50,40,40,40,24,-24,40,40,40,24,-27,-28,24,24,24,40,24,24,40,-25,-29,-31,24,24,24,24,-32,-30,]),'NOT':([4,6,7,8,9,10,11,12,13,14,18,23,24,25,34,35,37,38,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,82,84,85,91,94,106,110,111,112,113,114,119,120,122,125,126,129,130,131,132,133,134,],[25,25,-2,-4,-5,-6,-7,-8,-9,-10,25,25,25,25,25,25,-3,-26,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-11,25,25,25,-24,25,-27,-28,25,25,25,25,25,-25,-29,-31,25,25,25,25,-32,-30,]),'LPAREN':([4,6,7,8,9,10,11,12,13,14,17,18,19,20,21,22,23,24,25,34,35,37,38,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,82,84,85,91,94,106,110,111,112,113,114,119,120,122,125,126,129,130,131,132,133,134,],[18,18,-2,-4,-5,-6,-7,-8,-9,-10,56,18,60,61,62,63,18,18,18,18,18,-3,-26,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-11,18,18,18,-24,18,-27,-28,18,18,18,18,18,-25,-29,-31,18,18,18,18,-32,-30,]),'VAR_INT':([4,6,7,8,9,10,11,12,13,14,18,23,24,25,34,35,37,38,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,82,84,85,91,94,99,106,110,111,112,113,114,117,119,120,122,125,126,129,130,131,132,133,134,],[26,26,-2,-4,-5,-6,-7,-8,-9,-10,26,26,26,26,26,26,-3,-26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-11,26,26,26,-24,108,26,-27,-28,26,26,26,123,26,26,-25,-29,-31,26,26,26,26,-32,-30,]),'VAR_FLOAT':([4,6,7,8,9,10,11,12,13,14,18,23,24,25,34,35,37,38,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,82,84,85,91,94,106,110,111,112,113,114,119,120,122,125,126,129,130,131,132,133,134,],[27,27,-2,-4,-5,-6,-7,-8,-9,-10,27,27,27,27,27,27,-3,-26,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-11,27,27,27,-24,27,-27,-28,27,27,27,27,27,-25,-29,-31,27,27,27,27,-32,-30,]),'STRING':([4,6,7,8,9,10,11,12,13,14,18,23,24,25,34,35,37,38,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,82,84,85,91,94,106,110,111,112,113,114,119,120,122,125,126,129,130,131,132,133,134,],[28,28,-2,-4,-5,-6,-7,-8,-9,-10,58,58,58,58,58,58,-3,-26,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,-11,58,58,58,-24,58,-27,-28,28,28,58,28,28,-25,-29,-31,28,28,28,28,-32,-30,]),'TRUE':([4,6,7,8,9,10,11,12,13,14,18,23,24,25,34,35,37,38,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,82,84,85,91,94,106,110,111,112,113,114,119,120,122,125,126,129,130,131,132,133,134,],[29,29,-2,-4,-5,-6,-7,-8,-9,-10,29,29,29,29,29,29,-3,-26,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-11,29,29,29,-24,29,-27,-28,29,29,29,29,29,-25,-29,-31,29,29,29,29,-32,-30,]),'FALSE':([4,6,7,8,9,10,11,12,13,14,18,23,24,25,34,35,37,38,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,82,84,85,91,94,106,110,111,112,113,114,119,120,122,125,126,129,130,131,132,133,134,],[30,30,-2,-4,-5,-6,-7,-8,-9,-10,30,30,30,30,30,30,-3,-26,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-11,30,30,30,-24,30,-27,-28,30,30,30,30,30,-25,-29,-31,30,30,30,30,-32,-30,]),'INT':([4,6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,112,113,119,120,122,125,126,129,130,131,132,133,134,],[31,31,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,31,31,31,31,-25,-29,-31,31,31,31,31,-32,-30,]),'FLOAT':([4,6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,112,113,119,120,122,125,126,129,130,131,132,133,134,],[32,32,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,32,32,32,32,-25,-29,-31,32,32,32,32,-32,-30,]),'BOOL':([4,6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,112,113,119,120,122,125,126,129,130,131,132,133,134,],[33,33,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,33,33,33,33,-25,-29,-31,33,33,33,33,-32,-30,]),'ASSIGN':([5,55,92,95,109,],[34,84,34,106,118,]),'LBRACKET':([5,31,55,84,92,118,],[35,67,85,99,35,99,]),'SEMICOLON':([5,15,26,27,28,29,30,39,40,53,54,55,58,59,64,65,66,68,70,71,72,73,74,75,76,77,78,79,80,81,87,96,97,98,101,102,105,109,115,116,124,],[-54,38,-51,-52,-53,-55,-56,-33,-34,82,-12,-14,-53,-54,-35,-36,-49,94,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-13,-15,-18,110,111,114,-17,122,-19,-16,]),'PLUS':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,41,-51,-52,-53,-55,-56,-33,-34,41,-53,-54,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-50,41,41,41,41,41,41,41,41,]),'MINUS':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,42,-51,-52,-53,-55,-56,-33,-34,42,-53,-54,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-50,42,42,42,42,42,42,42,42,]),'TIMES':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,43,-51,-52,-53,-55,-56,-33,-34,43,-53,-54,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-50,43,43,43,43,43,43,43,43,]),'DIVIDE':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,44,-51,-52,-53,-55,-56,-33,-34,44,-53,-54,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-50,44,44,44,44,44,44,44,44,]),'LT':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,45,-51,-52,-53,-55,-56,-33,-34,45,-53,-54,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-50,45,45,45,45,45,45,45,45,]),'GT':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,46,-51,-52,-53,-55,-56,-33,-34,46,-53,-54,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-50,46,46,46,46,46,46,46,46,]),'LTE':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,47,-51,-52,-53,-55,-56,-33,-34,47,-53,-54,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-50,47,47,47,47,47,47,47,47,]),'GTE':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,48,-51,-52,-53,-55,-56,-33,-34,48,-53,-54,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-50,48,48,48,48,48,48,48,48,]),'EQ':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,49,-51,-52,-53,-55,-56,-33,-34,49,-53,-54,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-50,49,49,49,49,49,49,49,49,]),'NE':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,50,-51,-52,-53,-55,-56,-33,-34,50,-53,-54,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-50,50,50,50,50,50,50,50,50,]),'AND':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,51,-51,-52,-53,-55,-56,-33,-34,51,-53,-54,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-50,51,51,51,51,51,51,51,51,]),'OR':([5,15,26,27,28,29,30,39,40,57,58,59,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,97,100,105,115,121,],[-54,52,-51,-52,-53,-55,-56,-33,-34,52,-53,-54,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-50,52,52,52,52,52,52,52,52,]),'RBRACE':([6,7,8,9,10,11,12,13,14,37,38,82,94,110,111,119,120,122,125,126,131,132,133,134,],[36,-2,-4,-5,-6,-7,-8,-9,-10,-3,-26,-11,-24,-27,-28,125,126,-25,-29,-31,133,134,-32,-30,]),'RPAREN':([26,27,29,30,39,40,57,58,59,64,65,66,70,71,72,73,74,75,76,77,78,79,80,81,86,87,88,89,90,121,],[-51,-52,-55,-56,-33,-34,87,-53,-54,-35,-36,-49,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,101,-50,102,103,104,127,]),'RBRACKET':([26,27,29,30,39,40,58,59,64,65,66,67,69,70,71,72,73,74,75,76,77,78,79,80,81,87,100,107,108,123,],[-51,-52,-55,-56,-33,-34,-53,-54,-35,-36,-49,93,95,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,109,116,-20,-21,]),'COMA':([26,27,29,30,39,40,53,54,55,58,59,64,65,66,70,71,72,73,74,75,76,77,78,79,80,81,87,96,97,98,107,108,109,116,123,124,],[-51,-52,-55,-56,-33,-34,83,-12,-14,-53,-54,-35,-36,-49,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,-48,-50,-13,-15,-18,117,-20,-17,-19,-21,-16,]),'ELSE':([125,],[128,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([4,112,113,129,130,],[6,119,120,131,132,]),'statement':([4,6,112,113,119,120,129,130,131,132,],[7,37,7,7,37,37,7,7,37,37,]),'expression_statement':([4,6,112,113,119,120,129,130,131,132,],[8,8,8,8,8,8,8,8,8,8,]),'declaration_statement':([4,6,112,113,119,120,129,130,131,132,],[9,9,9,9,9,9,9,9,9,9,]),'assignment_statement':([4,6,63,112,113,119,120,129,130,131,132,],[10,10,91,10,10,10,10,10,10,10,10,]),'print_statement':([4,6,112,113,119,120,129,130,131,132,],[11,11,11,11,11,11,11,11,11,11,]),'if_statement':([4,6,112,113,119,120,129,130,131,132,],[12,12,12,12,12,12,12,12,12,12,]),'while_statement':([4,6,112,113,119,120,129,130,131,132,],[13,13,13,13,13,13,13,13,13,13,]),'for_statement':([4,6,112,113,119,120,129,130,131,132,],[14,14,14,14,14,14,14,14,14,14,]),'expression':([4,6,18,23,24,25,34,35,41,42,43,44,45,46,47,48,49,50,51,52,56,60,61,62,84,85,91,106,112,113,114,119,120,129,130,131,132,],[15,15,57,64,65,66,68,69,70,71,72,73,74,75,76,77,78,79,80,81,86,88,89,90,97,100,105,115,15,15,121,15,15,15,15,15,15,]),'type':([4,6,112,113,119,120,129,130,131,132,],[16,16,16,16,16,16,16,16,16,16,]),'declaration_list':([16,],[53,]),'declaration_item':([16,83,],[54,96,]),'array_initialization':([84,118,],[98,124,]),'int_list':([99,],[107,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> PROGRAM ID LBRACE statement_list RBRACE','program',5,'p_program','parser_.py',28),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser_.py',33),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser_.py',34),
  ('statement -> expression_statement','statement',1,'p_statement','parser_.py',43),
  ('statement -> declaration_statement','statement',1,'p_statement','parser_.py',44),
  ('statement -> assignment_statement','statement',1,'p_statement','parser_.py',45),
  ('statement -> print_statement','statement',1,'p_statement','parser_.py',46),
  ('statement -> if_statement','statement',1,'p_statement','parser_.py',47),
  ('statement -> while_statement','statement',1,'p_statement','parser_.py',48),
  ('statement -> for_statement','statement',1,'p_statement','parser_.py',49),
  ('declaration_statement -> type declaration_list SEMICOLON','declaration_statement',3,'p_declaration_statement','parser_.py',55),
  ('declaration_list -> declaration_item','declaration_list',1,'p_declaration_list','parser_.py',61),
  ('declaration_list -> declaration_list COMA declaration_item','declaration_list',3,'p_declaration_list','parser_.py',62),
  ('declaration_item -> ID','declaration_item',1,'p_declaration_item','parser_.py',71),
  ('declaration_item -> ID ASSIGN expression','declaration_item',3,'p_declaration_item','parser_.py',72),
  ('declaration_item -> ID LBRACKET expression RBRACKET ASSIGN array_initialization','declaration_item',6,'p_declaration_item','parser_.py',73),
  ('declaration_item -> ID LBRACKET expression RBRACKET','declaration_item',4,'p_declaration_item','parser_.py',74),
  ('declaration_item -> ID ASSIGN array_initialization','declaration_item',3,'p_declaration_item','parser_.py',75),
  ('array_initialization -> LBRACKET int_list RBRACKET','array_initialization',3,'p_array_initialization','parser_.py',86),
  ('int_list -> VAR_INT','int_list',1,'p_int_list','parser_.py',92),
  ('int_list -> int_list COMA VAR_INT','int_list',3,'p_int_list','parser_.py',93),
  ('expression_list -> expression','expression_list',1,'p_expression_list','parser_.py',102),
  ('expression_list -> expression_list COMA expression','expression_list',3,'p_expression_list','parser_.py',103),
  ('assignment_statement -> ID ASSIGN expression SEMICOLON','assignment_statement',4,'p_assignment_statement','parser_.py',112),
  ('assignment_statement -> ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLON','assignment_statement',7,'p_assignment_statement','parser_.py',113),
  ('expression_statement -> expression SEMICOLON','expression_statement',2,'p_expression_statement','parser_.py',121),
  ('print_statement -> WRITELN LPAREN expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','parser_.py',126),
  ('print_statement -> WRITE LPAREN expression RPAREN SEMICOLON','print_statement',5,'p_print_statement','parser_.py',127),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE','if_statement',7,'p_if_statement','parser_.py',133),
  ('if_statement -> IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE','if_statement',11,'p_if_statement','parser_.py',134),
  ('while_statement -> WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE','while_statement',7,'p_while_statement','parser_.py',142),
  ('for_statement -> FOR LPAREN assignment_statement expression SEMICOLON expression RPAREN LBRACE statement_list RBRACE','for_statement',10,'p_for_statement','parser_.py',146),
  ('expression -> expression PLUSPLUS','expression',2,'p_expression','parser_.py',151),
  ('expression -> expression MINUSMINUS','expression',2,'p_expression','parser_.py',152),
  ('expression -> PLUSPLUS expression','expression',2,'p_expression','parser_.py',153),
  ('expression -> MINUSMINUS expression','expression',2,'p_expression','parser_.py',154),
  ('expression -> expression PLUS expression','expression',3,'p_expression','parser_.py',155),
  ('expression -> expression MINUS expression','expression',3,'p_expression','parser_.py',156),
  ('expression -> expression TIMES expression','expression',3,'p_expression','parser_.py',157),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression','parser_.py',158),
  ('expression -> expression LT expression','expression',3,'p_expression','parser_.py',159),
  ('expression -> expression GT expression','expression',3,'p_expression','parser_.py',160),
  ('expression -> expression LTE expression','expression',3,'p_expression','parser_.py',161),
  ('expression -> expression GTE expression','expression',3,'p_expression','parser_.py',162),
  ('expression -> expression EQ expression','expression',3,'p_expression','parser_.py',163),
  ('expression -> expression NE expression','expression',3,'p_expression','parser_.py',164),
  ('expression -> expression AND expression','expression',3,'p_expression','parser_.py',165),
  ('expression -> expression OR expression','expression',3,'p_expression','parser_.py',166),
  ('expression -> NOT expression','expression',2,'p_expression','parser_.py',167),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression','parser_.py',168),
  ('expression -> VAR_INT','expression',1,'p_expression','parser_.py',169),
  ('expression -> VAR_FLOAT','expression',1,'p_expression','parser_.py',170),
  ('expression -> STRING','expression',1,'p_expression','parser_.py',171),
  ('expression -> ID','expression',1,'p_expression','parser_.py',172),
  ('expression -> TRUE','expression',1,'p_expression','parser_.py',173),
  ('expression -> FALSE','expression',1,'p_expression','parser_.py',174),
  ('type -> INT','type',1,'p_type','parser_.py',194),
  ('type -> FLOAT','type',1,'p_type','parser_.py',195),
  ('type -> BOOL','type',1,'p_type','parser_.py',196),
  ('type -> STRING','type',1,'p_type','parser_.py',197),
  ('type -> INT LBRACKET RBRACKET','type',3,'p_type','parser_.py',198),
]
