class Interpreter:
    def __init__(self):
        self.variables = {}
        self.output = []

    def generate(self, node):
        print(node, self.output, 'node mf! ')
        if node[0] == 'program':
            for statement in node[2]:
                self.generate(statement)
        elif node[0] == 'declaration':
            self.generate_declaration(node)
        elif node[0] == 'assignment':
            self.generate_assignment(node)
        elif node[0] == 'print':
            self.generate_print(node)
        elif node[0] == 'if':
            self.generate_if(node)
        elif node[0] == 'if_else':
            self.generate_if_else(node)
        elif node[0] == 'while':
            self.generate_while(node)
        elif node[0] == 'for':
            self.generate_for(node)
        # Ensure the method returns a string
        return "\n".join(self.output)

    def generate_declaration(self, node):
        for var in node[2]:
            self.output.append(f"{var} = None")

    def generate_assignment(self, node):
        value = self.generate_expression(node[2])
        self.output.append(f"{node[1]} = {value}")

    def generate_print(self, node):
        value = self.generate_expression(node[1])
        self.output.append(f"print({value})")

    def generate_if(self, node):
        condition = self.generate_expression(node[1])
        self.output.append(f"if {condition}:")
        self.output.extend(["    " + stmt for stmt in self.generate_statements(node[2])])

    def generate_if_else(self, node):
        condition = self.generate_expression(node[1])
        self.output.append(f"if {condition}:")
        self.output.extend(["    " + stmt for stmt in self.generate_statements(node[2])])
        self.output.append("else:")
        self.output.extend(["    " + stmt for stmt in self.generate_statements(node[3])])

    def generate_while(self, node):
        condition = self.generate_expression(node[1])
        self.output.append(f"while {condition}:")
        self.output.extend(["    " + stmt for stmt in self.generate_statements(node[2])])

    def generate_for(self, node):
        init = self.generate_statement(node[1])
        condition = self.generate_expression(node[2])
        increment = self.generate_statement(node[3])
        self.output.append(init)
        self.output.append(f"while {condition}:")
        body = ["    " + stmt for stmt in self.generate_statements(node[4])]
        body.append("    " + increment)
        self.output.extend(body)

    def generate_expression(self, node):
        if isinstance(node, tuple):
            if node[0] == 'binary_op':
                left = self.generate_expression(node[1])
                op = node[2]
                right = self.generate_expression(node[3])
                return f"({left} {op} {right})"
            elif node[0] == 'postfix_op':
                expr = self.generate_expression(node[1])
                if node[2] == '++':
                    return f"({expr} + 1)"
                elif node[2] == '--':
                    return f"({expr} - 1)"
        else:
            return str(node)

    def generate_statements(self, statements):
        result = []
        for statement in statements:
            result.append(self.generate_statement(statement))
        return result

    def generate_statement(self, statement):
        original_output = self.output
        self.output = []
        self.generate(statement)
        result = "\n".join(self.output)
        self.output = original_output
        return result

    def to_python_code(self):
        return "\n".join(self.output)

def save_and_run_python_code(python_code):
    with open("temp.py", "w") as file:
        file.write(python_code)
    exec(open("temp.py").read())

# Assuming `parsed_data` comes from your parser:
# interpreter = Interpreter()
# python_code = interpreter.generate(parsed_data)
# save_and_run_python_code(python_code)
