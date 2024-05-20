import sys
import ply.yacc as yacc
from Lexer import Lexer
from utils import print_red, print_green

if len(sys.argv) != 2:
    print("Usage: python parser.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.lexer = Lexer()
        self.parser = None

    # def types(self, p):
    #     '''
    #     type : INT
    #          | FLOAT
    #          | BOOL
    #          | STRING
    #          | INT LBRACKET RBRACKET
    #          | FLOAT LBRACKET RBRACKET
    #          | BOOL LBRACKET RBRACKET
    #          | STRING LBRACKET RBRACKET
    #          | INT LBRACKET expression RBRACKET
    #          | FLOAT LBRACKET expression RBRACKET
    #          | BOOL LBRACKET expression RBRACKET
    #          | STRING LBRACKET expression RBRACKET   
    #     '''
    #     if len(p) == 2:
    #         p[0] = p[1]
    #     else:
            # p[0] = f'{p[1]}[]'  # Array type


    # def generation(self, node):
        # if node is None:
        #     return ''
        # node_type = node[0]
        # if node_type == 'program':
        #     return self.generation(node[2])
        # elif node_type == 'declaration':
        #     return self.generation(node[1])
        # elif node_type == 'declaration_list':
        #     return ''.join([self.generation(child) for child in node[1]])
        # elif node_type == 'declaration_item':
        #     return f'{node[1]} = {self.generation(node[2])}\n'
        # elif node_type == 'array_initialization':
        #     return f'{node[1]} = {self.generation(node[2])}\n'
        # elif node_type == 'assignment':
        #     return f'{node[1]} = {self.generation(node[2])}\n'
        # elif node_type == 'array_element_assignment':
        #     return f'{node[1]}[{self.generation(node[2])}] = {self.generation(node[3])}\n'
        # elif node_type == 'print':
        #     return f'print({", ".join([self.generation(child) for child in node[2]])})\n'
        # elif node_type == 'if':
        #     result = f'if {self.generation(node[1])}:\n'
        #     result += self.generation(node[2])
        #     if node[3]:
        #         result += self.generation(node[3])
        #     return result
        # elif node_type == 'elseif':
        #     result = f'elif {self.generation(node[1])}:\n'
        #     result += self.generation(node[2])
        #     return result
        # elif node_type == 'else':
        #     return f'else:\n{self.generation(node[1])}\n'
        # elif node_type == 'while':
        #     return f'while {self.generation(node[1])}:\n{self.generation(node[2])}\n'
        # elif node_type == 'for':
        #     return f'for {self.generation(node[1])} in range({self.generation(node[2]), self.generation(node[3])}):\n{self.generation(node[4])}\n'
        # elif node_type == 'function_declaration':
        #     return f'def {node[1]}({", ".join([f"{child[1]}" for child in node[2]])}):\n{self.generation(node[3])}\n'
        # elif node_type == 'return':
        #     return f'return {self.generation(node[1])}\n'
        # elif node_type == 'expression':
        #     if len(node) == 2:
        #         return self.generation(node[1])
        #     elif len(node) == 3:
        #         if node[1] in {'++', '--'}:
        #             return f'{self.generation(node[1])}{node[2]}'
        #         else:
        #             return f'{node[1]}{self.generation(node[2])}'
        #     elif len(node) == 4:
        #         if node[1] == '(' and node[3] == ')':
        #             return f'({self.generation(node[2])})'
        #         else:
        #             return f'{self.generation(node[1])} {node[2]} {self.generation(node[3])}'
        # elif node_type == 'binary_op':
        #     return f'{self.generation(node[1])} {node[2]} {self.generation(node[3])}'
        # elif node_type == 'unary_op':
        #     return f'{node[1]}{self.generation(node[2])}'
        # elif node_type == 'postfix_op':
        #     return f'{self.generation(node[1])}{node[2]}'
        # elif node_type == 'function_call':
        #     return f'{node[1]}({", ".join([self.generation(child) for child in node[2]])})'
        # elif node_type == 'parameter_list':
        #     return ', '.join([self.generation(child) for child in node])
        # elif node_type == 'parameter':
        #     return f'{node[1]} {node[0]}'
        # elif node_type == 'argument_list':
        #     return ', '.join([self.generation(child) for child in node])
        # elif node_type == 'value_list':
        #     return ', '.join([self.generation(child) for child in node])
        # elif node_type == 'type':
        #     return node[0]
        # elif node_type == 'ID':
        #     return node
        # elif node_type == 'VAR_INT':
        #     return node
        # else: 
        #     pass



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
    
    # def p_statement_list_empty(self, p):
    #     'statement_list : empty'
    #     p[0] = []
    
    # def p_statement_list_statement(self, p):
    #     'statement_list : statement'
    #     p[0] = [p[1]]
    
    # def p_statement_list_statement_list(self, p):
    #     'statement_list : statement_list statement'
    #     p[0] = p[1] + [p[2]]

    def p_statement(self, p):
        '''
        statement : expression_statement 
                  | declaration_statement
                  | assignment_statement
                  | print_statement
                  | if_statement
                  | while_statement
                  | for_statement
                  | function_declaration
                  | return_statement
        '''
        p[0] = p[1]

    def p_function_declaration(self, p):
        'function_declaration : FUNCTION ID LPAREN parameter_list RPAREN LBRACE statement_list RBRACE'
        p[0] = ('function_declaration', p[2], p[4], p[7])

    def p_parameter_list(self, p):
        '''
        parameter_list : parameter
                       | parameter_list COMA parameter
                       | empty
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 4:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = []

    def p_parameter(self, p):
        'parameter : type ID'
        p[0] = (p[1], p[2])

    def p_return_statement(self, p):
        'return_statement : RETURN expression SEMICOLON'
        p[0] = ('return', p[2])

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

    # def p_else_if_list2(self, p):
    #     '''
    #     else_if_list : else_if_list ELSE IF LPAREN expression RPAREN LBRACE statement_list RBRACE
    #                 | ELSE IF LPAREN expression RPAREN LBRACE statement_list RBRACE
    #                 | empty
    #     '''
    #     if len(p) == 10:
    #         p[0] = p[1] + [('elseif', p[5], p[8])]
    #         p[0] = []
    #         self.p_error(p)
    #     elif len(p) == 9:
    #         p[0] = [('elseif', p[4], p[7])]
    #         p[0] = []
    #         self.p_error(p)

    def p_optional_else(self, p):
        '''
        optional_else : ELSE LBRACE statement_list RBRACE
                    | empty
        '''
        if len(p) == 5:
            p[0] = ('else', p[3])
    
    # def p_optional_else2(self, p):
    #     '''
    #     optional_else : ELSE LBRACE statement_list RBRACE
    #                 | empty
    #     '''
    #     if len(p) == 5:
    #         p[0] = ('else', p[3])
    #         p[0] = []
    #         self.p_error(p) # Syntax error

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
                | function_call
        '''
        if len(p) == 2:
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

    def p_function_call(self, p):
        'function_call : ID LPAREN argument_list RPAREN'
        p[0] = ('function_call', p[1], p[3])

    def p_argument_list(self, p):
        '''
        argument_list : expression
                      | argument_list COMA expression
                      | empty
        '''
        if len(p) == 2:
            p[0] = [p[1]]
        elif len(p) == 4:
            p[0] = p[1] + [p[3]]
        else:
            p[0] = []


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
        self.parser = yacc.yacc(module=self, debug=True, start='program')
        result = self.parser.parse(input=data, lexer=lexer)
        return result


# Esto es para imprimir el resultado del parser
print_green("Parsing...")

parser = Parser()

# Esto es para imprimir el resultado del parser
with open(filename, 'r') as inputfile:
    data = inputfile.read()

result = parser.parse(data)

if result:
    print_green("Parsing successful!")
    print_green(result)
else:
    print_red("Parsing failed!")
    sys.exit(1)
