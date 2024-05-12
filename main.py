import sys
import os
from parser_ import Parser
from interpreter import Interpreter, save_and_exit

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

# Save the Python code to temp.py and exit
save_and_exit(python_code)

# Command to run temp.py after the main script exits
os.system(f"{sys.executable} temp.py")
