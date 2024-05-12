# Python Transpiler and Interpreter

## Description
This project is a simple transpiler and interpreter for a custom programming language.

## Requirements
- Python 3.x
- `ply` library

## Usage
To run the main script with a specific code file, use the following command:

```bash
python main.py {your-file-path}
```
```bash
python temp.py
```


## FALTA: CORREGIR EN EL PARSER ESTE ERROR: 

1) Este caso no funciona. Cuando se inicializa e iguala un valor en la misma linea 
```bash
program main {
    int b = 0;
    writeln(b);
}
```

2) En comparación, este caso si funciona: 
```bash
program main {
    int b ;
    b = 0;
    writeln(b);
}
