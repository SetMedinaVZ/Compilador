# Documentación del Parser

## Descripción General

Este parser es parte de un compilador diseñado para analizar y transformar un conjunto de instrucciones de un lenguaje de programación específico en una representación intermedia conocida como árbol de nodos abstractos (AST). El parser utiliza la biblioteca PLY para analizar la gramática del lenguaje.

## Árbol de Nodos

```plaintext
program (ID)
└── statement_list
    ├── declaration_statement
    │   ├── type
    │   └── declaration_list
    ├── assignment_statement
    │   ├── ID
    │   └── expression
    ├── if_statement
    │   ├── expression
    │   ├── statement_list
    │   ├── else_if_list
    │   └── optional_else
    ├── expression_statement
    │   └── expression
    └── print_statement
        └── expression_list
```

El árbol de nodos representa la estructura sintáctica del código fuente analizado. A continuación, se detalla el formato general del árbol generado por el parser:

- **program**: Nodo raíz del programa que incluye un identificador y una lista de sentencias.
  - **ID**: Identificador del programa.
  - **statement_list**: Lista de todas las sentencias del programa.

### Tipos de Sentencias y Expresiones

Las sentencias y expresiones dentro del árbol se categorizan como sigue:

#### Declaraciones
- **declaration_statement**: Define variables con un tipo específico.
  - **type**: Tipo de la variable (int, float, bool, string, array).
  - **declaration_list**: Lista de variables a declarar.

#### Asignaciones
- **assignment_statement**: Asigna un valor a una variable.
  - **ID**: Identificador de la variable.
  - **expression**: Expresión cuyo valor se asignará a la variable.

#### Sentencias de Control
- **if_statement**: Sentencia condicional if.
  - **expression**: Condición a evaluar.
  - **statement_list**: Lista de sentencias a ejecutar si la condición es verdadera.
  - **else_if_list**: Lista opcional de condiciones else if.
  - **optional_else**: Bloque else opcional.

- **while_statement**: Sentencia de bucle while.
  - **expression**: Condición para la iteración.
  - **statement_list**: Sentencias a ejecutar mientras la condición sea verdadera.

- **for_statement**: Sentencia de bucle for.
  - **assignment_statement**: Inicialización de la variable del bucle.
  - **expression**: Condición para continuar el bucle.
  - **statement_list**: Sentencias dentro del bucle for.

#### Expresiones
- **expression_statement**: Evalúa una expresión y descarta su valor.
  - **expression**: Expresión a evaluar.

- **print_statement**: Imprime valores en consola.
  - **expression_list**: Lista de expresiones a imprimir.

## Funciones del Parser

### Función `parse`

Esta función es el punto de entrada para analizar el código fuente. Utiliza el lexer para generar tokens y el parser para construir el árbol de nodos basado en estos tokens.

### Función `p_error`

Maneja errores sintácticos que el parser no puede resolver. Proporciona mensajes de error que incluyen el número de línea y el token que causó el error.

## Uso del Parser

Para usar el parser, proporciona el nombre del archivo de código fuente como argumento al script. El parser leerá el archivo, analizará su contenido y generará un árbol de nodos que representa la estructura del programa.

```bash
python parser.py <filename>
```