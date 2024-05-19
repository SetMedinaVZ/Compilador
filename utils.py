import os 
import sys 

def print_red(message):
    red_color_code = "\033[91m"
    reset_color_code = "\033[0m"
    print(f'{red_color_code}{message}{reset_color_code}', file=sys.stderr)

def print_green(message):
    green_color_code = "\033[92m"
    reset_color_code = "\033[0m"
    print(f'{green_color_code}{message}{reset_color_code}')
    

def save_and_exit(python_code, error=None):
    with open("temp.py", "w") as file:
        if error:
            file.write(f"import sys\n")
            file.write(f"import os\n\n")
            file.write(f"def print_red(message):\n")
            file.write(f"    red_color_code = \"\\033[91m\"\n")
            file.write(f"    reset_color_code = \"\\033[0m\"\n")
            file.write(f"    print(f'{{red_color_code}}{{message}}{{reset_color_code}}', file=sys.stderr)\n\n")
            file.write("def report_error():\n")
            error = str(error).replace("'", "\\'")
            file.write(f"    print_red('Error: {error}')\n\n")
            file.write("report_error()\n")
        else:
            file.write(python_code)

    if error:
        print_red('Ups! Error: ' +  error + ' . Look at temp.py file generated for more information.')
    else:
        print("Python code saved to temp.py. Exiting to run temp.py.")
    os._exit(0)
