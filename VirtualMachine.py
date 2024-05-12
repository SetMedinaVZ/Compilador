import sys


class VirtualMachine:
    def __init__(self, quadruples):
        self.quadruples = quadruples
        self.memory = {}
        self.output = []

    def declare_vars(self, declarations):
        for var in declarations:
            var_type, var_name = var
            if var_type == 'int':
                self.memory[var_name] = 0
            elif var_type == 'float':
                self.memory[var_name] = 0.0
            elif var_type == 'string':
                self.memory[var_name] = ""

    def build(self):
        pc = 0
        while pc < len(self.quadruples):
            op, arg1, arg2, res = self.quadruples[pc]
            # ASSIGN
            if op == '=':
                # We make sure the variable has already been declared
                if self.memory.get(res) is not None:
                    var_type = type(self.memory.get(res))
                    # We make sure they're both the same type
                    if var_type == type(arg1):
                        # Assign new value to variable
                        self.memory[res] = arg1
                    else:
                        sys.exit(f'ERROR: variable {res} and value {arg1} are not the same type.')
                else:
                    sys.exit(f'ERROR: variable {res} was not declared.')
            # LESS THAN
            elif op == '<':
                # First check if the value to assign has been declared or is a temp variable
                if self.memory.get(res) is not None:
                    # Variable exists
                    self.memory[res] = arg1 < arg2
                else:
                    # Variable doesn't exist, check if temp variable
                    if res.startswith('T'):
                        # Temp value
                        self.memory.update({res: arg1 < arg2})
                    else:
                        sys.exit(f'ERROR: variable {res} was not declared.')
            # GREATER THAN
            elif op == '>':
                # First check if the value to assign has been declared or is a temp variable
                if self.memory.get(res) is not None:
                    # Variable exists
                    self.memory[res] = arg1 > arg2
                else:
                    # Variable doesn't exist, check if temp variable
                    if res.startswith('T'):
                        # Temp value
                        self.memory.update({res: arg1 > arg2})
                    else:
                        sys.exit(f'ERROR: variable {res} was not declared.')
            # LESS THAN OR EQUALS
            elif op == '<=':
                # First check if the value to assign has been declared or is a temp variable
                if self.memory.get(res) is not None:
                    # Variable exists
                    self.memory[res] = arg1 <= arg2
                else:
                    # Variable doesn't exist, check if temp variable
                    if res.startswith('T'):
                        # Temp value
                        self.memory.update({res: arg1 <= arg2})
                    else:
                        sys.exit(f'ERROR: variable {res} was not declared.')
            # GREATER THAN OR EQUALS
            elif op == '>=':
                # First check if the value to assign has been declared or is a temp variable
                if self.memory.get(res) is not None:
                    # Variable exists
                    self.memory[res] = arg1 >= arg2
                else:
                    # Variable doesn't exist, check if temp variable
                    if res.startswith('T'):
                        # Temp value
                        self.memory.update({res: arg1 >= arg2})
                    else:
                        sys.exit(f'ERROR: variable {res} was not declared.')
            # NOT EQUALS
            # PLUS
            # MINUS
            # TIMES
            # DIVIDE
            # WRITELN
            # GOTO F
            # GOTO V
            # GOTO
            pc += 1

    def run(self):
        print(self.output)


# Op  Arg1  Arg2  Res
quadruples = [
    ('writeln', '"texto dump"', None, None),  # 0
    ('=', 5, None, 'f'),  # 1
    ('=', 0, None, 'x'),  # 2
    ('<', 'x', 'f', 'T1'),  # 3
    ('gotoF', 'T1', None, 11),  # 4
    ('gotoV', 'T1', None, 8),  # 5
    ('+', 'i', 1, 'i'),  # 6
    ('goto', None, None, 4),  # 7
    ('+', 'x', 'f', 'T2'),  # 8
    # ('=', 'T2', None, 'n'),  # 9
    # ('goto', None, None, 7),  # 10
    # ('writeln', 'n', None, None),  # 11
]

declarations = [
    ('int', 'i'),
    ('int', 'n'),
    ('int', 'f'),
    ('int', 'x')
]

vm = VirtualMachine(quadruples)
vm.declare_vars(declarations)
print(vm.memory)
vm.build()
print(vm.memory)
