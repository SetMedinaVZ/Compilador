class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, node):
        print(node , "node")
        if node[0] == 'program':
            self.execute_program(node)
        elif node[0] == 'declaration':
            self.execute_declaration(node)
        elif node[0] == 'assignment':
            self.execute_assignment(node)
        elif node[0] == 'print':
            self.execute_print(node)
        elif node[0] == 'if':
            self.execute_if(node)
        elif node[0] == 'if_else':
            self.execute_if_else(node)
        elif node[0] == 'while':
            self.execute_while(node)
        elif node[0] == 'for':
            self.execute_for(node)

    def execute_program(self, node):
        for statement in node[2]:
            self.interpret(statement)

    def execute_declaration(self, node):
        for var in node[2]:
            self.variables[var] = None

    def execute_assignment(self, node):
        self.variables[node[1]] = self.evaluate_expression(node[2])

    def execute_print(self, node):
        print(self.evaluate_expression(node[1]))

    def execute_if(self, node):
        if self.evaluate_expression(node[1]):
            for statement in node[2]:
                self.interpret(statement)

    def execute_if_else(self, node):
        if self.evaluate_expression(node[1]):
            for statement in node[2]:
                self.interpret(statement)
        else:
            for statement in node[3]:
                self.interpret(statement)

    def execute_while(self, node):
        while self.evaluate_expression(node[1]):
            for statement in node[2]:
                self.interpret(statement)

    def execute_for(self, node):
        self.interpret(node[1])
        while self.evaluate_expression(node[2]):
            for statement in node[4]:
                self.interpret(statement)
            self.interpret(node[3])

    def evaluate_expression(self, node):
        if isinstance(node, tuple):
            if node[0] == 'binary_op':
                left = self.evaluate_expression(node[1])
                right = self.evaluate_expression(node[3])
                if node[2] == '+':
                    return left + right
                elif node[2] == '-':
                    return left - right
                elif node[2] == '*':
                    return left * right
                elif node[2] == '/':
                    return left / right
                elif node[2] == '>':
                    return left > right
                elif node[2] == '<':
                    return left < right
                elif node[2] == '>=':
                    return left >= right
                elif node[2] == '<=':
                    return left <= right
                elif node[2] == '==':
                    return left == right
                elif node[2] == '!=':
                    return left != right
            elif node[0] == 'postfix_op':
                var = self.variables[node[1]]
                if node[2] == '++':
                    self.variables[node[1]] = var + 1
                    return var
                elif node[2] == '--':
                    self.variables[node[1]] = var - 1
                    return var
        else:
            if isinstance(node, int) or isinstance(node, float) or isinstance(node, str):
                return node
            else:
                return self.variables[node]
