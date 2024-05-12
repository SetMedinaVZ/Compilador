import sys
import ply.yacc as yacc
from Lexer import Lexer
import logging


logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.txt",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)
log = logging.getLogger()

if len(sys.argv) != 2:
    print("Usage: python parser.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.lexer = Lexer()
        self.parser = None

    def p_program(self, p):
        'program : PROGRAM ID LBRACE statement_list RBRACE'
        p[0] = ('program', p[2], p[4])

    def p_statement_list(self, p):
        '''
        statement_list : statement
                       | statement_list statement
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[2]]

    def p_statement(self, p):
        '''
        statement : expression_statement 
                  | declaration_statement
                  | assignment_statement
                  | print_statement
                  | if_statement
                  | while_statement
                  | for_statement
        '''
        p[0] = p[1]

    def p_declaration_statement(self, p):
        'declaration_statement : type id_list SEMICOLON'
        p[0] = ('declaration', p[1], p[2])

    def p_id_list(self, p):
        '''
        id_list : ID
                | id_list COMA ID
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_assignment_statement(self, p):
        'assignment_statement : ID ASSIGN expression SEMICOLON'
        p[0] = ('assignment', p[1], p[3])
        
    def p_expression_statement(self, p):
        'expression_statement : expression SEMICOLON'
        p[0] = p[1]

    def p_print_statement(self, p):
        '''
        print_statement : WRITELN LPAREN expression RPAREN SEMICOLON 
                        | WRITE LPAREN expression RPAREN SEMICOLON
        '''
        p[0] = ('print', p[3])

    def p_if_statement(self, p):
        '''
        if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE
                     | IF LPAREN expression RPAREN LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE
        '''
        if len(p) == 8:
            p[0] = ('if', p[3], p[6])
        else:
            p[0] = ('if_else', p[3], p[6], p[10])

    def p_while_statement(self, p):
        'while_statement : WHILE LPAREN expression RPAREN LBRACE statement_list RBRACE'
        p[0] = ('while', p[3], p[6])

    def p_for_statement(self, p):
        'for_statement : FOR LPAREN assignment_statement expression SEMICOLON expression RPAREN LBRACE statement_list RBRACE'
        p[0] = ('for', p[3], p[4], p[6], p[9])

    def p_expression(self, p):
        '''
        expression : expression PLUSPLUS
                | expression MINUSMINUS
                | PLUSPLUS expression
                | MINUSMINUS expression
                | expression PLUS expression
                | expression MINUS expression
                | expression TIMES expression
                | expression DIVIDE expression
                | expression LT expression
                | expression GT expression
                | expression LTE expression
                | expression GTE expression
                | expression EQ expression
                | expression NE expression
                | VAR_INT
                | VAR_FLOAT
                | STRING
                | ID
        '''
        if len(p) == 2:
            p[0] = p[1]
        elif len(p) == 3:
            if p[2] in {'++', '--'}:
                p[0] = ('postfix_op', p[1], p[2])
            else:
                p[0] = ('binary_op', p[1], p[3], p[2])
        else:
            p[0] = ('binary_op', p[1], p[2], p[3])

    def p_type(self, p):
        '''
        type : INT
             | FLOAT
             | BOOL
             | STRING
        '''
        p[0] = p[1]

    def p_error(self, p):
        print("Syntax error at line: %s, at token %s" % (p.lineno, p.value))

    def parse(self, data):
        lexer = self.lexer.get_lexer()
        self.parser = yacc.yacc(module=self, debug=log)
        result = self.parser.parse(input=data, lexer=lexer, debug=log)
        return result

parser = Parser()

with open(filename, 'r') as inputfile:
    data = inputfile.read()

result = parser.parse(data)
print(result)
