from Lexer import Lexer
import os

dir_path = os.getcwd()
contents = os.listdir(dir_path + '/codes')

for i, filename in enumerate(contents):
    print(f'{i}: {filename}')
selected = input('Escribe el código de prueba a utilizar: ')
with open(dir_path + '/codes/' + contents[int(selected)], 'r') as file:
    data = file.read()

lexer = Lexer()
tokens = lexer.get_tokens(data)
print(tokens)
