import ply.lex as lex


class Lexer(object):
    def __init__(self):
        self.lexer = None
        
    def get_lexer(self):
        self.lexer = lex.lex(module=self)
        return self.lexer

    # Reserved words
    reserved = {
        'program': 'PROGRAM',
        'if': 'IF',
        'else': "ELSE",
        'while': 'WHILE',
        'for': 'FOR',
        'writeln': 'WRITELN',
        'int': 'INT',
        'float': 'FLOAT',
        'bool': 'BOOL',
        'string': 'STRING',
    }

    # List of token names
    tokens = [
                 'ID', 'SEMICOLON', 'COMA', 'ASSIGN',
                 'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE',  # BRACES
                 'VAR_INT', 'VAR_FLOAT', "VAR_STRING",  # VAR TYPE
                 'PLUS', 'MINUS', 'DIVIDE', 'TIMES', 'PLUSPLUS', 'MINUSMINUS',  # ARITHMETIC OPERATORS
                 'GT', 'LT', 'GTE', 'LTE', 'EQ', 'NE'  # LOGICAL OPERATORS
             ] + list(reserved.values())

    # Regular expression rules for tokens
    t_SEMICOLON = r';'
    t_COMA = r','
    t_ASSIGN = r'='
    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_LBRACE = r'\{'
    t_RBRACE = r'\}'
    t_STRING = r'\".*?\"'
    t_PLUSPLUS = r'\+\+'
    t_MINUSMINUS = r'-\-'
    t_PLUS = r'\+'
    t_MINUS = r'-'
    t_DIVIDE = r'\/'
    t_TIMES = r'\*'
    t_GT = r'>'
    t_LT = r'<'
    t_GTE = r'>='
    t_LTE = r'<='
    t_EQ = r'=='
    t_NE = r'!='

    # A string containing ignored characters (spaces and tabs)
    t_ignore = ' \t'

    def t_VAR_FLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_VAR_INT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    # If it's not in the reserved words, it's an ID, else its reserved
    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')  # Check for reserved words
        return t

    # Discard comments
    def t_COMMENT(self, _):
        r'\#.*'
        pass
        # No return value. Token discarded

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # Error handling rule
    def t_error(self, t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    def get_tokens(self, data, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        # Give the lexer some input
        self.lexer.input(data)

        all_tokens = []
        # Tokenize
        while True:
            tok = self.lexer.token()
            if not tok:
                break  # No more input
            all_tokens.append((tok.type, tok.value))
        return all_tokens
