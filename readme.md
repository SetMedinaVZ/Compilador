# Bienvenidos
TC3002B ITESM

Proyecto de un pseudo compilador en Python para el modulo de compiladores de la clase Desarrollo de aplicaciones avanzadas de ciencias computacionales con el profesor Paco Peña.
Sientanse libres de usar el codigo para los que estan en esta clase con el mismo profesor, y  recuerden:

>Si Paco Peña opina, no estoy de acuerdo.

>Si Paco Peña habla, ignoro.

>Si Paco Peña falla, juzgo.

>Si Paco Peña piensa, desprecio.

>Si Paco Peña tiene 100 haters, yo soy uno de ellos.

>Si Paco Peña tiene 1 hater, yo soy ese hater.

>Si Paco Peña no tiene un hater, yo no existo.


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
