import sys
import ply.yacc as yacc
import logging 
from Lexer import Lexer
from utils import print_red, print_green

logging.basicConfig(
    level=logging.DEBUG,
    filename="parselog.log",
    filemode="w",
    format="%(filename)10s:%(lineno)4d:%(message)s"
)

log = logging.getLogger()

if len(sys.argv) != 2:
    print("Usage: python parser.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

# Definición del parser
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
        '''
        declaration_statement : type declaration_list SEMICOLON
        '''
        p[0] = ('declaration', p[1], p[2])

    def p_declaration_list(self, p):
        '''
        declaration_list : declaration_item
                        | declaration_list COMA declaration_item
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_declaration_item(self, p):
        '''
        declaration_item : ID
                        | ID ASSIGN expression
                        | ID LBRACKET expression RBRACKET ASSIGN array_initialization
                        | ID LBRACKET expression RBRACKET
                        | ID ASSIGN array_initialization
        '''
        if len(p) == 2:
            p[0] = (p[1], None)  # No initialization
        elif len(p) == 4:
            p[0] = ('assignment', p[1], p[3])
        elif len(p) == 6:
            p[0] = ('array_initialization', p[1], p[5])

    def p_array_initialization(self, p):
        '''
        array_initialization : LBRACKET value_list RBRACKET
        '''
        p[0] = p[2]

    def p_value_list(self, p):
        '''
        value_list : expression
                   | value_list COMA expression
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_expression_list(self, p):
        '''
        expression_list : expression
                        | expression_list COMA expression
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        else:
            p[0] = p[1] + [p[3]]

    def p_assignment_statement(self, p):
        '''
        assignment_statement : ID ASSIGN expression SEMICOLON
                             | ID LBRACKET expression RBRACKET ASSIGN expression SEMICOLON
        '''
        if len(p) == 5:
            p[0] = ('assignment', p[1], p[3])
        elif len(p) == 8:
            p[0] = ('array_element_assignment', p[1], p[3], p[6])
        
    def p_expression_statement(self, p):
        'expression_statement : expression SEMICOLON'
        p[0] = ('expression', p[1])

    def p_print_statement(self, p):
        '''
        print_statement : WRITELN LPAREN expression_list RPAREN SEMICOLON 
                        | WRITE LPAREN expression_list RPAREN SEMICOLON
        '''
        p[0] = ('print', p[1], p[3])
    
    def p_if_statement(self, p):
        '''
        if_statement : IF LPAREN expression RPAREN LBRACE statement_list RBRACE else_if_list optional_else
                     | IF LPAREN expression RPAREN LBRACE statement_list RBRACE optional_else
        '''
        if len(p) == 9:
            p[0] = ('if', p[3], p[6], p[8], None)  # No else block
        elif len(p) == 10:
            p[0] = ('if', p[3], p[6], p[8], p[9])
            
    def p_else_if_list(self, p):
        '''
        else_if_list : else_if_list ELSE IF LPAREN expression RPAREN LBRACE statement_list RBRACE
                    | ELSE IF LPAREN expression RPAREN LBRACE statement_list RBRACE
                    | empty
        '''
        if len(p) == 10:
            p[0] = p[1] + [('elseif', p[5], p[8])]
        elif len(p) == 9:
            p[0] = [('elseif', p[4], p[7])]
        else:
            p[0] = []

    def p_optional_else(self, p):
        '''
        optional_else : ELSE LBRACE statement_list RBRACE
                    | empty
        '''
        if len(p) == 5:
            p[0] = ('else', p[3])

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
                | expression AND expression
                | expression OR expression
                | NOT expression
                | LPAREN expression RPAREN
                | VAR_INT
                | VAR_FLOAT
                | STRING
                | ID
                | TRUE
                | FALSE
        '''
        if len(p) == 2:
            if p[1] in {True, False}:
                p[0] = p[1]
            else:
                p[0] = p[1]
        elif len(p) == 3:
            if p[2] in {'++', '--'}:
                p[0] = ('postfix_op', p[1], p[2])
            elif p[1] == '!':
                p[0] = ('unary_op', p[1], p[2])
            else:
                p[0] = ('binary_op', p[1], p[2])
        elif len(p) == 4:
            if p[1] == '(' and p[3] == ')':
                p[0] = p[2]
            else:
                p[0] = ('binary_op', p[1], p[2], p[3])

    def p_type(self, p):
        '''
        type : INT
             | FLOAT
             | BOOL
             | STRING
             | INT LBRACKET RBRACKET
             | FLOAT LBRACKET RBRACKET
        '''
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = f'{p[1]}[]'  # Array type
            
    def p_empty(self, p):
        'empty :'
        pass
    
    def p_error(self, p):
        print_red("\nSyntax error at line: %s, at token %s" % (p.lineno, p.value))

    def parse(self, data):
        lexer = self.lexer.get_lexer()
        self.parser = yacc.yacc(module=self, debug=log)
        result = self.parser.parse(input=data, lexer=lexer)
        return result


# Esto es para imprimir el resultado del parser
print_green("Parsing...")

parser = Parser()

#This is for printing the result of the parser
with open(filename, 'r') as inputfile:
    data = inputfile.read()

result = parser.parse(data)

if result:
    print_green("Parsing successful!")
    print_green(result)
else:
    print_red("Parsing failed!")
    sys.exit(1)