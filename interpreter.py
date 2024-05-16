import sys
import os

class Interpreter:
    def __init__(self):
        self.variables = {}
        self.var_types = {} 
        self.output = []
        self.indent_level = 0

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

    def check_type(self, var_name, value_type):
        var_type = self.var_types.get(var_name)
        if var_type != value_type:
            raise TypeError(f"Variable '{var_name}' is of type '{var_type}' but got '{value_type}'")


    def check_expression_type(self, node):
        if isinstance(node, int):
            return 'int'
        elif isinstance(node, float):
            return 'float'
        elif isinstance(node, str) and node.startswith('"') and node.endswith('"'):
            return 'string'
        elif isinstance(node, str):
            if node.lower() in {"true", "false"}:  # Verificar valores booleanos
                return 'bool'
            return self.var_types.get(node, 'unknown')
        elif isinstance(node, bool):  # Reconocer booleanos True y False
            return 'bool'
        elif isinstance(node, tuple):
            if node[0] == 'binary_op':
                left_type = self.check_expression_type(node[1])
                right_type = self.check_expression_type(node[3])
                if left_type != right_type:
                    raise TypeError(f"Type mismatch in binary operation: {left_type} {node[2]} {right_type}")
                return 'bool' if node[2] in {'>', '<', '==', '!=', '>=', '<='} else left_type
            elif node[0] == 'postfix_op':
                expr_type = self.check_expression_type(node[1])
                if expr_type != 'int':
                    raise TypeError(f"Postfix operation on non-int type: {expr_type}")
                return 'int'
            if node[0] == 'unary_op':
                return self.check_expression_type(node[2])
        raise TypeError(f"Unsupported expression: {node}")


    def generate_declaration(self, node):
        if node[1] == 'int[]':  # Manejo especial para arrays
            self.generate_array_declaration(node)
        else:
            var_type = node[1]
            for var, expr in node[2]:
                self.var_types[var] = var_type  # Guardar el tipo de la variable
                if expr is None:
                    self.output.append(f"{'    ' * self.indent_level}{var} = None")
                else:
                    value = self.generate_expression(expr)
                    self.check_type(var, var_type)  # Verificar el tipo de la variable
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
        var_name = node[1]
        value_type = self.check_expression_type(node[2])
        self.var_types[var_name] = value_type  # Actualizar el tipo de la variable
        self.check_type(var_name, value_type)  # Verificar el tipo de la variable
        value = self.generate_expression(node[2])
        self.output.append(f"{'    ' * self.indent_level}{var_name} = {value}")


    def generate_print(self, node):
        # node[1] is 'writeln' or 'write'
        # node[2] is the list of expressions
        expressions = [self.generate_expression(expr) for expr in node[2]]
        if node[1] == 'writeln':
            self.output.append(f"{'    ' * self.indent_level}print({', '.join(expressions)})")
        else:
            # For 'write', using end='' to avoid newline
            self.output.append(f"{'    ' * self.indent_level}print({', '.join(expressions)}, end='')")


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
    
    def generate_if_else_if(self, node):
        condition = self.generate_expression(node[1])
        self.output.append(f"{'    ' * self.indent_level}if {condition}:")
        self.indent_level += 1
        self.generate_statements(node[2])
        self.indent_level -= 1

        for else_if in node[3]:
            else_if_condition = self.generate_expression(else_if[1])
            self.output.append(f"{'    ' * self.indent_level}elif {else_if_condition}:")
            self.indent_level += 1
            self.generate_statements(else_if[2])
            self.indent_level -= 1

        self.output.append(f"{'    ' * self.indent_level}else:")
        self.indent_level += 1
        self.generate_statements(node[4])
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
        elif statement[0] == 'if_else_if':
            self.generate_if_else_if(statement)
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
        if isinstance(node, int):
            return node
        elif isinstance(node, float):
            return node
        elif isinstance(node, str) and node.startswith('"') and node.endswith('"'):
            return node
        elif isinstance(node, str):
            if node.lower() in {"true", "false"}:  # Reconocer valores booleanos
                return node.capitalize()  # Convertir a True/False
            return node
        elif isinstance(node, bool):  # Manejar valores booleanos directamente
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

