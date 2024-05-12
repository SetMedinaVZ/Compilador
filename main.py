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
python_code = interpreter.generate(parsed_data)

# Save and run the generated Python code
def save_and_run_python_code(python_code):
    with open("temp.py", "w") as file:
        file.write(python_code)
    exec(open("temp.py").read())

save_and_run_python_code(python_code)
