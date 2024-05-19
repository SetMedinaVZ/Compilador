import sys
import os
from Parser import Parser
from Interpreter import Interpreter
from utils import save_and_exit

def main():
    if len(sys.argv) != 2:
        print("Starting the program requires a single argument: Add the path to the file you want to run.")
        sys.exit(1)

    filename = sys.argv[1]

    parser = Parser()

    try:
        with open(filename, 'r') as file:
            data = file.read()

        parsed_data = parser.parse(data)
        interpreter = Interpreter()
        python_code = interpreter.generate(parsed_data)

        save_and_exit(python_code)

    except Exception as e:
        error_message = str(e)
        python_code = ""
        save_and_exit(python_code, error=error_message)

    # Command to run temp.py after the main script exits
    os.system(f"{sys.executable} temp.py")

if __name__ == "__main__":
    main()
