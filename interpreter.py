import sys
print("Interpreter.py imported")

class Interpreter:
    def __init__(self):
        self.quadruples = []  # List to store quadruples
        self.temp_counter = 0  # Counter for temporary variables
        self.variables = {}  # Dictionary to store variable values
        self.var_types = {}  # Dictionary to store variable types
        self.output = []  # List to store generated Python code
        self.indent_level = 0  # Current indentation level

    def new_temp(self):
        self.temp_counter += 1
        return f"t{self.temp_counter}"

    def generate_quadruple(self, op, arg1, arg2, result):
        self.quadruples.append((op, arg1, arg2, result))

    def generate(self, node):
        if node[0] == 'program':
            for statement in node[2]:
                self.generate(statement)
        elif node[0] == 'declaration':
            self.generate_declaration(node)
        elif node[0] == 'assignment':
            self.generate_assignment(node)
        elif node[0] == 'array_element_assignment':
            self.generate_array_element_assignment(node)
        elif node[0] == 'print':
            self.generate_print(node)
        elif node[0] == 'if':
            self.generate_if(node)
        elif node[0] == 'while':
            self.generate_while(node)
        elif node[0] == 'for':
            self.generate_for(node)
        else:
            raise TypeError(f"Unsupported node type: {node[0]}")
        return "\n".join(self.output)

    def generate_declaration(self, node):
        var_type = node[1]
        for var_decl in node[2]:
            var = var_decl[0]
            expr = var_decl[1]
            self.var_types[var] = var_type  # Store variable type
            if expr is None:
                self.variables[var] = None
                self.output.append(f"{'    ' * self.indent_level}{var} = None")
            elif isinstance(expr, list):  # Array initialization
                processed_values = [self.generate_expression(value) for value in expr]
                values_str = ", ".join(processed_values)
                self.variables[var] = processed_values
                self.output.append(f"{'    ' * self.indent_level}{var} = [{values_str}]")
            else:
                value = self.generate_expression(expr)
                self.variables[var] = value
                self.output.append(f"{'    ' * self.indent_level}{var} = {value}")

    def generate_assignment(self, node):
        var_name = node[1]
        value = self.generate_expression(node[2])
        self.variables[var_name] = value
        self.output.append(f"{'    ' * self.indent_level}{var_name} = {value}")

    def generate_array_element_assignment(self, node):
        var_name = node[1]
        index = self.generate_expression(node[2])
        value = self.generate_expression(node[3])
        self.output.append(f"{'    ' * self.indent_level}{var_name}[{index}] = {value}")

    def generate_print(self, node):
        expressions = [self.generate_expression(expr) for expr in node[2]]
        if node[1] == 'writeln':
            self.output.append(f"{'    ' * self.indent_level}print({', '.join(expressions)})")
        else:
            self.output.append(f"{'    ' * self.indent_level}print({', '.join(expressions)}, end='')")

    def generate_if(self, node):
        condition = self.generate_expression(node[1])
        self.output.append(f"{'    ' * self.indent_level}if {condition}:")
        self.indent_level += 1
        self.generate_statements(node[2])
        self.indent_level -= 1

        if len(node) > 3:
            if node[3] and isinstance(node[3], list):
                self.generate_else_if_and_else(node[3], node[4] if len(node) > 4 else None)
            else:
                self.generate_else(node[3])

    def generate_else_if_and_else(self, elseifs, else_block):
        for elseif in elseifs:
            condition_elseif = self.generate_expression(elseif[1])
            self.output.append(f"{'    ' * self.indent_level}elif {condition_elseif}:")
            self.indent_level += 1
            self.generate_statements(elseif[2])
            self.indent_level -= 1

        if else_block:
            self.generate_else(else_block)

    def generate_else(self, else_block):
        if else_block:
            self.output.append(f"{'    ' * self.indent_level}else:")
            self.indent_level += 1
            self.generate_statements(else_block[1])
            self.indent_level -= 1

    def generate_while(self, node):
        condition = self.generate_expression(node[1])
        self.output.append(f"{'    ' * self.indent_level}while {condition}:")
        self.indent_level += 1
        self.generate_statements(node[2])
        self.indent_level -= 1

    def generate_for(self, node):
        init = self.generate_statement(node[1])
        condition = self.generate_expression(node[2])
        increment_expr = self.generate_expression(node[3])
        increment = f"{node[1][1]} = {increment_expr}"

        self.output.append(f"{'    ' * self.indent_level}{init}")
        self.output.append(f"{'    ' * self.indent_level}while {condition}:")
        self.indent_level += 1
        body_statements = node[4]
        for stmt in body_statements:
            self.generate_statement(stmt)
        self.output.append(f"{'    ' * self.indent_level}{increment}")
        self.indent_level -= 1

    def generate_statements(self, statements):
        for statement in statements:
            self.generate_statement(statement)

    def generate_statement(self, statement):
        if statement[0] == 'assignment':
            self.generate_assignment(statement)
        elif statement[0] == 'expression':
            if isinstance(statement[1], tuple) and statement[1][0] == 'postfix_op':
                var = self.generate_expression(statement[1][1])
                op = ' += 1' if statement[1][2] == '++' else ' -= 1'
                self.output.append(f"{'    ' * self.indent_level}{var}{op}")
            else:
                expr = self.generate_expression(statement[1])
                self.output.append(f"{'    ' * self.indent_level}{expr};")
        elif statement[0] == 'print':
            self.generate_print(statement)
        elif statement[0] == 'if':
            self.generate_if(statement)
        elif statement[0] == 'if_else':
            self.generate_if_else(statement)
        elif statement[0] == 'while':
            self.generate_while(statement)
        elif statement[0] == 'for':
            self.generate_for(statement)
        elif statement[0] == 'array_element_assignment':
            self.generate_array_element_assignment(statement)
        elif statement[0] == 'declaration':
            self.generate_declaration(statement)

    def generate_expression(self, node):
        if isinstance(node, int):
            return str(node)
        elif isinstance(node, float):
            return str(node)
        elif isinstance(node, str) and node.startswith('"') and node.endswith('"'):
            return node
        elif isinstance(node, str):
            if node.lower() in {"true", "false"}:
                return node.capitalize()
            return node
        elif isinstance(node, bool):
            return str(node)
        elif isinstance(node, tuple):
            if node[0] == 'binary_op':
                left_value = self.generate_expression(node[1])
                op = node[2]
                right_value = self.generate_expression(node[3])
                if op == '&&':
                    op = 'and'
                elif op == '||':
                    op = 'or'
                return f"({left_value} {op} {right_value})"
            elif node[0] == 'postfix_op':
                expr_value = self.generate_expression(node[1])
                if node[2] == '++':
                    return f"({expr_value} + 1)"
                elif node[2] == '--':
                    return f"({expr_value} - 1)"
            elif node[0] == 'unary_op':
                op = node[1]
                expr_value = self.generate_expression(node[2])
                if op == '!':
                    op = 'not'
                return f"({op} {expr_value})"
        raise TypeError(f"Unsupported expression: {node}")

    def to_python_code(self):
        return "\n".join(self.output)

# Example usage
ast = ('program', 'main', [
    ('declaration', 'int[]', [('myNum', [10, 20, 30, 40])]),
    ('print', 'writeln', ['myNum']),
    ('array_element_assignment', 'myNum', 0, 15),
    ('array_element_assignment', 'myNum', ('binary_op', 0, '+', 1), 10),
    ('print', 'writeln', ['myNum'])
])

interpreter = Interpreter()
python_code = interpreter.generate(ast)
print(python_code)
