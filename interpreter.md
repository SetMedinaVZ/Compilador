# Documentación del Intérprete

## Descripción General

Este intérprete está diseñado para ejecutar un árbol de nodos abstractos (AST) generado por un parser. Convierte el AST en código Python ejecutable, manejando diferentes tipos de nodos como declaraciones, asignaciones, y estructuras de control.

## Estructura del Intérprete

El intérprete se compone de varias funciones principales que juntas interpretan y ejecutan el AST generado:

- **generate**: Función principal que recibe el nodo raíz del AST y decide qué función específica llamar según el tipo de nodo.
- **generate_declaration**: Maneja las declaraciones de variables.
- **generate_assignment**: Gestiona las asignaciones a variables.
- **generate_print**: Prepara las sentencias de impresión.
- **generate_if**, **generate_while**, **generate_for**: Funciones que manejan las estructuras de control if, while y for respectivamente.
- **check_type** y **check_expression_type**: Funciones que verifican los tipos de las variables y las expresiones para asegurar coherencia en los tipos de datos.
- **generate_expression**: Convierte las expresiones del AST en expresiones Python.

## Estructuras de Nodos

El intérprete puede recibir varios tipos de nodos del AST generado por el parser. Cada tipo de nodo representa diferentes componentes del lenguaje fuente y es manejado específicamente por el intérprete para generar el código Python adecuado. 

La estructura de los nodos se puede revisar en la documentacion del parser, sección [Árbol de Nodos](parser.md#Árbol-de-Nodos).


## Funciones Detalladas

### `generate(node)`
Esta es la función principal que interpreta el AST. Recorre el árbol y delega cada nodo a su función específica según el tipo de nodo (por ejemplo, declaración, asignación).

### `generate_declaration(node)`
Maneja las declaraciones de variables simples y las inicializaciones de las mismas. Asegura que cada variable declarada sea registrada con su tipo correcto.

### `generate_assignment(node)`
Procesa las asignaciones, asegurándose de que las variables ya estén declaradas y que los tipos de datos de las asignaciones sean coherentes con los declarados.

### `generate_print(node)`
Prepara las sentencias de impresión, maneja tanto `write` como `writeln`.

### `generate_if(node)`, `generate_while(node)`, `generate_for(node)`
Estas funciones gestionan las estructuras de control, traduciendo las condiciones y bloques de sentencias a su equivalente en Python.

### `check_type(var_name, value_type)`
Verifica que el tipo de dato de una variable coincida con el tipo declarado, lanzando una excepción de tipo si no coincide.

### `check_expression_type(node)`
Determina el tipo de una expresión basada en su estructura y contenido. Es crucial para la coherencia de tipos en el intérprete.

### `generate_expression(node)`
Transforma una expresión del AST en una expresión Python. Maneja operaciones binarias, unarias y referencias a variables.

