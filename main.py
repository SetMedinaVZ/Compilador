import sys
from parser_ import Parser
from interpreter import Interpreter

if len(sys.argv) != 2:
    print("Usage: python main.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

parser = Parser()

with open(filename, 'r') as file:
    data = file.read()

parsed_data = parser.parse(data)
interpreter = Interpreter()
interpreter.interpret(parsed_data)
