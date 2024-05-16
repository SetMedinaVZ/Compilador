import sys
import os

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.output = []
        self.indent_level = 0  # Contador de indentación

    def generate(self, node):
        if node[0] == 'program':
            for statement in node[2]:
                self.generate(statement)
        elif node[0] == 'declaration':
            self.generate_declaration(node)
        elif node[0] == 'declaration_init':
            self.generate_declaration_init(node)
        elif node[0] == 'array_declaration':
            self.generate_array_declaration(node)
        elif node[0] == 'assignment':
            self.generate_assignment(node)
        elif node[0] == 'array_element_assignment':
            self.generate_array_element_assignment(node)
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
        return "\n".join(self.output)

    def generate_declaration(self, node):
        if node[1] == 'int[]':  # Manejo especial para arrays
            self.generate_array_declaration(node)
        else:
            for var, expr in node[2]:
                if expr is None:
                    self.output.append(f"{'    ' * self.indent_level}{var} = None")
                else:
                    value = self.generate_expression(expr)
                    self.output.append(f"{'    ' * self.indent_level}{var} = {value}")
        
    def generate_declaration_init(self, node):
        value = self.generate_expression(node[3])
        self.variables[node[2]] = value  # Opcional, si manejas un almacenamiento de variables
        self.output.append(f"{'    ' * self.indent_level}{node[2]} = {value}")
        
    def generate_array_declaration(self, node):
        if node[2][0][0] == 'assignment':
            var_name = node[2][0][1]
            values = node[2][0][2] if len(node[2][0]) > 2 else []
        else:
            var_name = node[2][0][0]
            values = []
        #operaciones binarias dentro
        processed_values = []
        for value in values:
            if isinstance(value, tuple) and value[0] == 'binary_op':
                processed_values.append(self.generate_expression(value))
            else:
                processed_values.append(value)

        if all(isinstance(value, int) for value in processed_values):
            values_str = ", ".join(map(str, processed_values))
            self.output.append(f"{'    ' * self.indent_level}{var_name} = [{values_str}]")
        else:
            error_message = "Array initialization must be a list of integers"
            save_and_exit("", error_message)
            
    def generate_array_element_assignment(self, node):
        var_name = node[1]
        index = self.generate_expression(node[2])
        value = self.generate_expression(node[3])

        if isinstance(value, int):
            self.output.append(f"{'    ' * self.indent_level}{var_name}[{index}] = {value}")
        else:
            error_message = "Array element assignment must be an integer"
            save_and_exit("", error_message)

    def generate_assignment(self, node):
        value = self.generate_expression(node[2])
        self.output.append(f"{'    ' * self.indent_level}{node[1]} = {value}")

    def generate_print(self, node):
        value = self.generate_expression(node[1])
        self.output.append(f"{'    ' * self.indent_level}print({value})")

    def generate_if(self, node):
        condition = self.generate_expression(node[1])
        self.output.append(f"{'    ' * self.indent_level}if {condition}:")
        self.indent_level += 1
        self.generate_statements(node[2])
        self.indent_level -= 1

    def generate_if_else(self, node):
        condition = self.generate_expression(node[1])
        self.output.append(f"{'    ' * self.indent_level}if {condition}:")
        self.indent_level += 1
        self.generate_statements(node[2])
        self.indent_level -= 1
        self.output.append(f"{'    ' * self.indent_level}else:")
        self.indent_level += 1
        self.generate_statements(node[3])
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
        elif statement[0] == 'array_declaration':
            self.generate_array_declaration(statement)
        elif statement[0] == 'declaration_init':
            self.generate_declaration_init(statement)

    def generate_expression(self, node):
        if isinstance(node, int): # Se usa en los arrays
            return node
        elif isinstance(node, tuple):
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

    def to_python_code(self):
        return "\n".join(self.output)

def save_and_exit(python_code, error=None):
    with open("temp.py", "w") as file:
        if error:
            file.write(f"def report_error():\n")
            file.write(f"    print('Error: {error}')\n\n")
            file.write(f"report_error()\n")
        else:
            file.write(python_code)

    if error:
        print(f"Error: {error}. Exiting to run temp.py.")
    else:
        print("Python code saved to temp.py. Exiting to run temp.py.")
    os._exit(0)

